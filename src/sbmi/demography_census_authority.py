"""Verificação externa da autoridade das fontes do Censo 2022."""

from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd
import requests

from sbmi.base_territorial_coverage import normalize_text

LOCALITY_CODE = "4318002"
OFFICIAL_INSTITUTION = "Instituto Brasileiro de Geografia e Estatística - IBGE"
PANORAMA_URL = (
    "https://censo2022.ibge.gov.br/panorama/?localidade=4318002"
)
DOWNLOADS_URL = (
    "https://censo2022.ibge.gov.br/panorama/downloads.html?localidade=4318002"
)
MUNICIPALITY_API_URL = (
    "https://servicodados.ibge.gov.br/api/v1/localidades/municipios/4318002"
)
ALLOWED_DOMAINS = {
    "censo2022.ibge.gov.br",
    "servicodados.ibge.gov.br",
}
QUALITY_REQUIRED_COLUMNS = {
    "dataset_identity",
    "processed_reuse_status",
    "quality_class",
}
PROVENANCE_REQUIRED_COLUMNS = {
    "dataset_identity",
    "source_authority_status",
    "provenance_status",
}

SOURCE_REGISTRY = (
    (
        "censo 2022 alfabetizacao sao borja rs",
        "Alfabetização",
        "Alfabetização: Resultados do universo",
        "2024-05-17",
        "UNIVERSE",
    ),
    (
        "censo 2022 caracteristicas do entorno sao borja rs",
        "Características do entorno",
        "Características Urbanísticas do Entorno dos Domicílios",
        "2025-04-17",
        "UNIVERSE",
    ),
    (
        "censo 2022 caracteristicas dos domicilios sao borja rs",
        "Características dos domicílios",
        "Características dos domicílios - Resultados do universo",
        "2024-02-23",
        "UNIVERSE",
    ),
    (
        "censo 2022 composicao domiciliar sao borja rs",
        "Composição domiciliar",
        "Composição domiciliar e óbitos informados: Resultados do universo",
        "2024-10-25",
        "UNIVERSE",
    ),
    (
        "censo 2022 crescimento populacional sao borja rs",
        "Crescimento populacional",
        "População e Domicílios - Primeiros Resultados",
        "2023-06-28",
        "UNIVERSE",
    ),
    (
        "censo 2022 deficiencia e autismo sao borja rs",
        "Deficiência e autismo",
        (
            "Pessoas com deficiência e Pessoas diagnosticadas com transtorno "
            "do espectro autista: Resultados preliminares da amostra"
        ),
        "2025-05-23",
        "SAMPLE_PRELIMINARY",
    ),
    (
        "censo 2022 meios de transporte mais usados sao borja rs",
        "Meios de transporte mais usados para chegar ao trabalho",
        "Deslocamentos para trabalho e para estudo: Resultados preliminares da amostra",
        "2025-10-09",
        "SAMPLE_PRELIMINARY",
    ),
    (
        "censo 2022 nivel de instrucao sao borja rs",
        "Nível de instrução",
        "Educação: Resultados preliminares da amostra",
        "2025-02-25",
        "SAMPLE_PRELIMINARY",
    ),
    (
        "censo 2022 piramide etaria sao borja rs",
        "Pirâmide etária",
        "População por idade e sexo - Resultados do universo",
        "2023-10-27",
        "UNIVERSE",
    ),
    (
        "censo 2022 populacao indigena sao borja rs",
        "População indígena",
        "Indígenas: Primeiros resultados do universo",
        "2023-08-07",
        "UNIVERSE",
    ),
    (
        "censo 2022 populacao por cor ou raca sao borja rs",
        "Cor ou Raça",
        "População por cor ou raça - Resultados do universo",
        "2023-12-22",
        "UNIVERSE",
    ),
    (
        "censo 2022 populacao por religiao sao borja rs",
        "Religião",
        "Religiões: Resultados preliminares da amostra",
        "2025-06-06",
        "SAMPLE_PRELIMINARY",
    ),
    (
        "censo 2022 populacao por sexo sao borja rs",
        "Sexo",
        "População por idade e sexo - Resultados do universo",
        "2023-10-27",
        "UNIVERSE",
    ),
    (
        "censo 2022 populacao por situacao do domicilio sao borja rs",
        "População por situação do domicílio",
        "População e Domicílios - Primeiros Resultados",
        "2023-06-28",
        "UNIVERSE",
    ),
    (
        "censo 2022 populacao quilombola sao borja rs",
        "População quilombola",
        "Quilombolas: Primeiros resultados do universo",
        "2023-07-27",
        "UNIVERSE",
    ),
    (
        "censo 2022 populacao residente em favelas sao borja rs",
        "População residente em favelas",
        "Favelas e Comunidades urbanas: Resultados do universo",
        "2024-11-08",
        "UNIVERSE",
    ),
    (
        "censo 2022 territorio sao borja rs",
        "Território",
        "População e Domicílios - Primeiros Resultados",
        "2023-06-28",
        "UNIVERSE",
    ),
)


