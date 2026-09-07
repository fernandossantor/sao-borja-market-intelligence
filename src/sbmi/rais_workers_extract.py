"""Streaming extraction helpers for public RAIS worker archives."""

from __future__ import annotations

import csv
import hashlib
import io
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RaisMunicipalityExtract:
    """Audit information for a municipality-only RAIS worker extract."""

    output_path: Path
    rows_source: int
    rows_selected: int
    columns: int
    size_bytes: int
    sha256: str
    reused_existing: bool


def normalize_code(value: object) -> str:
    """Normalize RAIS code fields without changing significant leading zeros."""
    text = str(value).strip().strip('"')
    return text[:-2] if text.endswith(".0") else text


def _sha256(path: Path, *, chunk_size: int = 8 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inspect_existing_extract(
    output: Path,
    *,
    municipality_column: str,
    municipality_code: str,
    expected_columns: int | None = None,
    expected_rows: int | None = None,
) -> RaisMunicipalityExtract:
    """Validate an existing UTF-8 municipality extract before reuse."""
    rows = 0
    with Path(output).open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        header = next(reader)
        if municipality_column not in header:
            raise ValueError(f"Coluna municipal ausente em {output}: {municipality_column}")
        if expected_columns is not None and len(header) != expected_columns:
            raise ValueError(
                f"Largura divergente em {output}: observado={len(header)}, "
                f"esperado={expected_columns}"
            )
        municipality_idx = header.index(municipality_column)
        for row in reader:
            if len(row) != len(header):
                raise ValueError(
                    f"Linha com largura divergente em {output}: "
                    f"observado={len(row)}, esperado={len(header)}"
                )
            if normalize_code(row[municipality_idx]) != municipality_code:
                raise ValueError(
                    f"Extrato contém município diferente de {municipality_code}: {output}"
                )
            rows += 1
    if expected_rows is not None and rows != expected_rows:
        raise ValueError(
            f"Quantidade de linhas divergente em {output}: observado={rows}, "
            f"esperado={expected_rows}"
        )
    return RaisMunicipalityExtract(
        output_path=Path(output),
        rows_source=-1,
        rows_selected=rows,
        columns=len(header),
        size_bytes=Path(output).stat().st_size,
        sha256=_sha256(Path(output)),
        reused_existing=True,
    )


def extract_municipality_from_7z_csv(
    archive: Path,
    *,
    member: str,
    output: Path,
    municipality_column: str,
    municipality_code: str,
    source_encoding: str = "latin-1",
    expected_columns: int | None = None,
    expected_rows: int | None = None,
) -> RaisMunicipalityExtract:
    """Stream one archived CSV member through 7-Zip and keep one municipality."""
    archive = Path(archive)
    output = Path(output)
    if output.exists():
        return inspect_existing_extract(
            output,
            municipality_column=municipality_column,
            municipality_code=municipality_code,
            expected_columns=expected_columns,
            expected_rows=expected_rows,
        )

    sevenzip = shutil.which("7zz") or shutil.which("7z") or shutil.which("7za")
    if sevenzip is None:
        raise RuntimeError("7-Zip não encontrado; instale 7z/7zz/7za no Codespace")

    output.parent.mkdir(parents=True, exist_ok=True)
    partial = output.with_name(f"{output.name}.partial")
    if partial.exists():
        raise FileExistsError(f"Extrato parcial já existe; revise antes de continuar: {partial}")

    proc = subprocess.Popen(
        [sevenzip, "x", "-so", str(archive), member],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert proc.stdout is not None
    assert proc.stderr is not None
    text = io.TextIOWrapper(proc.stdout, encoding=source_encoding, newline="", errors="strict")
    reader = csv.reader(text, delimiter=",", quotechar='"')
    header = next(reader)
    if municipality_column not in header:
        proc.kill()
        raise ValueError(f"Coluna municipal ausente no RAIS: {municipality_column}")
    if expected_columns is not None and len(header) != expected_columns:
        proc.kill()
        raise ValueError(
            "Largura do cabeçalho RAIS divergente: "
            f"observado={len(header)}, esperado={expected_columns}"
        )

    municipality_idx = header.index(municipality_column)
    rows_source = 0
    rows_selected = 0
    try:
        with partial.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle)
            writer.writerow(header)
            for row in reader:
                rows_source += 1
                if len(row) != len(header):
                    proc.kill()
                    raise ValueError(
                        "Linha RAIS com largura divergente: "
                        f"linha={rows_source}, observado={len(row)}, esperado={len(header)}"
                    )
                if normalize_code(row[municipality_idx]) == municipality_code:
                    writer.writerow(row)
                    rows_selected += 1
    except Exception:
        proc.kill()
        proc.wait()
        raise

    stderr = proc.stderr.read().decode("utf-8", errors="replace")
    returncode = proc.wait()
    if returncode != 0:
        raise RuntimeError(
            f"Falha no streaming 7-Zip: returncode={returncode}; stderr={stderr[-2000:]}"
        )
    if expected_rows is not None and rows_selected != expected_rows:
        raise ValueError(
            "Quantidade de registros municipais divergente: "
            f"observado={rows_selected}, esperado={expected_rows}; parcial={partial}"
        )

    partial.replace(output)
    return RaisMunicipalityExtract(
        output_path=output,
        rows_source=rows_source,
        rows_selected=rows_selected,
        columns=len(header),
        size_bytes=output.stat().st_size,
        sha256=_sha256(output),
        reused_existing=False,
    )
