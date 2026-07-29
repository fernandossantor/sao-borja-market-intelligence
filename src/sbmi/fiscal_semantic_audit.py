"""Auditoria semântica e de sobreposição dos dados fiscais locais."""

from __future__ import annotations

import hashlib
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

import pandas as pd

FEDERAL_COLUMNS = [
    "mes_ano", "tipo", "tipo_de_favorecido", "uf", "nome_do_favorecido",
    "cpf_cnpj", "municipio", "funcao", "programa_orcamentario",
    "acao_orcamentaria", "linguagem_cidada", "valor_transferido",
]
MONTHS = {
    "jan": 1, "fev": 2, "mar": 3, "abr": 4, "mai": 5, "jun": 6,
    "jul": 7, "ago": 8, "set": 9, "out": 10, "nov": 11, "dez": 12,
}
EXPECTED_DATASETS = {
    "federal_transferencias", "estadual_icms", "estadual_transferencias",
    "municipal_despesas_instituicao", "municipal_despesas_elemento",
    "municipal_receita_elemento",
}


@dataclass(frozen=True)
class FiscalSemanticAuditResult:
    contracts: pd.DataFrame
    overlap_by_year: pd.DataFrame
    overlap_by_source: pd.DataFrame
    historical_duplicates: pd.DataFrame
    issues: pd.DataFrame
    summary: pd.DataFrame
    inputs: tuple[Path, ...]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _date_key(value: object) -> str:
    text = str(value).strip().lower()
    if "/" in text and text.split("/", 1)[0][:3] in MONTHS:
        month, year = text.split("/", 1)
        return f"{2000 + int(year):04d}-{MONTHS[month[:3]]:02d}-01"
    return pd.Timestamp(value).strftime("%Y-%m-%d")


def _row_key(row: pd.Series) -> tuple[str, ...]:
    values = [_date_key(row["mes_ano"])]
    values.extend(str(row[column]).strip() for column in FEDERAL_COLUMNS[1:-1])
    values.append(str(Decimal(str(row["valor_transferido"])).quantize(Decimal("0.01"))))
    return tuple(values)


def _require_columns(frame: pd.DataFrame, required: set[str], dataset: str) -> None:
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Contrato divergente em {dataset}: {sorted(missing)}")


def _contract_rows(datasets: dict[str, pd.DataFrame]) -> pd.DataFrame:
    records = []
    for name in sorted(datasets):
        frame = datasets[name]
        if name == "federal_transferencias":
            status, blocker = "PARTIAL_OVERLAP", "SOURCE_AUTHORITY_NOT_ESTABLISHED"
        elif name == "estadual_icms":
            flagged = int(frame["_duplicate_group_id"].notna().sum())
            status = "BLOCKED"
            blocker = "PENDING_SOURCE_DUPLICATE_VALIDATION" if flagged else "SEMANTIC_REVIEW"
        elif name == "estadual_transferencias":
            status, blocker = "BLOCKED", "EXPENDITURE_PHASE_SEPARATION_REQUIRED"
        else:
            status, blocker = "BLOCKED", "REFERENCE_PERIOD_AND_UNIT_NOT_PROVEN"
        date_column = "mes_ano" if "mes_ano" in frame else "data" if "data" in frame else None
        records.append({
            "dataset": name,
            "rows_observed": len(frame),
            "columns_observed": len(frame.columns),
            "date_min": frame[date_column].min() if date_column else "",
            "date_max": frame[date_column].max() if date_column else "",
            "semantic_status": status,
            "promotion_blocker": blocker,
            "unit_status": "NOT_PROVEN",
            "nature": "observed_and_calculated",
        })
    return pd.DataFrame(records)