@dataclass(frozen=True)
class OfficialPage:
    page_id: str
    url: str
    content: bytes
    status_code: int
    content_type: str
    sha256: str


@dataclass(frozen=True)
class CensusAuthorityResult:
    registry: pd.DataFrame
    verification: pd.DataFrame
    pages: pd.DataFrame
    summary: pd.DataFrame
    snapshot_path: Path
    output_path: Path


def build_source_registry() -> pd.DataFrame:
    """Constrói o registro versionado de produtos oficiais associados aos temas."""
    records = []
    for identity, topic, product, release_date, result_basis in SOURCE_REGISTRY:
        records.append(
            {
                "dataset_identity": identity,
                "official_institution": OFFICIAL_INSTITUTION,
                "official_platform": "Panorama do Censo Demográfico 2022",
                "official_locality_code": LOCALITY_CODE,
                "official_locality_name": "São Borja (RS)",
                "panorama_topic_label": topic,
                "official_product_title": product,
                "official_release_date": release_date,
                "official_result_basis": result_basis,
                "official_panorama_url": PANORAMA_URL,
                "official_download_catalog_url": DOWNLOADS_URL,
                "official_municipality_url": MUNICIPALITY_API_URL,
                "nature": "externally_observed_registry",
            }
        )
    return pd.DataFrame(records).sort_values("dataset_identity").reset_index(drop=True)


def _validate_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc not in ALLOWED_DOMAINS:
        raise ValueError(f"URL oficial fora da lista permitida: {url}")


def _fetch_page(
    session: requests.Session,
    page_id: str,
    url: str,
    *,
    timeout_seconds: float,
    max_bytes: int,
) -> OfficialPage:
    _validate_url(url)
    response = session.get(
        url,
        timeout=timeout_seconds,
        headers={"User-Agent": "sbmi-demography-authority-audit/1.0"},
    )
    response.raise_for_status()
    content = bytes(response.content)
    if not content:
        raise ValueError(f"Página oficial vazia: {url}")
    if len(content) > max_bytes:
        raise ValueError(
            f"Página oficial excede o limite: bytes={len(content)}, limite={max_bytes}"
        )
    return OfficialPage(
        page_id=page_id,
        url=url,
        content=content,
        status_code=int(response.status_code),
        content_type=str(response.headers.get("Content-Type", "")),
        sha256=hashlib.sha256(content).hexdigest(),
    )


def _visible_text(content: bytes) -> str:
    decoded = content.decode("utf-8", errors="replace")
    without_scripts = re.sub(
        r"<(script|style)\b[^>]*>.*?</\1>",
        " ",
        decoded,
        flags=re.IGNORECASE | re.DOTALL,
    )
    without_tags = re.sub(r"<[^>]+>", " ", without_scripts)
    return normalize_text(html.unescape(without_tags))


def _contains(text: str, value: object) -> bool:
    return normalize_text(value) in text


def _municipality_confirmed(page: OfficialPage) -> bool:
    try:
        payload = json.loads(page.content)
        state = payload["regiao-imediata"]["regiao-intermediaria"]["UF"]
    except (json.JSONDecodeError, KeyError, TypeError):
        return False
    return (
        str(payload.get("id")) == LOCALITY_CODE
        and normalize_text(payload.get("nome")) == normalize_text("São Borja")
        and state.get("id") == 43
        and state.get("sigla") == "RS"
        and normalize_text(state.get("nome")) == normalize_text("Rio Grande do Sul")
    )


def _quality_lookup(quality: pd.DataFrame) -> dict[str, object]:
    missing = QUALITY_REQUIRED_COLUMNS.difference(quality.columns)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes na revisão de qualidade: "
            f"{sorted(missing)}"
        )
    return {
        str(row.dataset_identity): row
        for row in quality.itertuples(index=False)
    }


