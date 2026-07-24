"""Builder portátil das edições publicadas do IPS Brasil para São Borja."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import unicodedata
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from html.parser import HTMLParser
from pathlib import Path

import pandas as pd

DEFAULT_IBGE_CODE = "4318002"
DEFAULT_MUNICIPALITY = "São Borja"
DEFAULT_YEARS = (2024, 2025, 2026)

INDEX_LABELS = {"indice de progresso social", "ips brasil"}
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
METADATA_LABELS = {
    "codigo ibge",
    "municipio",
    "uf",
    "area km2",
    "area km",
    "populacao 2025",
    "populacao",
    "pib per capita",
}


@dataclass(frozen=True)
class IpsPublishedResult:
    """Produtos derivados das páginas publicadas do IPS Brasil."""

    published_long: pd.DataFrame
    profile_2026: pd.DataFrame
    summary_2026: pd.DataFrame
    metadata: dict[str, object]


class _TableParser(HTMLParser):
    """Extrai tabelas HTML sem dependências externas."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tables: list[list[list[str]]] = []
        self._table: list[list[str]] | None = None
        self._row: list[str] | None = None
        self._cell_parts: list[str] | None = None
        self._table_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        if tag == "table":
            self._table_depth += 1
            if self._table_depth == 1:
                self._table = []
        elif self._table_depth == 1 and tag == "tr":
            self._row = []
        elif self._table_depth == 1 and tag in {"th", "td"}:
            self._cell_parts = []

    def handle_data(self, data: str) -> None:
        if self._cell_parts is not None:
            self._cell_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if self._table_depth == 1 and tag in {"th", "td"}:
            if self._row is not None and self._cell_parts is not None:
                value = re.sub(r"\s+", " ", " ".join(self._cell_parts)).strip()
                self._row.append(value)
            self._cell_parts = None
        elif self._table_depth == 1 and tag == "tr":
            if self._table is not None and self._row:
                self._table.append(self._row)
            self._row = None
        elif tag == "table" and self._table_depth:
            if self._table_depth == 1 and self._table is not None:
                self.tables.append(self._table)
                self._table = None
            self._table_depth -= 1


def normalize_label(value: object) -> str:
    """Normaliza rótulos apenas para comparação estrutural."""
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
    """Classifica o nível estrutural sem criar nomenclatura oficial nova."""
    normalized = normalize_label(label)
    if normalized in METADATA_LABELS:
        return "metadata"
    if normalized in INDEX_LABELS:
        return "index"
    if normalized in DIMENSION_LABELS:
        return "dimension"
    if normalized in COMPONENT_LABELS:
        return "component"
    return "indicator"


def _extract_code_table(html_text: str, ibge_code: str) -> tuple[list[str], list[str]]:
    parser = _TableParser()
    parser.feed(html_text)
    candidates: list[tuple[list[str], list[str]]] = []

    for table in parser.tables:
        header_index = None
        headers: list[str] | None = None
        for index, row in enumerate(table):
            normalized = {normalize_label(cell) for cell in row}
            if "codigo ibge" in normalized and "municipio" in normalized:
                header_index = index
                headers = row
                break
        if headers is None or header_index is None:
            continue
        for row in table[header_index + 1 :]:
            if ibge_code in {cell.strip() for cell in row}:
                candidates.append((headers, row))

    if not candidates:
        raise ValueError(f"O município {ibge_code} não foi encontrado nas tabelas HTML.")
    if len(candidates) > 1:
        raise ValueError(
            f"Foram encontradas {len(candidates)} linhas para o município {ibge_code}."
        )
    headers, row = candidates[0]
    if len(headers) != len(row):
        raise ValueError(
            "A linha municipal não possui a mesma largura do cabeçalho: "
            f"headers={len(headers)}, cells={len(row)}"
        )
    return headers, row


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


def _municipality_fields(headers: list[str], row: list[str]) -> tuple[str, str]:
    pairs = dict(zip((normalize_label(header) for header in headers), row, strict=True))
    municipality = str(pairs.get("municipio", "")).strip()
    uf = str(pairs.get("uf", "")).strip()
    return municipality, uf


