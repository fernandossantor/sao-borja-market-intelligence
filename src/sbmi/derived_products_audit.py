"""Auditoria estrutural e de utilidade dos produtos derivados existentes."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import duckdb
import pandas as pd
import pyarrow.parquet as pq

from sbmi.inbox_profile import normalize_label

GEO_TOKENS = {
    "municipio",
    "municipios",
    "cidade",
    "uf",
    "estado",
    "territorio",
    "localidade",
    "codmunicipio",
    "codigo_municipio",
    "nome_municipio",
    "geocodigo",
}
TIME_TOKENS = {
    "ano",
    "mes",
    "data",
    "periodo",
    "competencia",
    "referencia",
    "mes_ano",
    "data_referencia",
}
MEASURE_TOKENS = {
    "valor",
    "total",
    "quantidade",
    "qtd",
    "taxa",
    "indice",
    "percentual",
    "porcentagem",
    "pib",
    "remuneracao",
    "emprego",
    "saldo",
    "arrecadado",
    "pago",
    "liquidado",
    "empenhado",
    "populacao",
    "producao",
}
CATEGORY_TOKENS = {
    "categoria",
    "setor",
    "atividade",
    "cnae",
    "rubrica",
    "funcao",
    "subfuncao",
    "programa",
    "produto",
    "grupo",
    "classe",
    "tipo",
    "descricao",
}


@dataclass(frozen=True)
class DerivedProductsAuditResult:
    files: pd.DataFrame
    tables: pd.DataFrame
    families: pd.DataFrame
    exact_duplicates: pd.DataFrame
    summary: pd.DataFrame


def _extension(path: Path) -> str:
    name = path.name.lower()
    if name.endswith(".duckdb.wal"):
        return "duckdb.wal"
    return path.suffix.lower().lstrip(".")


def _family(relative_path: str) -> str:
    parts = PurePosixPath(relative_path).parts
    if not parts:
        return "(unknown)"
    if parts[0] == "processed" and len(parts) >= 3:
        return "/".join(parts[:2])
    return parts[0]


def _schema_signature(headers: list[str]) -> str:
    normalized = [normalize_label(header) for header in headers]
    payload = "|".join(normalized)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest() if payload else ""


def _signal(headers: list[str], tokens: set[str]) -> bool:
    normalized = {normalize_label(header) for header in headers if str(header).strip()}
    for header in normalized:
        if header in tokens:
            return True
        parts = set(header.split("_"))
        if parts & tokens:
            return True
    return False


def _table_record(
    *,
    relative_path: str,
    table_name: str,
    source_format: str,
    rows: int,
    headers: list[str],
    variable_width_rows: int = 0,
) -> dict[str, object]:
    geography = _signal(headers, GEO_TOKENS)
    temporal = _signal(headers, TIME_TOKENS)
    measure = _signal(headers, MEASURE_TOKENS)
    category = _signal(headers, CATEGORY_TOKENS)
    if rows <= 0:
        utility = "EMPTY"
    elif measure and (geography or temporal or category):
        utility = "ANALYTICAL_SIGNAL_PRESENT"
    else:
        utility = "STRUCTURED_REVIEW_REQUIRED"
    return {
        "relative_path": relative_path,
        "family": _family(relative_path),
        "table_name": table_name,
        "source_format": source_format,
        "rows_observed": int(rows),
        "columns_observed": len(headers),
        "headers": "|".join(str(header) for header in headers),
        "schema_signature_sha256": _schema_signature(headers),
        "geography_signal_estimate": geography,
        "time_signal_estimate": temporal,
        "measure_signal_estimate": measure,
        "category_signal_estimate": category,
        "utility_estimate": utility,
        "variable_width_rows": int(variable_width_rows),
    }


def _profile_parquet(path: Path, relative_path: str) -> list[dict[str, object]]:
    parquet = pq.ParquetFile(path)
    metadata = parquet.metadata
    headers = list(parquet.schema_arrow.names)
    rows = 0 if metadata is None else metadata.num_rows
    return [
        _table_record(
            relative_path=relative_path,
            table_name=path.stem,
            source_format="parquet",
            rows=rows,
            headers=headers,
        )
    ]


def _decode_text(path: Path) -> tuple[str, str]:
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("utf-8", raw, 0, 1, "Codificação não reconhecida")


def _profile_delimited(path: Path, relative_path: str) -> list[dict[str, object]]:
    text, _encoding = _decode_text(path)
    if not text.strip():
        return [
            _table_record(
                relative_path=relative_path,
                table_name=path.stem,
                source_format=_extension(path),
                rows=0,
                headers=[],
            )
        ]
    sample = text[:65536]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
    except csv.Error:
        dialect = csv.excel
    reader = csv.reader(text.splitlines(), dialect)
    rows = list(reader)
    headers = rows[0] if rows else []
    expected_width = len(headers)
    variable = sum(len(row) != expected_width for row in rows[1:])
    return [
        _table_record(
            relative_path=relative_path,
            table_name=path.stem,
            source_format=_extension(path),
            rows=max(len(rows) - 1, 0),
            headers=headers,
            variable_width_rows=variable,
        )
    ]


def _profile_json(path: Path, relative_path: str) -> list[dict[str, object]]:
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(payload, list):
        rows = len(payload)
        headers = sorted(
            {
                str(key)
                for item in payload
                if isinstance(item, dict)
                for key in item
            }
        )
    elif isinstance(payload, dict):
        rows = 1
        headers = [str(key) for key in payload]
    else:
        rows = 1
        headers = ["value"]
    return [
        _table_record(
            relative_path=relative_path,
            table_name=path.stem,
            source_format="json",
            rows=rows,
            headers=headers,
        )
    ]


def _quoted_identifier(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def _profile_duckdb(path: Path, relative_path: str) -> list[dict[str, object]]:
    connection = duckdb.connect(str(path), read_only=True)
    try:
        relations = connection.execute(
            """
            SELECT table_schema, table_name, table_type
            FROM information_schema.tables
            WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
            ORDER BY table_schema, table_name
            """
        ).fetchall()
        records: list[dict[str, object]] = []
        for schema_name, table_name, _table_type in relations:
            qualified = (
                f"{_quoted_identifier(str(schema_name))}."
                f"{_quoted_identifier(str(table_name))}"
            )
            rows = int(connection.execute(f"SELECT COUNT(*) FROM {qualified}").fetchone()[0])
            description = connection.execute(f"DESCRIBE SELECT * FROM {qualified}").fetchall()
            headers = [str(row[0]) for row in description]
            records.append(
                _table_record(
                    relative_path=relative_path,
                    table_name=f"{schema_name}.{table_name}",
                    source_format="duckdb",
                    rows=rows,
                    headers=headers,
                )
            )
        return records
    finally:
        connection.close()


def _profile_file(path: Path, relative_path: str) -> tuple[dict[str, object], list[dict[str, object]]]:
    extension = _extension(path)
    file_record: dict[str, object] = {
        "relative_path": relative_path,
        "family": _family(relative_path),
        "extension": extension,
        "size_bytes": path.stat().st_size,
        "read_status": "OK",
        "error_type": "",
        "error_message": "",
        "tables_observed": 0,
        "rows_observed": 0,
    }
    if extension == "duckdb.wal":
        file_record["read_status"] = "AUXILIARY"
        return file_record, []

    try:
        if extension == "parquet":
            tables = _profile_parquet(path, relative_path)
        elif extension in {"csv", "tsv", "txt"}:
            tables = _profile_delimited(path, relative_path)
        elif extension in {"json", "jsonl"}:
            tables = _profile_json(path, relative_path)
        elif extension == "duckdb":
            tables = _profile_duckdb(path, relative_path)
        else:
            file_record["read_status"] = "UNSUPPORTED"
            return file_record, []
        file_record["tables_observed"] = len(tables)
        file_record["rows_observed"] = sum(int(row["rows_observed"]) for row in tables)
        if not tables or int(file_record["rows_observed"]) == 0:
            file_record["read_status"] = "EMPTY"
        return file_record, tables
    except Exception as exc:
        file_record["read_status"] = "ERROR"
        file_record["error_type"] = type(exc).__name__
        file_record["error_message"] = str(exc)
        return file_record, []


def _exact_duplicates(manifest: pd.DataFrame) -> pd.DataFrame:
    frame = manifest.copy()
    frame["local_sha256"] = frame["local_sha256"].fillna("").astype(str)
    duplicated = frame.loc[
        frame["local_sha256"].ne("")
        & frame["local_sha256"].duplicated(keep=False)
    ].copy()
    columns = [
        "duplicate_group",
        "local_sha256",
        "relative_path",
        "scope",
        "downloaded_size_bytes",
    ]
    if duplicated.empty:
        return pd.DataFrame(columns=columns)
    groups = {
        value: index
        for index, value in enumerate(
            sorted(duplicated["local_sha256"].unique()),
            start=1,
        )
    }
    duplicated["duplicate_group"] = duplicated["local_sha256"].map(groups)
    return duplicated[columns].sort_values(["duplicate_group", "relative_path"])


def _family_summary(files: pd.DataFrame, tables: pd.DataFrame) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    for family, file_group in files.groupby("family", sort=True):
        table_group = tables.loc[tables["family"].eq(family)] if not tables.empty else tables
        errors = int(file_group["read_status"].eq("ERROR").sum())
        empty = int(file_group["read_status"].eq("EMPTY").sum())
        if errors:
            status = "ERROR"
        elif empty:
            status = "REVIEW_EMPTY"
        else:
            status = "OK"
        records.append(
            {
                "family": family,
                "files": len(file_group),
                "known_bytes": int(file_group["size_bytes"].sum()),
                "readable_files": int(file_group["read_status"].isin({"OK", "EMPTY"}).sum()),
                "auxiliary_files": int(file_group["read_status"].eq("AUXILIARY").sum()),
                "unsupported_files": int(file_group["read_status"].eq("UNSUPPORTED").sum()),
                "error_files": errors,
                "empty_files": empty,
                "tables": len(table_group),
                "rows_observed": int(table_group["rows_observed"].sum()) if not table_group.empty else 0,
                "unique_schemas": int(table_group["schema_signature_sha256"].nunique())
                if not table_group.empty
                else 0,
                "analytical_signal_tables": int(
                    table_group["utility_estimate"].eq("ANALYTICAL_SIGNAL_PRESENT").sum()
                )
                if not table_group.empty
                else 0,
                "family_status": status,
            }
        )
    return pd.DataFrame(records)


def audit_derived_products_snapshot(snapshot_path: Path) -> DerivedProductsAuditResult:
    """Lê produtos existentes; não os reconstrói nem os compara ao bruto."""
    root = snapshot_path.expanduser().resolve()
    manifest_path = root / "snapshot_manifest.csv"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Manifesto da captura não encontrado: {manifest_path}")
    manifest = pd.read_csv(manifest_path)
    required = {"relative_path", "scope", "local_sha256", "downloaded_size_bytes"}
    missing = required.difference(manifest.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes no manifesto: {sorted(missing)}")

    file_records: list[dict[str, object]] = []
    table_records: list[dict[str, object]] = []
    for row in manifest.sort_values("relative_path").itertuples(index=False):
        relative_path = str(row.relative_path)
        local_path = root / Path(*PurePosixPath(relative_path).parts)
        if not local_path.is_file():
            file_records.append(
                {
                    "relative_path": relative_path,
                    "family": _family(relative_path),
                    "extension": _extension(local_path),
                    "size_bytes": 0,
                    "read_status": "ERROR",
                    "error_type": "FileNotFoundError",
                    "error_message": "Arquivo ausente na captura local.",
                    "tables_observed": 0,
                    "rows_observed": 0,
                }
            )
            continue
        file_record, tables = _profile_file(local_path, relative_path)
        file_records.append(file_record)
        table_records.extend(tables)

    files = pd.DataFrame(file_records)
    tables = pd.DataFrame(table_records)
    if tables.empty:
        tables = pd.DataFrame(
            columns=[
                "relative_path",
                "family",
                "table_name",
                "source_format",
                "rows_observed",
                "columns_observed",
                "headers",
                "schema_signature_sha256",
                "geography_signal_estimate",
                "time_signal_estimate",
                "measure_signal_estimate",
                "category_signal_estimate",
                "utility_estimate",
                "variable_width_rows",
            ]
        )
    duplicates = _exact_duplicates(manifest)
    families = _family_summary(files, tables)
    indicators = [
        ("snapshot_files", len(manifest), "observed"),
        ("files_profiled", len(files), "observed"),
        ("files_ok", int(files["read_status"].eq("OK").sum()), "calculated"),
        ("files_empty", int(files["read_status"].eq("EMPTY").sum()), "calculated"),
        ("files_error", int(files["read_status"].eq("ERROR").sum()), "calculated"),
        (
            "files_unsupported",
            int(files["read_status"].eq("UNSUPPORTED").sum()),
            "calculated",
        ),
        (
            "files_auxiliary",
            int(files["read_status"].eq("AUXILIARY").sum()),
            "calculated",
        ),
        ("tables_observed", len(tables), "calculated"),
        ("rows_observed", int(tables["rows_observed"].sum()), "calculated"),
        ("families_observed", len(families), "calculated"),
        (
            "analytical_signal_tables",
            int(tables["utility_estimate"].eq("ANALYTICAL_SIGNAL_PRESENT").sum()),
            "estimated",
        ),
        (
            "structured_review_tables",
            int(tables["utility_estimate"].eq("STRUCTURED_REVIEW_REQUIRED").sum()),
            "estimated",
        ),
        (
            "exact_duplicate_groups",
            int(duplicates["duplicate_group"].nunique()) if not duplicates.empty else 0,
            "calculated",
        ),
        (
            "exact_duplicate_rows",
            len(duplicates),
            "calculated",
        ),
    ]
    summary = pd.DataFrame(indicators, columns=["indicator", "value", "nature"])
    return DerivedProductsAuditResult(
        files=files,
        tables=tables,
        families=families,
        exact_duplicates=duplicates,
        summary=summary,
    )


def write_derived_products_audit(
    result: DerivedProductsAuditResult,
    output_dir: Path,
    *,
    replace: bool = False,
) -> Path:
    """Publica relatórios locais de modo atômico."""
    target = output_dir.expanduser().resolve()
    if target.exists():
        if not replace:
            raise FileExistsError(f"Destino da auditoria já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    try:
        result.files.to_csv(partial / "derived_file_profile.csv", index=False)
        result.tables.to_csv(partial / "derived_table_profile.csv", index=False)
        result.families.to_csv(partial / "derived_family_summary.csv", index=False)
        result.exact_duplicates.to_csv(partial / "derived_exact_duplicates.csv", index=False)
        result.summary.to_csv(partial / "derived_products_audit_summary.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.rename(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