def _provenance_lookup(provenance: pd.DataFrame) -> dict[str, object]:
    missing = PROVENANCE_REQUIRED_COLUMNS.difference(provenance.columns)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes na auditoria de proveniência: "
            f"{sorted(missing)}"
        )
    return {
        str(row.dataset_identity): row
        for row in provenance.itertuples(index=False)
    }


def _reuse_decision(quality_row: object) -> str:
    status = str(getattr(quality_row, "processed_reuse_status", ""))
    if status == "QUARANTINE_PROCESSED_PRODUCT":
        return "REBUILD_FROM_OFFICIAL_SOURCE_REQUIRED"
    return "OFFICIAL_VALUE_RECONCILIATION_REQUIRED_BEFORE_CURATED_REUSE"


def verify_registry(
    registry: pd.DataFrame,
    quality: pd.DataFrame,
    provenance: pd.DataFrame,
    pages: dict[str, OfficialPage],
) -> pd.DataFrame:
    """Confronta o registro com páginas oficiais e diagnósticos locais."""
    required_pages = {"panorama", "downloads", "municipality"}
    missing_pages = required_pages.difference(pages)
    if missing_pages:
        raise ValueError(f"Páginas oficiais ausentes: {sorted(missing_pages)}")
    quality_by_id = _quality_lookup(quality)
    provenance_by_id = _provenance_lookup(provenance)
    panorama_text = _visible_text(pages["panorama"].content)
    downloads_text = _visible_text(pages["downloads"].content)
    municipality_confirmed = _municipality_confirmed(pages["municipality"])

    records: list[dict[str, object]] = []
    for row in registry.itertuples(index=False):
        identity = str(row.dataset_identity)
        if identity not in quality_by_id or identity not in provenance_by_id:
            raise ValueError(f"Dataset sem diagnóstico local completo: {identity}")
        quality_row = quality_by_id[identity]
        provenance_row = provenance_by_id[identity]
        topic_present = _contains(panorama_text, row.panorama_topic_label)
        product_present = _contains(downloads_text, row.official_product_title)
        release_present = _contains(
            downloads_text,
            pd.Timestamp(row.official_release_date).strftime("%d/%m/%Y"),
        )
        platform_confirmed = bool(topic_present and product_present and release_present)
        official_status = (
            "OFFICIAL_PLATFORM_TOPIC_AND_PRODUCT_CONFIRMED"
            if platform_confirmed and municipality_confirmed
            else "OFFICIAL_VERIFICATION_INCOMPLETE"
        )
        local_status = str(provenance_row.source_authority_status)
        records.append(
            {
                **row._asdict(),
                "panorama_topic_present": topic_present,
                "official_product_present": product_present,
                "official_release_date_present": release_present,
                "official_municipality_code_confirmed": municipality_confirmed,
                "external_authority_status": official_status,
                "local_file_provenance_status": str(
                    provenance_row.provenance_status
                ),
                "local_file_authority_status": local_status,
                "local_file_origin_linkage_status": (
                    "LOCAL_FILE_ORIGIN_NOT_ESTABLISHED"
                    if local_status != "ESTABLISHED"
                    else "LOCAL_FILE_ORIGIN_ESTABLISHED"
                ),
                "quality_class": str(quality_row.quality_class),
                "processed_reuse_status": str(
                    quality_row.processed_reuse_status
                ),
                "recommended_next_action": _reuse_decision(quality_row),
                "conceptual_validation_status": (
                    "PENDING_MEASURE_DEFINITION_AND_VALUE_RECONCILIATION"
                ),
                "what_cannot_be_concluded": (
                    "A confirmação da plataforma e do produto oficial não prova que "
                    "a planilha local seja o arquivo oficial originalmente baixado."
                ),
                "verification_nature": "external_observation_and_calculation",
            }
        )
    return pd.DataFrame(records).sort_values("dataset_identity").reset_index(drop=True)


