"""Inventário, sem execução, de consultas complementares para São Borja."""

from __future__ import annotations

import hashlib
import html
import re
import shutil
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pandas as pd

MUNICIPALITY_CODE = "4318002"
PAGE_SPECS = {
    "ibge_censo_2022_panorama": (
        "https://censo2022.ibge.gov.br/panorama/index.html?localidade=4318002",
        "IBGE",
        "PRIMARY_OFFICIAL",
    ),
    "ibge_cidades_panorama": (
        "https://cidades.ibge.gov.br/brasil/rs/sao-borja/panorama",
        "IBGE",
        "PRIMARY_OFFICIAL",
    ),
    "sebrae_observatorio_profile": (
        "https://observatorio.sebrae.com.br/profile/geo/sao-borja",
        "Sebrae/Datawheel",
        "SECONDARY_AGGREGATOR",
    ),
}
ALLOWED_PAGE_HOSTS = {
    "censo2022.ibge.gov.br",
    "cidades.ibge.gov.br",
    "observatorio.sebrae.com.br",
}
QUERY_HOST = "apiv2-observatorio.sebrae.com.br"

SOURCE_BY_CUBE = {
    "RAIS": "Ministério do Trabalho/RAIS",
    "CAGED": "Ministério do Trabalho/CAGED",
    "RF": "Receita Federal",
    "INEP": "INEP",
    "IBGE": "IBGE",
    "SICONFI": "Tesouro Nacional/SICONFI",
    "MDIC": "MDIC/Comex Stat",
    "DATASUS": "Ministério da Saúde/DATASUS",
    "ANS": "ANS",
    "MDS": "MDS",
    "ANATEL": "ANATEL",
    "ANEEL": "ANEEL",
    "BCB": "Banco Central do Brasil",
    "PNUD": "PNUD/Ipea/FJP",
    "TSE": "TSE",
    "PEVS": "IBGE/PEVS",
    "PAM": "IBGE/PAM",
    "PPM": "IBGE/PPM",
    "REDESIM": "REDESIM",
}


@dataclass(frozen=True)
class InventoryResult:
    snapshot_path: Path
    output_path: Path
    pages: pd.DataFrame
    queries: pd.DataFrame
    overlaps: pd.DataFrame
    limitations: pd.DataFrame
    summary: pd.DataFrame


def _validate_page_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_PAGE_HOSTS:
        raise ValueError(f"Página fora do escopo permitido: {url}")


def _fetch_page(session, source_id: str, url: str, timeout: float, limit: int):
    _validate_page_url(url)
    response = session.get(
        url,
        timeout=timeout,
        headers={"User-Agent": "sbmi-complementary-source-inventory/1.0"},
    )
    response.raise_for_status()
    content = bytes(response.content)
    if not content or len(content) > limit:
        raise ValueError(f"Página vazia ou acima do limite: {source_id}")
    content_type = str(response.headers.get("Content-Type", ""))
    if "html" not in content_type.lower():
        raise ValueError(f"Tipo inesperado em {source_id}: {content_type}")
    final_url = str(getattr(response, "url", url))
    _validate_page_url(final_url)
    return content, {
        "source_id": source_id,
        "requested_url": url,
        "final_url": final_url,
        "obtained_at": datetime.now(UTC).isoformat(),
        "status_code": int(response.status_code),
        "content_type": content_type,
        "bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
        "local_file": f"{source_id}.html",
        "nature": "observed",
    }


def _cube(url: str) -> str:
    return parse_qs(urlparse(url).query).get("cube", [""])[0]


def _primary_source(cube: str) -> str:
    upper = cube.upper()
    for prefix, source in SOURCE_BY_CUBE.items():
        if upper.startswith(prefix):
            return source
    if "EXP_IMP" in upper:
        return "MDIC/Comex Stat"
    return "NOT_CONFIRMED"


def _dimension(cube: str, url: str = "") -> str:
    upper = cube.upper()
    if upper.startswith(("RAIS", "CAGED")):
        return "renda_emprego_trabalho"
    if upper.startswith("INEP"):
        return "educacao"
    if upper.startswith(("SICONFI",)):
        return "financas_publicas_transferencias"
    if upper.startswith(("DATASUS", "ANS", "MDS")):
        return "saude_condicoes_sociais"
    if upper.startswith(("ANATEL", "ANEEL", "BCB_AGENC")):
        return "infraestrutura_conectividade"
    if upper.startswith(("IBGE_CENSO", "PNUD", "TSE")):
        return "ambiente_sociocultural_territorial"
    if upper == "IBGE" and "population" in url.lower():
        return "demografia"
    if upper.startswith(("RF", "IBGE", "MDIC", "PEVS", "PAM", "PPM", "BCB")):
        return "economia_estrutura_produtiva"
    if "EXP_IMP" in upper:
        return "economia_estrutura_produtiva"
    if upper.startswith("REDESIM"):
        return "ambiente_politico_regulatorio"
    return "transversal_multitematico"


def _overlap(cube: str) -> tuple[str, str]:
    upper = cube.upper()
    if upper.startswith(("PEVS", "PAM", "PPM")):
        return "PARTIAL_OVERLAP", "Comparar com a captura SIDRA já integrada."
    if upper.startswith("RAIS"):
        return "PARTIAL_OVERLAP", "Comparar com os produtos RAIS locais auditados."
    if upper.startswith("SICONFI"):
        return "PARTIAL_OVERLAP", "Comparar com o staging fiscal já validado."
    if upper.startswith("IBGE_CENSO"):
        return "PARTIAL_OVERLAP", "Comparar com o módulo censitário curado."
    return "COMPLEMENTARY", "Avaliar autoridade e conceito antes da coleta."


