"""Captura local verificada de fontes brutas selecionadas por caminho exato."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

import pandas as pd
from google.auth.transport.requests import AuthorizedSession

from sbmi.inbox_snapshot import (
    REQUIRED_COLUMNS,
    SNAPSHOT_ID_PATTERN,
    _download_file,
    _folder_mask,
    _safe_relative_path,
    planned_bytes,
)


@dataclass(frozen=True)
class SourceSnapshotResult:
    """Resumo da captura seletiva concluída."""

    snapshot_path: Path
    files: int
    bytes: int


def normalize_requested_paths(relative_paths: Iterable[str]) -> tuple[str, ...]:
    """Normaliza caminhos solicitados e rejeita valores inseguros."""
    normalized: list[str] = []
    for value in relative_paths:
        safe = _safe_relative_path(value)
        normalized.append(PurePosixPath(*safe.parts).as_posix())
    unique = tuple(dict.fromkeys(normalized))
    if not unique:
        raise ValueError("Ao menos um caminho de fonte deve ser informado.")
    return unique


def select_exact_source_files(
    inventory: pd.DataFrame,
    relative_paths: Iterable[str],
) -> pd.DataFrame:
    """Seleciona arquivos não-pasta por correspondência exata de caminho."""
    missing = REQUIRED_COLUMNS.difference(inventory.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")

    requested = normalize_requested_paths(relative_paths)
    frame = inventory.copy()
    frame["relative_path"] = (
        frame["relative_path"].fillna("").astype(str).str.strip("/")
    )
    frame["is_folder"] = _folder_mask(frame["is_folder"])
    frame["size_bytes"] = pd.to_numeric(frame["size_bytes"], errors="coerce")
    frame["sha256_checksum"] = (
        frame["sha256_checksum"].fillna("").astype(str).str.strip().str.lower()
    )

    selected = frame.loc[
        frame["relative_path"].isin(requested) & ~frame["is_folder"]
    ].copy()
    found = set(selected["relative_path"].astype(str))
    not_found = sorted(set(requested).difference(found))
    if not_found:
        raise ValueError(f"Fontes não encontradas no inventário: {not_found}")
    if selected["relative_path"].duplicated().any():
        duplicated = sorted(
            selected.loc[
                selected["relative_path"].duplicated(False),
                "relative_path",
            ]
            .astype(str)
            .unique()
        )
        raise ValueError(f"Caminhos duplicados no inventário: {duplicated}")
    if selected["drive_file_id"].fillna("").astype(str).str.strip().eq("").any():
        raise ValueError("Há fontes sem drive_file_id.")
    if selected["size_bytes"].isna().any():
        paths = selected.loc[selected["size_bytes"].isna(), "relative_path"].tolist()
        raise ValueError(f"Há fontes sem tamanho informado: {paths}")

    return selected.sort_values("relative_path").reset_index(drop=True)


def snapshot_source_files(
    session: AuthorizedSession,
    inventory: pd.DataFrame,
    snapshots_root: Path,
    *,
    relative_paths: Iterable[str],
    snapshot_id: str,
    max_total_bytes: int = 100_000_000,
) -> SourceSnapshotResult:
    """Baixa fontes exatas, valida tamanho e hash e publica atomicamente."""
    if SNAPSHOT_ID_PATTERN.fullmatch(snapshot_id) is None:
        raise ValueError("Identificador de snapshot inválido.")
    if max_total_bytes <= 0:
        raise ValueError("max_total_bytes deve ser maior que zero.")

    selected = select_exact_source_files(inventory, relative_paths)
    total_bytes = planned_bytes(selected)
    if total_bytes > max_total_bytes:
        raise ValueError(
            "Captura bloqueada pelo limite: "
            f"planejado={total_bytes}, limite={max_total_bytes}"
        )

    root = snapshots_root.expanduser().resolve()
    final_path = root / snapshot_id
    partial_path = root / f".{snapshot_id}.partial"
    if final_path.exists() or partial_path.exists():
        raise FileExistsError(f"A captura já existe ou está incompleta: {snapshot_id}")

    partial_path.mkdir(parents=True, exist_ok=False)
    manifest_rows: list[dict[str, Any]] = []
    try:
        for row in selected.itertuples(index=False):
            relative_path = _safe_relative_path(row.relative_path)
            target = partial_path / relative_path
            expected_size = int(row.size_bytes)
            expected_sha256 = str(row.sha256_checksum or "").strip().lower()
            downloaded, local_sha256 = _download_file(
                session=session,
                file_id=str(row.drive_file_id),
                target=target,
                expected_size=expected_size,
                expected_sha256=expected_sha256,
            )
            manifest_rows.append(
                {
                    "drive_file_id": str(row.drive_file_id),
                    "relative_path": PurePosixPath(*relative_path.parts).as_posix(),
                    "expected_size_bytes": expected_size,
                    "downloaded_size_bytes": downloaded,
                    "expected_sha256": expected_sha256,
                    "local_sha256": local_sha256,
                    "verification_status": "VERIFIED",
                }
            )

        pd.DataFrame(manifest_rows).to_csv(
            partial_path / "source_manifest.csv",
            index=False,
        )
        final_path.parent.mkdir(parents=True, exist_ok=True)
        partial_path.replace(final_path)
    except Exception:
        shutil.rmtree(partial_path, ignore_errors=True)
        raise

    return SourceSnapshotResult(
        snapshot_path=final_path,
        files=len(manifest_rows),
        bytes=total_bytes,
    )