def _write_snapshot(
    pages: dict[str, OfficialPage],
    root: Path,
    snapshot_id: str,
    *,
    replace: bool,
) -> tuple[Path, pd.DataFrame]:
    target = root.expanduser().resolve() / snapshot_id
    if target.exists():
        if not replace:
            raise FileExistsError(f"Captura oficial já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    records = []
    try:
        for page_id, page in sorted(pages.items()):
            suffix = ".json" if page_id == "municipality" else ".html"
            file_name = f"{page_id}{suffix}"
            (partial / file_name).write_bytes(page.content)
            records.append(
                {
                    "page_id": page_id,
                    "url": page.url,
                    "status_code": page.status_code,
                    "content_type": page.content_type,
                    "bytes": len(page.content),
                    "sha256": page.sha256,
                    "local_file": file_name,
                    "nature": "observed",
                }
            )
        manifest = pd.DataFrame(records)
        manifest.to_csv(partial / "official_page_manifest.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.rename(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target, manifest


def _write_audit(
    registry: pd.DataFrame,
    verification: pd.DataFrame,
    pages: pd.DataFrame,
    root: Path,
    run_id: str,
    *,
    replace: bool,
) -> tuple[Path, pd.DataFrame]:
    target = root.expanduser().resolve() / run_id
    if target.exists():
        if not replace:
            raise FileExistsError(f"Auditoria de autoridade já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    summary = pd.DataFrame(
        [
            ("datasets_registered", len(registry), "calculated"),
            (
                "official_topics_confirmed",
                int(verification["panorama_topic_present"].sum()),
                "calculated",
            ),
            (
                "official_products_confirmed",
                int(verification["official_product_present"].sum()),
                "calculated",
            ),
            (
                "official_release_dates_confirmed",
                int(verification["official_release_date_present"].sum()),
                "calculated",
            ),
            (
                "official_authority_confirmed_datasets",
                int(
                    verification["external_authority_status"]
                    .eq("OFFICIAL_PLATFORM_TOPIC_AND_PRODUCT_CONFIRMED")
                    .sum()
                ),
                "calculated",
            ),
            (
                "local_file_origin_established_datasets",
                int(
                    verification["local_file_origin_linkage_status"]
                    .eq("LOCAL_FILE_ORIGIN_ESTABLISHED")
                    .sum()
                ),
                "observed",
            ),
            (
                "official_rebuild_required_datasets",
                int(
                    verification["recommended_next_action"]
                    .eq("REBUILD_FROM_OFFICIAL_SOURCE_REQUIRED")
                    .sum()
                ),
                "calculated",
            ),
            ("conceptually_validated_datasets", 0, "observed"),
        ],
        columns=["indicator", "value", "nature"],
    )
    try:
        registry.to_csv(partial / "demography_census_official_registry.csv", index=False)
        verification.to_csv(
            partial / "demography_census_authority_verification.csv",
            index=False,
        )
        pages.to_csv(partial / "demography_census_official_pages.csv", index=False)
        summary.to_csv(
            partial / "demography_census_authority_summary.csv",
            index=False,
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.rename(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target, summary


def audit_census_authority(
    session: requests.Session,
    quality: pd.DataFrame,
    provenance: pd.DataFrame,
    *,
    snapshots_root: Path,
    audit_root: Path,
    snapshot_id: str,
    run_id: str,
    replace: bool = False,
    timeout_seconds: float = 30.0,
    max_page_bytes: int = 5_000_000,
) -> CensusAuthorityResult:
    """Captura páginas oficiais e verifica autoridade sem atribuir linhagem local."""
    if timeout_seconds <= 0 or max_page_bytes <= 0:
        raise ValueError("Timeout e limite de bytes devem ser positivos.")
    pages = {
        "panorama": _fetch_page(
            session,
            "panorama",
            PANORAMA_URL,
            timeout_seconds=timeout_seconds,
            max_bytes=max_page_bytes,
        ),
        "downloads": _fetch_page(
            session,
            "downloads",
            DOWNLOADS_URL,
            timeout_seconds=timeout_seconds,
            max_bytes=max_page_bytes,
        ),
        "municipality": _fetch_page(
            session,
            "municipality",
            MUNICIPALITY_API_URL,
            timeout_seconds=timeout_seconds,
            max_bytes=max_page_bytes,
        ),
    }
    registry = build_source_registry()
    verification = verify_registry(registry, quality, provenance, pages)
    snapshot_path, page_manifest = _write_snapshot(
        pages,
        snapshots_root,
        snapshot_id,
        replace=replace,
    )
    output_path, summary = _write_audit(
        registry,
        verification,
        page_manifest,
        audit_root,
        run_id,
        replace=replace,
    )
    return CensusAuthorityResult(
        registry=registry,
        verification=verification,
        pages=page_manifest,
        summary=summary,
        snapshot_path=snapshot_path,
        output_path=output_path,
    )