def _extract_queries(content: bytes) -> pd.DataFrame:
    text = html.unescape(content.decode("utf-8", errors="replace"))
    text = text.replace("\\u0026", "&").replace("\\n", "")
    matches = re.findall(
        r"https://apiv2-observatorio\.sebrae\.com\.br/tesseract/[^\"' <]+",
        text,
    )
    urls = {
        part.rstrip("\\")
        for match in matches
        for part in match.split("|||")
        if MUNICIPALITY_CODE in part
    }
    rows = []
    for number, url in enumerate(sorted(urls), start=1):
        parsed = urlparse(url)
        if parsed.scheme != "https" or parsed.hostname != QUERY_HOST:
            raise ValueError(f"Endpoint extraído fora do domínio permitido: {url}")
        cube = _cube(url)
        overlap, decision = _overlap(cube)
        rows.append({
            "query_id": f"sebrae_candidate_{number:03d}",
            "municipality_code": MUNICIPALITY_CODE,
            "aggregator": "Sebrae/Datawheel",
            "primary_source_declared": _primary_source(cube),
            "cube": cube,
            "dimension": _dimension(cube, url),
            "query_url": url,
            "overlap_classification": overlap,
            "recommended_decision": decision,
            "execution_status": "PREPARED_NOT_EXECUTED",
            "nature": "observed_url_and_calculated_classification",
        })
    return pd.DataFrame(rows)


def build_complementary_source_inventory(
    session,
    *,
    snapshot_root: Path,
    audit_root: Path,
    execution_id: str,
    timeout_seconds: float = 45.0,
    max_page_bytes: int = 15_000_000,
) -> InventoryResult:
    if Path(execution_id).name != execution_id or not execution_id:
        raise ValueError("execution_id deve ser um nome simples")
    snapshot = snapshot_root.resolve() / execution_id
    output = audit_root.resolve() / execution_id
    snapshot_partial = snapshot.with_name(f".{snapshot.name}.partial")
    output_partial = output.with_name(f".{output.name}.partial")
    if any(path.exists() for path in (snapshot, output, snapshot_partial, output_partial)):
        raise FileExistsError("Saída existente ou incompleta")
    fetched = {
        source_id: _fetch_page(
            session, source_id, spec[0], timeout_seconds, max_page_bytes
        )
        for source_id, spec in PAGE_SPECS.items()
    }
    pages = pd.DataFrame([
        metadata | {
            "institution": PAGE_SPECS[source_id][1],
            "authority_role": PAGE_SPECS[source_id][2],
        }
        for source_id, (_, metadata) in fetched.items()
    ])
    queries = _extract_queries(fetched["sebrae_observatorio_profile"][0])
    overlaps = queries[[
        "query_id", "cube", "dimension", "primary_source_declared",
        "overlap_classification", "recommended_decision",
    ]].copy()
    limitations = pd.DataFrame([
        ("ibge_censo_2022_panorama", "QUERY_DISCOVERY_PENDING",
         "A página é oficial, mas parâmetros de tabelas não foram inferidos."),
        ("ibge_cidades_panorama", "QUERY_DISCOVERY_PENDING",
         "Indicadores heterogêneos exigem registro por pesquisa e período."),
        ("sebrae_observatorio_profile", "SECONDARY_AGGREGATOR",
         "Preferir a fonte primária quando houver endpoint oficial equivalente."),
        ("all", "VALUES_NOT_REQUESTED",
         "Nenhuma URL extraída foi executada nesta etapa."),
    ], columns=["scope", "limitation_code", "description"])
    summary = pd.DataFrame([
        ("pages_captured", len(pages), "observed"),
        ("query_candidates", len(queries), "calculated"),
        ("distinct_cubes", queries["cube"].nunique(), "calculated"),
        ("dimensions_represented", queries["dimension"].nunique(), "calculated"),
        ("values_requests", 0, "observed"),
    ], columns=["indicator", "value", "nature"])
    snapshot_partial.mkdir(parents=True)
    output_partial.mkdir(parents=True)
    try:
        for source_id, (content, _) in fetched.items():
            (snapshot_partial / f"{source_id}.html").write_bytes(content)
        pages.to_csv(snapshot_partial / "page_manifest.csv", index=False)
        pages.to_csv(output_partial / "source_page_register.csv", index=False)
        queries.to_csv(output_partial / "candidate_query_inventory.csv", index=False)
        overlaps.to_csv(output_partial / "overlap_register.csv", index=False)
        limitations.to_csv(output_partial / "limitation_register.csv", index=False)
        summary.to_csv(output_partial / "inventory_summary.csv", index=False)
        snapshot.parent.mkdir(parents=True, exist_ok=True)
        output.parent.mkdir(parents=True, exist_ok=True)
        snapshot_partial.replace(snapshot)
        output_partial.replace(output)
    except Exception:
        shutil.rmtree(snapshot_partial, ignore_errors=True)
        shutil.rmtree(output_partial, ignore_errors=True)
        raise
    return InventoryResult(
        snapshot, output, pages, queries, overlaps, limitations, summary
    )