def _profile_for_year(
    *,
    year: int,
    headers: list[str],
    row: list[str],
    source_url: str,
    source_sha256: str,
    ibge_code: str,
) -> pd.DataFrame:
    municipality, uf = _municipality_fields(headers, row)
    records: list[dict[str, object]] = []
    for order, (label, value_text) in enumerate(zip(headers, row, strict=True), start=1):
        level = indicator_level(label)
        records.append(
            {
                "reference_year": year,
                "edition_type": "published_original",
                "comparability_status": "NOT_STRICTLY_COMPARABLE_ACROSS_EDITIONS",
                "ibge_code": ibge_code,
                "municipality_observed": municipality,
                "uf_observed": uf,
                "indicator_order": order,
                "indicator_label": label,
                "indicator_key": normalize_label(label).replace(" ", "_"),
                "indicator_level": level,
                "value_text": value_text,
                "value_numeric": parse_published_number(value_text),
                "unit_status": "AS_PUBLISHED_NOT_VALIDATED",
                "nature": "observed",
                "source_url": source_url,
                "source_sha256": source_sha256,
            }
        )
    return pd.DataFrame(records)


def build_published_ips(
    snapshot_path: Path,
    *,
    ibge_code: str = DEFAULT_IBGE_CODE,
    municipality: str = DEFAULT_MUNICIPALITY,
    expected_years: tuple[int, ...] = DEFAULT_YEARS,
) -> IpsPublishedResult:
    """Constrói perfis anuais sem calcular variação entre edições não comparáveis."""
    root = snapshot_path.expanduser().resolve()
    manifest = _manifest(root)
    years = tuple(sorted(int(value) for value in manifest["reference_year"].tolist()))
    if years != tuple(sorted(expected_years)):
        raise ValueError(f"Anos inesperados no manifesto: observados={years}")

    profiles: list[pd.DataFrame] = []
    source_rows: list[dict[str, object]] = []
    for record in manifest.sort_values("reference_year").to_dict("records"):
        year = int(record["reference_year"])
        local_path = root / str(record["local_file"])
        content = local_path.read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        if digest != str(record["sha256"]):
            raise ValueError(f"SHA-256 divergente na captura de {year}.")
        headers, row = _extract_code_table(content.decode("utf-8"), ibge_code)
        profile = _profile_for_year(
            year=year,
            headers=headers,
            row=row,
            source_url=str(record["requested_url"]),
            source_sha256=digest,
            ibge_code=ibge_code,
        )
        observed_name = str(profile["municipality_observed"].iloc[0])
        if municipality.casefold() not in observed_name.casefold():
            raise ValueError(
                f"Município inesperado em {year}: observado={observed_name!r}"
            )
        profiles.append(profile)
        source_rows.append(
            {
                "reference_year": year,
                "source_url": str(record["requested_url"]),
                "source_sha256": digest,
                "table_columns_observed": len(headers),
                "municipality_cells_observed": len(row),
            }
        )

    published = pd.concat(profiles, ignore_index=True)
    profile_2026 = published.loc[published["reference_year"].eq(2026)].copy()
    summary_2026 = profile_2026.loc[
        profile_2026["indicator_level"].isin({"index", "dimension", "component"})
    ].reset_index(drop=True)

    metadata: dict[str, object] = {
        "dataset": "IPS Brasil — edições originalmente publicadas",
        "municipality": municipality,
        "ibge_code": ibge_code,
        "geographic_scope": "municipality",
        "reference_years": list(years),
        "edition_type": "published_original",
        "published_rows_observed": len(published),
        "profile_2026_rows_observed": len(profile_2026),
        "summary_2026_rows_observed": len(summary_2026),
        "sources": source_rows,
        "data_nature": "observed",
        "comparability_status": "NOT_STRICTLY_COMPARABLE_ACROSS_EDITIONS",
        "temporal_change_calculated": False,
        "harmonized_series_status": "NOT_INCLUDED_REQUIRES_LIVEVIEW_EVENT",
        "limitations": [
            "Os anos 2024, 2025 e 2026 preservam as edições originalmente publicadas.",
            "Não são calculadas variações entre edições metodologicamente não comparáveis.",
            "As unidades são preservadas conforme a tabela e ainda exigem catálogo metodológico.",
            "A série harmonizada 2024–2026 será construída em módulo separado.",
        ],
    }
    return IpsPublishedResult(
        published_long=published,
        profile_2026=profile_2026,
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
        result.published_long.to_csv(
            partial / "ips_published_editions_long.csv",
            index=False,
        )
        result.profile_2026.to_csv(partial / "ips_2026_full_profile.csv", index=False)
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
