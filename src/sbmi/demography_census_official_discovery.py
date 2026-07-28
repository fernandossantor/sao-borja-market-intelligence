"""Descoberta verificável de links em páginas oficiais de produtos censitários."""

from __future__ import annotations

import hashlib
import shutil
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

import pandas as pd
import requests

HOUSEHOLD_COMPOSITION_URL = (
    "https://www.ibge.gov.br/estatisticas/sociais/populacao/"
    "22827-censo-demografico-2022.html?edicao=41639&t=resultados"
)
POPULATION_HOUSEHOLDS_URL = (
    "https://www.ibge.gov.br/estatisticas/sociais/populacao/"
    "22827-censo-demografico-2022.html?edicao=37225&t=resultados"
)
PAGE_SPECS = (
    (
        "household_composition",
        "Composição domiciliar e óbitos informados: Resultados do universo",
        HOUSEHOLD_COMPOSITION_URL,
    ),
    (
        "population_households",
        "População e Domicílios - Primeiros Resultados",
        POPULATION_HOUSEHOLDS_URL,
    ),
)
FETCH_DOMAINS = {"www.ibge.gov.br"}
OFFICIAL_DOMAIN_SUFFIXES = (".ibge.gov.br",)
DIRECT_FILE_SUFFIXES = (".csv", ".ods", ".xls", ".xlsx", ".zip")


@dataclass(frozen=True)
class OfficialProductPage:
    page_id: str
    product_title: str
    requested_url: str
    final_url: str
    content: bytes
    status_code: int
    content_type: str
    fetch_status: str
    challenge_detected: bool
    sha256: str


@dataclass(frozen=True)
class OfficialDiscoveryResult:
    pages: pd.DataFrame
    links: pd.DataFrame
    candidates: pd.DataFrame
    summary: pd.DataFrame
    snapshot_path: Path
    output_path: Path


class _AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._href: str | None = None
        self._text: list[str] = []
        self.anchors: list[tuple[str, str]] = []

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        if tag.casefold() != "a":
            return
        attributes = dict(attrs)
        href = attributes.get("href")
        if href:
            self._href = href.strip()
            self._text = []

    def handle_data(self, data: str) -> None:
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.casefold() == "a" and self._href is not None:
            text = " ".join("".join(self._text).split())
            self.anchors.append((self._href, text))
            self._href = None
            self._text = []


def _validate_identifier(identifier: str, field: str) -> None:
    if not isinstance(identifier, str) or not identifier.strip():
        raise ValueError(f"{field} deve ser um identificador não vazio")
    if Path(identifier).name != identifier or identifier in {".", ".."}:
        raise ValueError(f"{field} deve ser um nome simples")


def _ensure_output_available(root: Path, identifier: str) -> None:
    target = root.expanduser().resolve() / identifier
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")


def _validate_fetch_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in FETCH_DOMAINS:
        raise ValueError(f"URL oficial fora da lista de captura: {url}")


def _is_official_url(url: str) -> bool:
    hostname = (urlparse(url).hostname or "").casefold()
    return hostname == "ibge.gov.br" or hostname.endswith(OFFICIAL_DOMAIN_SUFFIXES)


