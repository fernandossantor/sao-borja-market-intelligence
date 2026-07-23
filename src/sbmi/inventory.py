"""Inventário local de arquivos com hash SHA-256."""

import hashlib
from pathlib import Path

import pandas as pd

CHUNK_SIZE = 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file_obj:
        while chunk := file_obj.read(CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def build_inventory(root: Path) -> pd.DataFrame:
    root = root.expanduser().resolve()
    if not root.exists():
        raise FileNotFoundError(f"Diretório não encontrado: {root}")
    if not root.is_dir():
        raise NotADirectoryError(f"O caminho não é um diretório: {root}")

    records: list[dict[str, object]] = []

    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        stat = path.stat()
        records.append(
            {
                "relative_path": path.relative_to(root).as_posix(),
                "file_name": path.name,
                "extension": path.suffix.lower(),
                "size_bytes": stat.st_size,
                "modified_at_utc": pd.Timestamp(stat.st_mtime, unit="s", tz="UTC"),
                "sha256": sha256_file(path),
                "audit_status": "PENDING_AUDIT",
            }
        )

    columns = [
        "relative_path",
        "file_name",
        "extension",
        "size_bytes",
        "modified_at_utc",
        "sha256",
        "audit_status",
    ]
    return pd.DataFrame(records, columns=columns)


def duplicate_candidates(inventory: pd.DataFrame) -> pd.DataFrame:
    required = {"relative_path", "size_bytes", "sha256"}
    missing = required.difference(inventory.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")

    duplicated = inventory[inventory.duplicated("sha256", keep=False)].copy()
    if duplicated.empty:
        return pd.DataFrame(
            columns=["sha256", "size_bytes", "relative_path", "duplicate_class"]
        )

    duplicated["duplicate_class"] = "EXACT_DUPLICATE"
    return duplicated[
        ["sha256", "size_bytes", "relative_path", "duplicate_class"]
    ].sort_values(["sha256", "relative_path"])
