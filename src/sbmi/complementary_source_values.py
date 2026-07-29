"""Coleta auditável de valores das quatro fontes complementares autorizadas."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import shutil
import unicodedata
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd

MUNICIPALITY_CODE = "4318002"
MUNICIPALITY_CODE_SIX = "431800"
YEAR_MIN = 1996
YEAR_MAX = 2026
ALLOWED_HOSTS = {
    "servicodados.ibge.gov.br",
    "apiv2-observatorio.sebrae.com.br",
    "ipsbrasil.org.br",
}

CENSO_INDICATOR_GROUPS = (
    "102705|102982|105286|105307",
    "107335|107457",
    "282208|282892|282920",
    "286565",
    "288711|288712",
    "288903|288904|288905|288906",
    "289207|289213|289219|289232|289233|289234",
    "289422|289502",
    "291926|291947|291968|291989|292010|292031|292052|292073|292094",
    "293436|293437|293438|293439|293440|293441|293442|293443|293444|"
    "293445|293446|293447|293448|293449",
    "96385",
    "96386",
    "96414",
    "96486",
    "96544|96545|96546",
    "97469|97470",
    "97512|97513|97527|97528|97545|97546|97563|97564|97581|97582|"
    "97599|97600|97617|97618|97635|97636|97653|97654|97671|97672|"
    "97689|97690|97707|97708|97725|97726|97743|97744|97761|97762|"
    "97779|97780|97797|97798|97815|97816|97833|97834|97851|97852|"
    "97869|97870",
    "97967|97971|97975|97979|97983",
)

CIDADES_INDICATORS = (
    "29169|29170|96385|29171|96486|96544|96386|143558|143514|60037|"
    "60045|78187|78192|5908|5903|5913|5929|5934|5950|5955|47001|"
    "329756|28141|60048|29749|30279|60032|28242|95335|60030|60029|"
    "60031|93371|77861|82270|29167|87529|87530|91245|91247|91249|91251"
)

IPS_EDITIONS = {
    2024: "c905fb0f-02ee-4ae8-b13f-a9d798d450d4",
    2025: "3b719d23-21a1-4330-8f1c-858c17dc22e7",
    2026: "8723347c-668a-4ab0-9af8-4b180315bdd8",
}

SOURCE_META = {
    "ibge_censo_2022_panorama": ("IBGE", "IBGE"),
    "ibge_cidades_panorama": ("IBGE", "IBGE"),
    "sebrae_observatorio_profile": ("Sebrae/Datawheel", "Fonte primária por cubo"),
    "ips_brasil_explorer": ("IPS Brasil", "IPS Brasil"),
}


@dataclass(frozen=True)
class CollectionResult:
    manifest: pd.DataFrame
    values: pd.DataFrame
    validation: pd.DataFrame
    snapshot_path: Path
    staging_path: Path
    curated_path: Path
    export_path: Path
    audit_path: Path


def _simple_identifier(value: str) -> None:
    if not value or Path(value).name != value:
        raise ValueError("execution_id deve ser um identificador simples")


def _targets(root: Path, execution_id: str) -> tuple[Path, Path]:
    target = root.resolve() / execution_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    return target, partial


def _validate_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS:
        raise ValueError(f"URL fora do escopo autorizado: {url}")


def _query_plan(sebrae_plan_path: Path) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for number, group in enumerate(CENSO_INDICATOR_GROUPS, start=1):
        rows.append({
            "source_id": "ibge_censo_2022_panorama",
            "query_id": f"censo_2022_{number:02d}",
            "dimension": "transversal_multitematico",
            "reference_period": "2022",
            "url": (
                "https://servicodados.ibge.gov.br/api/v1/pesquisas/-/indicadores/"
                f"{group}/resultados/{MUNICIPALITY_CODE}"
            ),
            "content_kind": "json",
            "declared_author": "IBGE",
        })
    rows.append({
        "source_id": "ibge_cidades_panorama",
        "query_id": "ibge_cidades_panorama_values",
        "dimension": "transversal_multitematico",
        "reference_period": "1996-2026_available",
        "url": (
            "https://servicodados.ibge.gov.br/api/v1/pesquisas/indicadores/"
            f"{CIDADES_INDICATORS}/resultados/{MUNICIPALITY_CODE_SIX}"
        ),
        "content_kind": "json",
        "declared_author": "IBGE",
    })
    plan = pd.read_csv(sebrae_plan_path, dtype=str)
    required = {
        "query_id", "dimension", "query_url", "execution_status",
        "primary_source_declared",
    }
    if not required.issubset(plan.columns) or plan.empty:
        raise ValueError("Plano Sebrae ausente ou inválido")
    if set(plan.execution_status) != {"PREPARED_NOT_EXECUTED"}:
        raise ValueError("Plano Sebrae não está no estado autorizado")
    for row in plan.itertuples(index=False):
        rows.append({
            "source_id": "sebrae_observatorio_profile",
            "query_id": row.query_id,
            "dimension": row.dimension,
            "reference_period": "1996-2026_available",
            "url": row.query_url,
            "content_kind": "json",
            "declared_author": row.primary_source_declared,
        })
    for year, edition_id in IPS_EDITIONS.items():
        rows.append({
            "source_id": "ips_brasil_explorer",
            "query_id": f"ips_brasil_{year}",
            "dimension": "saude_condicoes_sociais",
            "reference_period": str(year),
            "url": (
                "https://ipsbrasil.org.br/explore/data/export"
                f"?edition_id={edition_id}"
            ),
            "content_kind": "csv",
            "declared_author": "IPS Brasil",
        })
    result = pd.DataFrame(rows)
    if result.query_id.duplicated().any():
        raise ValueError("Plano contém query_id duplicado")
    for url in result.url:
        _validate_url(str(url))
    return result


def _fetch(session, row, timeout: float, per_response_limit: int) -> tuple[bytes, dict]:
    response = session.get(
        row.url,
        timeout=timeout,
        headers={
            "Accept": "application/json,text/csv,*/*;q=0.1",
            "User-Agent": "sbmi-complementary-source-values/1.0",
        },
    )
    response.raise_for_status()
    content = bytes(response.content)
    if not content or len(content) > per_response_limit:
        raise ValueError(f"Resposta vazia ou acima do limite: {row.query_id}")
    final_url = str(getattr(response, "url", row.url))
    _validate_url(final_url)
    content_type = str(response.headers.get("Content-Type", ""))
    if row.content_kind == "json":
        json.loads(content)
    elif "html" in content_type.lower():
        raise ValueError(f"CSV retornou HTML: {row.query_id}")
    extension = "json" if row.content_kind == "json" else "csv"
    institution, _ = SOURCE_META[row.source_id]
    return content, {
        "source_id": row.source_id,
        "query_id": row.query_id,
        "institution": institution,
        "declared_author": row.declared_author,
        "requested_url": row.url,
        "final_url": final_url,
        "obtained_at_utc": datetime.now(UTC).isoformat(),
        "publication_date": "",
        "reference_period": row.reference_period,
        "municipality_code": MUNICIPALITY_CODE,
        "status_code": int(response.status_code),
        "content_type": content_type,
        "bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
        "raw_file": f"{row.query_id}.{extension}",
        "dimension": row.dimension,
        "nature": "observed",
    }


def _numeric(value: object) -> float | None:
    if value is None or str(value).strip() in {"", "-", "..", "...", "X"}:
        return None
    text = str(value).strip().replace(".", "").replace(",", ".")
    try:
        return float(text)
    except ValueError:
        return None


def _ibge_values(content: bytes, metadata: dict) -> list[dict]:
    payload = json.loads(content)
    output = []
    for indicator in payload:
        indicator_id = str(indicator.get("id", ""))
        for result in indicator.get("res", []):
            locality = str(result.get("localidade", ""))
            if locality not in {MUNICIPALITY_CODE, MUNICIPALITY_CODE_SIX}:
                raise ValueError(f"Localidade IBGE divergente: {locality}")
            notes = result.get("notas", {}) or {}
            for period, raw_value in (result.get("res", {}) or {}).items():
                if not str(period).isdigit():
                    continue
                year = int(period)
                if not YEAR_MIN <= year <= YEAR_MAX:
                    continue
                output.append({
                    **metadata,
                    "reference_year": year,
                    "indicator_id": indicator_id,
                    "field_name": indicator_id,
                    "raw_value": raw_value,
                    "numeric_value": _numeric(raw_value),
                    "value_status": (
                        "OBSERVED_NUMERIC"
                        if _numeric(raw_value) is not None
                        else "MISSING_OR_NON_NUMERIC"
                    ),
                    "source_note": notes.get(str(period)),
                })
    return output


def _sebrae_values(content: bytes, metadata: dict) -> list[dict]:
    payload = json.loads(content)
    rows = payload.get("data", []) if isinstance(payload, dict) else []
    output = []
    for row_number, row in enumerate(rows, start=1):
        year_value = row.get("Year")
        year = int(year_value) if str(year_value).isdigit() else None
        if year is not None and not YEAR_MIN <= year <= YEAR_MAX:
            continue
        for field, raw_value in row.items():
            output.append({
                **metadata,
                "reference_year": year,
                "indicator_id": "",
                "field_name": field,
                "raw_value": raw_value,
                "numeric_value": _numeric(raw_value),
                "value_status": (
                    "OBSERVED_NUMERIC"
                    if _numeric(raw_value) is not None
                    else "OBSERVED_TEXT_OR_MISSING"
                ),
                "source_note": f"source_row={row_number}",
            })
    return output


def _canonical_header(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value))
    return re.sub(r"[^a-z0-9]+", "_", text.encode("ascii", "ignore").decode().lower()).strip("_")


def _ips_values(content: bytes, metadata: dict) -> list[dict]:
    text = content.decode("utf-8-sig")
    dialect = csv.Sniffer().sniff(text[:20_000], delimiters=",;\t")
    frame = pd.read_csv(io.StringIO(text), sep=dialect.delimiter, dtype=str)
    canonical = {_canonical_header(column): column for column in frame.columns}
    code_column = canonical.get("codigo_ibge")
    if code_column is not None:
        selected = frame.loc[
            frame[code_column]
            .astype(str)
            .str.replace(r"\D", "", regex=True)
            .eq(MUNICIPALITY_CODE)
        ]
        filter_note = "filtered_by_codigo_ibge=4318002"
    else:
        municipality_column = canonical.get("municipio")
        uf_column = canonical.get("uf")
        if municipality_column is None or uf_column is None:
            raise ValueError("CSV IPS sem chaves territoriais reconhecidas")
        selected = frame.loc[
            frame[municipality_column].astype(str).str.strip().eq("São Borja")
            & frame[uf_column].astype(str).str.strip().eq("RS")
        ]
        filter_note = (
            "source_without_codigo_ibge;filtered_by_municipio=São Borja;uf=RS;"
            "canonical_code_assigned=4318002"
        )
    if len(selected) != 1:
        raise ValueError(f"CSV IPS deve conter uma linha de São Borja: {len(selected)}")
    year = int(metadata["reference_period"])
    output = []
    for field, raw_value in selected.iloc[0].items():
        output.append({
            **metadata,
            "reference_year": year,
            "indicator_id": "",
            "field_name": str(field),
            "raw_value": raw_value,
            "numeric_value": _numeric(raw_value),
            "value_status": (
                "OBSERVED_NUMERIC"
                if _numeric(raw_value) is not None
                else "OBSERVED_TEXT_OR_MISSING"
            ),
            "source_note": filter_note,
        })
    return output


def collect_complementary_source_values(
    session,
    *,
    sebrae_plan_path: Path,
    snapshot_root: Path,
    staging_root: Path,
    curated_root: Path,
    export_root: Path,
    audit_root: Path,
    execution_id: str,
    timeout_seconds: float = 45,
    max_response_bytes: int = 5_000_000,
    max_total_bytes: int = 20_000_000,
) -> CollectionResult:
    """Executa o plano e publica as cinco camadas apenas após validação."""
    _simple_identifier(execution_id)
    if timeout_seconds <= 0 or max_response_bytes <= 0 or max_total_bytes <= 0:
        raise ValueError("Timeout e limites devem ser positivos")
    plan = _query_plan(sebrae_plan_path)
    roots = (snapshot_root, staging_root, curated_root, export_root, audit_root)
    targets = [_targets(root, execution_id) for root in roots]
    fetched = []
    total_bytes = 0
    for row in plan.itertuples(index=False):
        content, metadata = _fetch(session, row, timeout_seconds, max_response_bytes)
        total_bytes += len(content)
        if total_bytes > max_total_bytes:
            raise ValueError("Coleta bloqueada pelo limite total de bytes")
        fetched.append((content, metadata))
    records = []
    for content, metadata in fetched:
        if metadata["source_id"].startswith("ibge_"):
            records.extend(_ibge_values(content, metadata))
        elif metadata["source_id"].startswith("sebrae_"):
            records.extend(_sebrae_values(content, metadata))
        else:
            records.extend(_ips_values(content, metadata))
    values = pd.DataFrame(records)
    if values.empty:
        raise ValueError("Nenhum valor normalizado")
    manifest = pd.DataFrame(metadata for _, metadata in fetched)
    source_counts = values.groupby("source_id").size()
    missing_sources = sorted(set(SOURCE_META).difference(source_counts.index))
    duplicate_key = [
        "source_id", "query_id", "reference_year", "indicator_id",
        "field_name", "source_note",
    ]
    duplicates = int(values.duplicated(duplicate_key).sum())
    validation = pd.DataFrame([
        ("sources_expected", len(SOURCE_META), "calculated", "PASS"),
        ("sources_observed", len(source_counts), "calculated",
         "PASS" if not missing_sources else "FAIL"),
        ("queries_executed", len(fetched), "observed", "PASS"),
        ("raw_bytes", total_bytes, "calculated", "PASS"),
        ("normalized_rows", len(values), "calculated", "PASS"),
        ("duplicate_keys", duplicates, "calculated",
         "PASS" if not duplicates else "FAIL"),
        ("minimum_year", int(values.reference_year.dropna().min()), "calculated", "PASS"),
        ("maximum_year", int(values.reference_year.dropna().max()), "calculated", "PASS"),
    ], columns=["indicator", "value", "nature", "status"])
    if missing_sources or duplicates:
        raise ValueError(
            f"Validação falhou: fontes_ausentes={missing_sources}, duplicatas={duplicates}"
        )
    for _, partial in targets:
        partial.mkdir(parents=True)
    try:
        snapshot_partial, staging_partial, curated_partial, export_partial, audit_partial = (
            item[1] for item in targets
        )
        for content, metadata in fetched:
            source_dir = snapshot_partial / metadata["source_id"]
            source_dir.mkdir(exist_ok=True)
            (source_dir / metadata["raw_file"]).write_bytes(content)
        manifest.to_csv(snapshot_partial / "manifest.csv", index=False)
        values.to_csv(staging_partial / "complementary_values_staging.csv", index=False)
        values.to_csv(curated_partial / "complementary_values.csv", index=False)
        values.to_csv(export_partial / "complementary_values.csv", index=False)
        manifest.to_csv(audit_partial / "source_manifest.csv", index=False)
        validation.to_csv(audit_partial / "validation.csv", index=False)
        plan.assign(execution_status="EXECUTED").to_csv(
            audit_partial / "executed_query_plan.csv", index=False
        )
        for target, partial in targets:
            target.parent.mkdir(parents=True, exist_ok=True)
            partial.replace(target)
    except Exception:
        for _, partial in targets:
            shutil.rmtree(partial, ignore_errors=True)
        raise
    return CollectionResult(manifest, values, validation, *(item[0] for item in targets))