def audit_fiscal_semantics(staging_root: Path, historical_root: Path) -> FiscalSemanticAuditResult:
    """Compara contratos fiscais sem promover ou modificar dados."""
    staging_root = staging_root.expanduser().resolve()
    historical_root = historical_root.expanduser().resolve()
    datasets = {}
    staging_files = []
    for name in sorted(EXPECTED_DATASETS):
        path = staging_root / f"{name}.parquet"
        if not path.is_file():
            raise FileNotFoundError(f"Staging ausente: {path}")
        datasets[name] = pd.read_parquet(path)
        staging_files.append(path)
    federal = datasets["federal_transferencias"]
    _require_columns(federal, set(FEDERAL_COLUMNS) | {"_source_file"}, "federal")

    historical_files = sorted(historical_root.glob("*.parquet"))
    if not historical_files:
        raise FileNotFoundError(f"Parquets históricos ausentes: {historical_root}")
    historical_frames = []
    for path in historical_files:
        frame = pd.read_parquet(path)
        _require_columns(frame, set(FEDERAL_COLUMNS), path.name)
        frame["_historical_file"] = path.name
        historical_frames.append(frame)
    historical = pd.concat(historical_frames, ignore_index=True)

    current_counter = Counter(_row_key(row) for _, row in federal.iterrows())
    historical_counter = Counter(_row_key(row) for _, row in historical.iterrows())
    owners: dict[tuple[str, ...], set[str]] = defaultdict(set)
    for _, row in historical.iterrows():
        owners[_row_key(row)].add(str(row["_historical_file"]))

    year_rows = []
    for year in sorted({int(key[0][:4]) for key in current_counter}):
        current_year = Counter({
            key: count for key, count in current_counter.items()
            if int(key[0][:4]) == year
        })
        matched = sum((current_year & historical_counter).values())
        year_rows.append({
            "year": year,
            "staging_only_rows": sum(current_year.values()) - matched,
            "overlap_rows": matched,
        })
    overlap_by_year = pd.DataFrame(year_rows)
    overlap_by_year["classification"] = overlap_by_year.apply(
        lambda row: (
            "UNIQUE" if row["overlap_rows"] == 0
            else "CONTENT_DUPLICATE" if row["staging_only_rows"] == 0
            else "PARTIAL_OVERLAP"
        ), axis=1)
    overlap_by_year["nature"] = "calculated"

    source_rows = []
    for source, group in federal.groupby("_source_file", sort=True):
        group_counter = Counter(_row_key(row) for _, row in group.iterrows())
        matched = sum((group_counter & historical_counter).values())
        source_rows.append({
            "source_file": source,
            "rows_observed": len(group),
            "overlap_rows": matched,
            "staging_only_rows": len(group) - matched,
            "classification": (
                "CONTENT_DUPLICATE" if matched == len(group)
                else "UNIQUE" if matched == 0 else "PARTIAL_OVERLAP"
            ),
            "historical_files": "|".join(sorted({
                owner for key in group_counter for owner in owners.get(key, set())
            })),
            "nature": "calculated",
        })
    overlap_by_source = pd.DataFrame(source_rows)

    duplicate_rows = []
    for key, count in historical_counter.items():
        if count > 1:
            duplicate_rows.append({
                "reference_period": key[0],
                "action": key[9],
                "value": key[-1],
                "occurrences": count,
                "excess_occurrences": count - 1,
                "historical_files": "|".join(sorted(owners[key])),
                "classification": "CONTENT_DUPLICATE",
                "nature": "calculated",
            })
    historical_duplicates = pd.DataFrame(duplicate_rows)

    issues = []
    icms = datasets["estadual_icms"]
    non_icms = icms.loc[~icms["descricao"].astype(str).str.upper().eq("ICMS")]
    if len(non_icms):
        issues.append({
            "dataset": "estadual_icms",
            "source_file": "",
            "issue_class": "DATASET_NAME_CONTENT_MISMATCH",
            "affected_rows": len(non_icms),
            "decision": "REVIEW_CONTRACT_NAME_BEFORE_CURATED",
            "nature": "observed_and_calculated",
        })
    suspicious = federal.loc[
        federal["_source_file"].eq(
            "ATENCAO A SAUDE DA POPULACAO PARA PROCEDIMENTOS EM MEDIA E ALTA COMPLEXIDADE.xlsx"
        )
    ]
    if len(suspicious) and suspicious["acao_orcamentaria"].str.contains("FPM", na=False).all():
        issues.append({
            "dataset": "federal_transferencias",
            "source_file": suspicious.iloc[0]["_source_file"],
            "issue_class": "FILE_NAME_CONTENT_MISMATCH",
            "affected_rows": len(suspicious),
            "decision": "DO_NOT_CLASSIFY_FROM_FILENAME",
            "nature": "observed_and_calculated",
        })
    issues_frame = pd.DataFrame(issues, columns=[
        "dataset", "source_file", "issue_class", "affected_rows", "decision", "nature",
    ])

    overlap = sum((current_counter & historical_counter).values())
    summary = pd.DataFrame([
        ("staging_rows", sum(len(frame) for frame in datasets.values()), "observed"),
        ("federal_staging_rows", len(federal), "observed"),
        ("historical_federal_rows", len(historical), "observed"),
        ("federal_overlap_rows", overlap, "calculated"),
        ("federal_staging_only_rows", len(federal) - overlap, "calculated"),
        ("historical_only_rows", len(historical) - overlap, "calculated"),
        ("historical_duplicate_excess", sum(max(v - 1, 0) for v in historical_counter.values()),
         "calculated"),
        ("promotion_allowed", 0, "recommended_decision"),
    ], columns=["indicator", "value", "nature"])
    return FiscalSemanticAuditResult(
        _contract_rows(datasets), overlap_by_year, overlap_by_source,
        historical_duplicates, issues_frame, summary,
        tuple(staging_files + historical_files),
    )


def write_fiscal_semantic_audit(result: FiscalSemanticAuditResult, output_dir: Path) -> Path:
    """Publica a auditoria atomicamente e recusa sobrescrita."""
    target = output_dir.expanduser().resolve()
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    partial.mkdir(parents=True, exist_ok=False)
    try:
        outputs = {
            "dataset_contract_review.csv": result.contracts,
            "federal_overlap_by_year.csv": result.overlap_by_year,
            "federal_overlap_by_source.csv": result.overlap_by_source,
            "historical_duplicate_groups.csv": result.historical_duplicates,
            "semantic_issues.csv": result.issues,
            "fiscal_semantic_summary.csv": result.summary,
        }
        for name, frame in outputs.items():
            frame.to_csv(partial / name, index=False)
        manifest = []
        for path in result.inputs:
            manifest.append(("input", str(path), path.stat().st_size, _sha256(path)))
        for path in sorted(partial.iterdir()):
            manifest.append(("output", path.name, path.stat().st_size, _sha256(path)))
        pd.DataFrame(manifest, columns=["role", "path", "bytes", "sha256"]).to_csv(
            partial / "fiscal_semantic_manifest.csv", index=False)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
