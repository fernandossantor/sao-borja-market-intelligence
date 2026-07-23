"""Captura seletiva e verificável dos arquivos de ``raw/new_files``."""

from __future__ import annotations

import hashlib
import re
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path, PurePosixPath
from typing import Any

import pandas as pd
from google.auth.transport.requests import AuthorizedSession

from sbmi.google_drive import DRIVE_API_BASE
from sbmi.inbox_audit import DEFAULT_INBOX_PREFIX

SNAPSHOT_ID_PATTERN = re.compile(r"^[A-Za-z0-9._-]+$")
REQUIRED_COLUMNS = {
    "drive_file_id",
    "relative_path",
    "is_folder",
    "size_bytes",
    "sha256_checksum",
}


@dataclass(frozen=True)
class SnapshotResult:
    """Resumo da captura local concluída."""

    snapshot_path: Path
    files: int
    bytes: int


def default_snapshot_id() -> str:
    """Gera identificador UTC estável para a captura."""
    return datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")


def _folder_mask(series: pd.Series) -> pd.Series:
    if pd.api.types.is_bool_dtype(series):
        return series.fillna(False).astype(bool)

    normalized = series.fillna(False).astype(str).str.strip().str.lower()
    truthy = {"true", "1", "yes", "sim"}
    falsy = {"false", "0", "no", "não", "nao", "", "none", "nan"}
    unknown = set(normalized.unique()).difference(truthy | falsy)
    if unknown:
        raise ValueError(f"Valores inválidos em is_folder: {sorted(unknown)}")
    return normalized.isin(truthy)


def _normalized_prefix(prefix: str) -> str:
    value = prefix.strip().strip("/")
    if not value:
        raise ValueError("O prefixo da caixa de entrada não pode estar vazio.")
    parts = PurePosixPath(value).parts
    if any(part in {".", ".."} for part in parts):
        raise ValueError("O prefixo da caixa de entrada não pode conter '.' ou '..'.")
    return PurePosixPath(value).as_posix()


def _safe_relative_path(value: object) -> Path:
    text = str(value or "").strip().strip("/")
    pure = PurePosixPath(text)
    if not text or pure.is_absolute() or any(part in {".", ".."} for part in pure.parts):
        raise ValueError(f"Caminho relativo inválido: {value!r}")
    return Path(*pure.parts)


def select_inbox_files(
    inventory: pd.DataFrame,
    inbox_prefix: str = DEFAULT_INBOX_PREFIX,
) -> pd.DataFrame:
    """Seleciona somente arquivos da caixa de entrada, preservando metadados de validação."""
    missing = REQUIRED_COLUMNS.difference(inventory.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")

    prefix = _normalized_prefix(inbox_prefix)
    frame = inventory.copy()
    frame["relative_path"] = frame["relative_path"].fillna("").astype(str).str.strip("/")
    frame["is_folder"] = _folder_mask(frame["is_folder"])
    frame["size_bytes"] = pd.to_numeric(frame["size_bytes"], errors="coerce")
    frame["sha256_checksum"] = (
        frame["sha256_checksum"].fillna("").astype(str).str.strip().str.lower()
    )

    in_scope = frame["relative_path"].str.startswith(f"{prefix}/")
    selected = frame.loc[in_scope & ~frame["is_folder"]].copy()
    selected = selected.sort_values("relative_path").reset_index(drop=True)

    if selected.empty:
        raise ValueError(f"Nenhum arquivo encontrado sob {prefix}.")
    if selected["drive_file_id"].fillna("").astype(str).str.strip().eq("").any():
        raise ValueError("Há arquivos sem drive_file_id na seleção.")
    if selected["size_bytes"].isna().any():
        paths = selected.loc[selected["size_bytes"].isna(), "relative_path"].tolist()
        raise ValueError(f"Há arquivos sem tamanho informado: {paths}")

    for relative_path in selected["relative_path"]:
        _safe_relative_path(relative_path)
    return selected


def planned_bytes(selected: pd.DataFrame) -> int:
    """Calcula o volume total conhecido da captura."""
    return int(pd.to_numeric(selected["size_bytes"], errors="raise").sum())


def _download_file(
    session: AuthorizedSession,
    file_id: str,
    target: Path,
    expected_size: int,
    expected_sha256: str,
    chunk_size: int = 1024 * 1024,
) -> tuple[int, str]:
    """Baixa um arquivo binário e valida tamanho e SHA-256 antes da publicação local."""
    if target.exists():
        raise FileExistsError(f"O destino já existe: {target}")

    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(f".{target.name}.part")
    digest = hashlib.sha256()
    downloaded = 0

    try:
        response = session.get(
            f"{DRIVE_API_BASE}/{file_id}",
            params={"alt": "media", "supportsAllDrives": "true"},
            stream=True,
            timeout=120,
        )
        response.raise_for_status()
        with temporary.open("wb") as destination:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if not chunk:
                    continue
                destination.write(chunk)
                digest.update(chunk)
                downloaded += len(chunk)

        local_sha256 = digest.hexdigest()
        if downloaded != expected_size:
            raise ValueError(
                f"Tamanho divergente para {target.name}: esperado={expected_size}, obtido={downloaded}"
            )
        if expected_sha256 and local_sha256 != expected_sha256.lower():
            raise ValueError(
                f"SHA-256 divergente para {target.name}: esperado={expected_sha256}, obtido={local_sha256}"
            )

        temporary.replace(target)
        return downloaded, local_sha256
    except Exception:
        temporary.unlink(missing_ok=True)
        raise


def snapshot_inbox(
    session: AuthorizedSession,
    inventory: pd.DataFrame,
    snapshots_root: Path,
    inbox_prefix: str = DEFAULT_INBOX_PREFIX,
    snapshot_id: str | None = None,
    max_total_bytes: int = 10_000_000,
) -> SnapshotResult:
    """Cria captura local imutável da caixa de entrada, sem escrever no Drive."""
    selected = select_inbox_files(inventory, inbox_prefix)
    total_bytes = planned_bytes(selected)
    if total_bytes > max_total_bytes:
        raise ValueError(
            f"Captura bloqueada pelo limite: planejado={total_bytes}, limite={max_total_bytes}"
        )

    resolved_id = snapshot_id or default_snapshot_id()
    if SNAPSHOT_ID_PATTERN.fullmatch(resolved_id) is None:
        raise ValueError("Identificador de snapshot inválido.")

    root = snapshots_root.expanduser().resolve()
    final_path = root / resolved_id
    partial_path = root / f".{resolved_id}.partial"
    if final_path.exists() or partial_path.exists():
        raise FileExistsError(f"A captura já existe ou está incompleta: {resolved_id}")

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
            partial_path / "snapshot_manifest.csv",
            index=False,
        )
        partial_path.replace(final_path)
    except Exception:
        shutil.rmtree(partial_path, ignore_errors=True)
        raise

    return SnapshotResult(
        snapshot_path=final_path,
        files=len(manifest_rows),
        bytes=total_bytes,
    )
