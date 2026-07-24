"""Captura local verificada de ``processed``, ``exports`` e ``warehouse``."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

import pandas as pd
from google.auth.transport.requests import AuthorizedSession

from sbmi.inbox_snapshot import (
    SNAPSHOT_ID_PATTERN,
    _download_file,
    _safe_relative_path,
    planned_bytes,
    select_inbox_files,
)

DEFAULT_DERIVED_SCOPES = ("processed", "exports", "warehouse")


@dataclass(frozen=True)
class DerivedProductsSnapshotResult:
    """Resumo da captura local concluída."""

    snapshot_path: Path
    files: int
    bytes: int
    scopes: tuple[str, ...]


def normalize_scopes(scopes: tuple[str, ...] | list[str]) -> tuple[str, ...]:
    """Normaliza escopos sem aceitar caminhos relativos inseguros."""
    normalized: list[str] = []
    for scope in scopes:
        value = str(scope).strip().strip("/")
        if not value:
            continue
        pure = PurePosixPath(value)
        if pure.is_absolute() or any(part in {".", ".."} for part in pure.parts):
            raise ValueError(f"Escopo inválido: {scope!r}")
        normalized.append(pure.as_posix())
    unique = tuple(dict.fromkeys(normalized))
    if not unique:
        raise ValueError("Ao menos um escopo derivado deve ser informado.")
    return unique


def select_derived_files(
    inventory: pd.DataFrame,
    scopes: tuple[str, ...] | list[str] = DEFAULT_DERIVED_SCOPES,
) -> pd.DataFrame:
    """Seleciona arquivos derivados preservando metadados de validação."""
    normalized = normalize_scopes(scopes)
    selected = [select_inbox_files(inventory, scope) for scope in normalized]
    frame = pd.concat(selected, ignore_index=True)
    if frame["relative_path"].duplicated().any():
        duplicated = sorted(
            frame.loc[frame["relative_path"].duplicated(False), "relative_path"]
            .astype(str)
            .unique()
        )
        raise ValueError(f"Arquivos selecionados por mais de um escopo: {duplicated}")
    return frame.sort_values("relative_path").reset_index(drop=True)


def snapshot_derived_products(
    session: AuthorizedSession,
    inventory: pd.DataFrame,
    snapshots_root: Path,
    *,
    snapshot_id: str,
    scopes: tuple[str, ...] | list[str] = DEFAULT_DERIVED_SCOPES,
    max_total_bytes: int = 350_000_000,
) -> DerivedProductsSnapshotResult:
    """Baixa produtos derivados sem reconstruí-los nem escrever no Drive."""
    if SNAPSHOT_ID_PATTERN.fullmatch(snapshot_id) is None:
        raise ValueError("Identificador de snapshot inválido.")
    if max_total_bytes <= 0:
        raise ValueError("max_total_bytes deve ser maior que zero.")

    normalized_scopes = normalize_scopes(scopes)
    selected = select_derived_files(inventory, normalized_scopes)
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
                    "scope": PurePosixPath(*relative_path.parts).parts[0],
                    "expected_size_bytes": expected_size,
                    "downloaded_size_bytes": downloaded,
                    "expected_sha256": expected_sha256,
                    "local_sha256": local_sha256,
                    "verification_status": "VERIFIED",
                }
            )

        pd.DataFrame(manifest_rows).to_csv(
            partial_path / "snapshot_manifest.csv",
            index=False,
        )
        partial_path.replace(final_path)
    except Exception:
        shutil.rmtree(partial_path, ignore_errors=True)
        raise

    return DerivedProductsSnapshotResult(
        snapshot_path=final_path,
        files=len(manifest_rows),
        bytes=total_bytes,
        scopes=normalized_scopes,
    )