def _candidate_kind(url: str, anchor_text: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.casefold()
    text = anchor_text.casefold()
    if (parsed.hostname or "").casefold() == "sidra.ibge.gov.br":
        return "SIDRA_LINK"
    if path.endswith(DIRECT_FILE_SUFFIXES):
        return "DIRECT_FILE_LINK"
    if "download" in path or "download" in text:
        return "DOWNLOAD_PAGE_LINK"
    if "tabela" in text or "resultado" in text:
        return "TABLE_OR_RESULTS_LINK"
    return "OTHER_OFFICIAL_LINK"


def _fetch_page(
    session: requests.Session,
    page_id: str,
    product_title: str,
    url: str,
    *,
    timeout_seconds: float,
    max_page_bytes: int,
) -> OfficialProductPage:
    _validate_fetch_url(url)
    response = session.get(
        url,
        timeout=timeout_seconds,
        headers={"User-Agent": "sbmi-census-official-discovery/1.0"},
    )
    content = bytes(response.content)
    if not content:
        raise ValueError(f"Página oficial vazia: {url}")
    if len(content) > max_page_bytes:
        raise ValueError(
            f"Página oficial excede o limite: bytes={len(content)}, limite={max_page_bytes}"
        )
    content_type = str(response.headers.get("Content-Type", ""))
    if "text/html" not in content_type.casefold():
        raise ValueError(f"Tipo de conteúdo inesperado em {url}: {content_type}")
    final_url = str(getattr(response, "url", url))
    _validate_fetch_url(final_url)
    status_code = int(response.status_code)
    fetch_status = "CAPTURED" if 200 <= status_code < 300 else "HTTP_ERROR"
    challenge_detected = (
        str(response.headers.get("cf-mitigated", "")).casefold() == "challenge"
        or b"challenges.cloudflare.com" in content
    )
    return OfficialProductPage(
        page_id=page_id,
        product_title=product_title,
        requested_url=url,
        final_url=final_url,
        content=content,
        status_code=status_code,
        content_type=content_type,
        fetch_status=fetch_status,
        challenge_detected=challenge_detected,
        sha256=hashlib.sha256(content).hexdigest(),
    )


def extract_official_links(pages: dict[str, OfficialProductPage]) -> pd.DataFrame:
    """Extrai links oficiais sem atribuir correspondência temática ou conceitual."""
    records: list[dict[str, object]] = []
    for page_id, page in sorted(pages.items()):
        if page.fetch_status != "CAPTURED":
            continue
        parser = _AnchorParser()
        parser.feed(page.content.decode("utf-8", errors="replace"))
        seen: set[tuple[str, str]] = set()
        for href, anchor_text in parser.anchors:
            resolved = urljoin(page.final_url, href)
            key = (resolved, anchor_text)
            if key in seen:
                continue
            seen.add(key)
            official = _is_official_url(resolved)
            records.append(
                {
                    "page_id": page_id,
                    "product_title": page.product_title,
                    "anchor_text": anchor_text,
                    "url": resolved,
                    "domain": urlparse(resolved).hostname or "",
                    "is_official_ibge_domain": official,
                    "candidate_kind": (
                        _candidate_kind(resolved, anchor_text) if official else "NON_OFFICIAL_LINK"
                    ),
                    "conceptual_equivalence_status": "NOT_ASSESSED",
                    "nature": "observed_and_calculated",
                }
            )
    columns = [
        "page_id",
        "product_title",
        "anchor_text",
        "url",
        "domain",
        "is_official_ibge_domain",
        "candidate_kind",
        "conceptual_equivalence_status",
        "nature",
    ]
    return pd.DataFrame(records, columns=columns)


def _write_snapshot(
    pages: dict[str, OfficialProductPage],
    root: Path,
    snapshot_id: str,
) -> tuple[Path, pd.DataFrame]:
    target = root.expanduser().resolve() / snapshot_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Captura já existe ou está incompleta: {target}")
    partial.mkdir(parents=True, exist_ok=False)
    records = []
    try:
        for page_id, page in sorted(pages.items()):
            file_name = f"{page_id}.html"
            (partial / file_name).write_bytes(page.content)
            records.append(
                {
                    "page_id": page_id,
                    "product_title": page.product_title,
                    "requested_url": page.requested_url,
                    "final_url": page.final_url,
                    "status_code": page.status_code,
                    "content_type": page.content_type,
                    "fetch_status": page.fetch_status,
                    "challenge_detected": page.challenge_detected,
                    "bytes": len(page.content),
                    "sha256": page.sha256,
                    "local_file": file_name,
                    "nature": "observed",
                }
            )
        manifest = pd.DataFrame(records)
        manifest.to_csv(partial / "official_product_page_manifest.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target, manifest


def _write_audit(
    pages: pd.DataFrame,
    links: pd.DataFrame,
    root: Path,
    run_id: str,
) -> tuple[Path, pd.DataFrame, pd.DataFrame]:
    target = root.expanduser().resolve() / run_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Auditoria já existe ou está incompleta: {target}")
    official_mask = links["is_official_ibge_domain"].astype(bool)
    official = links.loc[official_mask].copy()
    candidates = official[official["candidate_kind"].ne("OTHER_OFFICIAL_LINK")].reset_index(
        drop=True
    )
    summary = pd.DataFrame(
        [
            ("pages_captured", len(pages), "observed"),
            (
                "pages_successful",
                int(pages["fetch_status"].eq("CAPTURED").sum()),
                "calculated",
            ),
            (
                "pages_http_error",
                int(pages["fetch_status"].eq("HTTP_ERROR").sum()),
                "calculated",
            ),
            (
                "cloudflare_challenges",
                int(pages["challenge_detected"].astype(bool).sum()),
                "calculated",
            ),
            ("links_observed", len(links), "calculated"),
            ("official_ibge_links", len(official), "calculated"),
            ("download_candidates", len(candidates), "calculated"),
            (
                "direct_file_candidates",
                int(candidates["candidate_kind"].eq("DIRECT_FILE_LINK").sum()),
                "calculated",
            ),
            ("conceptually_validated_candidates", 0, "observed"),
        ],
        columns=["indicator", "value", "nature"],
    )
    partial.mkdir(parents=True, exist_ok=False)
    try:
        links.to_csv(partial / "official_product_link_register.csv", index=False)
        candidates.to_csv(partial / "official_download_candidate_register.csv", index=False)
        summary.to_csv(partial / "official_discovery_summary.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target, candidates, summary


def discover_official_census_products(
    session: requests.Session,
    *,
    snapshots_root: Path,
    audit_root: Path,
    snapshot_id: str,
    run_id: str,
    timeout_seconds: float = 30.0,
    max_page_bytes: int = 5_000_000,
) -> OfficialDiscoveryResult:
    """Captura duas páginas oficiais e registra links sem baixar bases."""
    if timeout_seconds <= 0 or max_page_bytes <= 0:
        raise ValueError("Timeout e limite de bytes devem ser positivos.")
    _validate_identifier(snapshot_id, "snapshot_id")
    _validate_identifier(run_id, "run_id")
    _ensure_output_available(snapshots_root, snapshot_id)
    _ensure_output_available(audit_root, run_id)
    pages = {
        page_id: _fetch_page(
            session,
            page_id,
            product_title,
            url,
            timeout_seconds=timeout_seconds,
            max_page_bytes=max_page_bytes,
        )
        for page_id, product_title, url in PAGE_SPECS
    }
    links = extract_official_links(pages)
    snapshot_path, page_manifest = _write_snapshot(pages, snapshots_root, snapshot_id)
    output_path, candidates, summary = _write_audit(page_manifest, links, audit_root, run_id)
    return OfficialDiscoveryResult(
        pages=page_manifest,
        links=links,
        candidates=candidates,
        summary=summary,
        snapshot_path=snapshot_path,
        output_path=output_path,
    )
