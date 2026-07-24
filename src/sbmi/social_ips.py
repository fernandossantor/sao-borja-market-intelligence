"""Builder portátil dos scorecards publicados do IPS Brasil para São Borja."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import unicodedata
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path

import pandas as pd

from sbmi.ips_web_snapshot import SUMMARY_LABELS, visible_text

DEFAULT_IBGE_CODE = "4318002"
DEFAULT_MUNICIPALITY = "São Borja"
DEFAULT_YEARS = (2024, 2025, 2026)
INDEX_LABEL = "Índice de Progresso Social"
DIMENSION_LABELS = {
    "necessidades humanas basicas",
    "fundamentos do bem estar",
    "oportunidades",
}
COMPONENT_LABELS = {
    "nutricao e cuidados medicos basicos",
    "agua e saneamento",
    "moradia",
    "seguranca pessoal",
    "acesso ao conhecimento basico",
    "acesso a informacao e comunicacao",
    "saude e bem estar",
    "qualidade do meio ambiente",
    "direitos individuais",
    "liberdades individuais e de escolha",
    "inclusao social",
    "acesso a educacao superior",
}


@dataclass(frozen=True)
class IpsPublishedResult:
    """Produtos derivados dos scorecards publicados."""

    published_summary_long: pd.DataFrame
    summary_2026: pd.DataFrame
    metadata: dict[str, object]


def normalize_label(value: object) -> str:
    """Normaliza rótulos apenas para integração técnica."""
    text = unicodedata.normalize("NFKD", str(value))
    text = "".join(character for character in text if not unicodedata.combining(character))
    text = text.lower().replace("²", "2")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_published_number(value: object) -> str | None:
    """Converte a representação brasileira para decimal canônico textual."""
    text = str(value).strip().replace("\xa0", " ")
    text = text.replace("%", "").replace("R$", "").replace(" ", "")
    if text.lower() in {"", "-", "--", "n/a", "na", "null"}:
        return None
    if "," in text:
        canonical = text.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"-?\d{1,3}(\.\d{3})+", text):
        canonical = text.replace(".", "")
    else:
        canonical = text
    try:
        number = Decimal(canonical)
    except InvalidOperation:
        return None
    return format(number, "f")


def indicator_level(label: str) -> str:
    """Classifica índice, dimensões e componentes do scorecard."""
    normalized = normalize_label(label)
    if normalized == normalize_label(INDEX_LABEL):
        return "index"
    if normalized in DIMENSION_LABELS:
        return "dimension"
    if normalized in COMPONENT_LABELS:
        return "component"
    raise ValueError(f"Rótulo agregado inesperado: {label!r}")


def _decimal_pattern() -> re.Pattern[str]:
    return re.compile(r"(?<!\d)(\d{1,3}[,.]\d{1,3})(?!\d)")


def _extract_index_score(text: str, year: int) -> str:
    match = re.search(
        rf"IPS\s+BRASIL\s+{year}\b.*?(\d{{1,3}}[,.]\d{{1,3}})\s*/\s*100",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if match is None:
        raise ValueError(f"Pontuação geral do IPS não encontrada no scorecard de {year}.")
    return match.group(1)


def _extract_label_score(text: str, label: str, next_labels: tuple[str, ...]) -> str:
    folded = text.casefold()
    start = folded.find(label.casefold())
    if start < 0:
        raise ValueError(f"Rótulo ausente no scorecard: {label!r}")
    segment_start = start + len(label)
    boundaries = [
        folded.find(candidate.casefold(), segment_start)
        for candidate in next_labels
        if folded.find(candidate.casefold(), segment_start) >= 0
    ]
    segment_end = min(boundaries) if boundaries else min(segment_start + 8000, len(text))
    segment = text[segment_start:segment_end]
    match = _decimal_pattern().search(segment)
    if match is None:
        raise ValueError(f"Pontuação não encontrada após o rótulo {label!r}.")
    return match.group(1)


def extract_scorecard_summary(
    html_text: str,
    *,
    year: int,
    ibge_code: str,
    municipality: str,
    source_url: str,
    source_sha256: str,
) -> pd.DataFrame:
    """Extrai índice, três dimensões e doze componentes do scorecard."""
    text = visible_text(html_text)
    if municipality.casefold() not in text.casefold():
        raise ValueError(f"Município inesperado no scorecard de {year}.")
    if ibge_code not in html_text:
        raise ValueError(f"Código IBGE ausente no scorecard de {year}.")

    labels = (INDEX_LABEL, *SUMMARY_LABELS)
    values: list[str] = [_extract_index_score(text, year)]
    for index, label in enumerate(SUMMARY_LABELS):
        values.append(_extract_label_score(text, label, SUMMARY_LABELS[index + 1 :]))

    records: list[dict[str, object]] = []
    for order, (label, value_text) in enumerate(zip(labels, values, strict=True), start=1):
        records.append(
            {
                "reference_year": year,
                "edition_type": "published_original",
                "comparability_status": "NOT_STRICTLY_COMPARABLE_ACROSS_EDITIONS",
                "ibge_code": ibge_code,
                "municipality_observed": municipality,
                "indicator_order": order,
                "indicator_label": label,
                "indicator_key": normalize_label(label).replace(" ", "_"),
                "indicator_level": indicator_level(label),
                "value_text": value_text,
                "value_numeric": parse_published_number(value_text),
                "unit": "score_0_100",
                "nature": "observed",
                "source_url": source_url,
                "source_sha256": source_sha256,
            }
        )
    return pd.DataFrame(records)


def _manifest(snapshot_path: Path) -> pd.DataFrame:
    path = snapshot_path / "web_manifest.csv"
    if not path.is_file():
        raise FileNotFoundError(f"Manifesto web não encontrado: {path}")
    frame = pd.read_csv(path)
    required = {
        "reference_year",
        "requested_url",
        "sha256",
        "ibge_code",
        "local_file",
    }
    missing = sorted(required.difference(frame.columns))
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes no manifesto: {missing}")
    return frame


def build_published_ips(
    snapshot_path: Path,
    *,
    ibge_code: str = DEFAULT_IBGE_CODE,
    municipality: str = DEFAULT_MUNICIPALITY,
    expected_years: tuple[int, ...] = DEFAULT_YEARS,
) -> IpsPublishedResult:
    """Constrói agregados anuais sem calcular variação entre edições."""
    root = snapshot_path.expanduser().resolve()
    manifest = _manifest(root)
    years = tuple(sorted(int(value) for value in manifest["reference_year"].tolist()))
    if years != tuple(sorted(expected_years)):
        raise ValueError(f"Anos inesperados no manifesto: observados={years}")

    summaries: list[pd.DataFrame] = []
    source_rows: list[dict[str, object]] = []
    for record in manifest.sort_values("reference_year").to_dict("records"):
        year = int(record["reference_year"])
        local_path = root / str(record["local_file"])
        content = local_path.read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        if digest != str(record["sha256"]):
            raise ValueError(f"SHA-256 divergente na captura de {year}.")
        summary = extract_scorecard_summary(
            content.decode("utf-8"),
            year=year,
            ibge_code=ibge_code,
            municipality=municipality,
            source_url=str(record["requested_url"]),
            source_sha256=digest,
        )
        if len(summary) != 16:
            raise ValueError(f"Agregados inesperados em {year}: observados={len(summary)}")
        summaries.append(summary)
        source_rows.append(
            {
                "reference_year": year,
                "source_url": str(record["requested_url"]),
                "source_sha256": digest,
                "summary_scores_observed": len(summary),
            }
        )

    published = pd.concat(summaries, ignore_index=True)
    summary_2026 = published.loc[published["reference_year"].eq(2026)].reset_index(drop=True)
    metadata: dict[str, object] = {
        "dataset": "IPS Brasil — scorecards das edições originalmente publicadas",
        "municipality": municipality,
        "ibge_code": ibge_code,
        "geographic_scope": "municipality",
        "reference_years": list(years),
        "edition_type": "published_original",
        "published_summary_rows_observed": len(published),
        "summary_2026_rows_observed": len(summary_2026),
        "sources": source_rows,
        "data_nature": "observed",
        "unit": "score_0_100",
        "comparability_status": "NOT_STRICTLY_COMPARABLE_ACROSS_EDITIONS",
        "temporal_change_calculated": False,
        "individual_indicator_values_status": "NOT_PUBLISHED_AS_NUMERIC_VALUES_IN_SCORECARD_HTML",
        "harmonized_series_status": "NOT_INCLUDED_REQUIRES_LIVEVIEW_EVENT",
        "limitations": [
            "Os anos preservam as edições originalmente publicadas.",
            "Não são calculadas variações entre edições metodologicamente não comparáveis.",
            "O produto contém somente o índice, três dimensões e doze componentes.",
            "Os indicadores individuais aparecem por nome, sem valores numéricos no HTML.",
            "A série harmonizada 2024–2026 será construída em módulo separado.",
        ],
    }
    return IpsPublishedResult(
        published_summary_long=published,
        summary_2026=summary_2026,
        metadata=metadata,
    )


def write_published_ips(
    result: IpsPublishedResult,
    output_dir: Path,
    *,
    replace: bool = False,
) -> Path:
    """Publica produtos localmente e de modo atômico."""
    target = output_dir.expanduser().resolve()
    if target.exists():
        if not replace:
            raise FileExistsError(f"Destino já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    try:
        result.published_summary_long.to_csv(
            partial / "ips_published_summary_2024_2026.csv",
            index=False,
        )
        result.summary_2026.to_csv(partial / "ips_2026_summary.csv", index=False)
        (partial / "ips_metadata.json").write_text(
            json.dumps(result.metadata, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.rename(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
