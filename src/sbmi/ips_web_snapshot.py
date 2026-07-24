"""Captura reproduzível dos scorecards renderizados do IPS Brasil."""

from __future__ import annotations

import hashlib
import re
import shutil
import time
from dataclasses import dataclass
from datetime import UTC, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Protocol

import pandas as pd

DEFAULT_YEARS = (2024, 2025, 2026)
DEFAULT_IBGE_CODE = "4318002"
DEFAULT_MUNICIPALITY = "São Borja"
DEFAULT_SNAPSHOT_ID = "ips-brasil-rendered-published-2024-2026"
BASE_URL = "https://ipsbrasil.org.br/explore/scorecard"
SUMMARY_LABELS = (
    "Necessidades Humanas Básicas",
    "Fundamentos do Bem-estar",
    "Oportunidades",
    "Nutrição e Cuidados Médicos Básicos",
    "Água e Saneamento",
    "Moradia",
    "Segurança Pessoal",
    "Acesso ao Conhecimento Básico",
    "Acesso à Informação e Comunicação",
    "Saúde e Bem-estar",
    "Qualidade do Meio Ambiente",
    "Direitos Individuais",
    "Liberdades Individuais e de Escolha",
    "Inclusão Social",
    "Acesso à Educação Superior",
)

_SCORE_PATTERN = re.compile(
    r"(?<!\d)("
    r"\d{1,3}(?:\s*\.\s*\d{3})*\s*,\s*\d{1,3}"
    r"|\d{1,3}\s*\.\s*\d{1,2}"
    r")(?!\d)"
)


@dataclass(frozen=True)
class RenderedScorecard:
    """Conteúdo final de uma página após a conexão LiveView."""

    html: str
    text: str
    final_url: str
    status_code: int


class ScorecardRenderer(Protocol):
    """Contrato mínimo para renderizadores reais e dublês de teste."""

    def render(
        self,
        url: str,
        *,
        year: int,
        ibge_code: str,
        municipality: str,
        timeout_seconds: int,
    ) -> RenderedScorecard: ...

    def close(self) -> None: ...


@dataclass(frozen=True)
class ScorecardDiagnostics:
    """Sinais observados no texto renderizado."""

    municipality_present: bool
    year_marker_present: bool
    labels_present: int
    labels_with_score: int
    index_scores: int
    score_candidates: int

    @property
    def ready(self) -> bool:
        return (
            self.municipality_present
            and self.year_marker_present
            and self.labels_present == len(SUMMARY_LABELS)
            and self.labels_with_score == len(SUMMARY_LABELS)
            and self.index_scores >= 1
            and self.score_candidates >= 16
        )


@dataclass(frozen=True)
class IpsWebSnapshotResult:
    """Resumo da captura browser concluída."""

    snapshot_path: Path
    pages: int
    stored_bytes: int
    years: tuple[int, ...]
    browser_navigations: int


def scorecard_url(year: int, *, ibge_code: str = DEFAULT_IBGE_CODE) -> str:
    """Monta a URL pública do scorecard municipal para uma edição."""
    if year < 2024:
        raise ValueError("O IPS Brasil municipal disponível nesta rotina começa em 2024.")
    if not ibge_code.isdigit():
        raise ValueError("O código IBGE deve conter apenas dígitos.")
    return f"{BASE_URL}/{ibge_code}?year={year}"


def normalize_rendered_text(value: str) -> str:
    """Normaliza apenas espaços do texto efetivamente renderizado."""
    return re.sub(r"\s+", " ", value).strip()


def _parse_score_candidate(raw: str) -> Decimal | None:
    text = re.sub(r"\s+", "", raw)
    if "," in text:
        canonical = text.replace(".", "").replace(",", ".")
    else:
        canonical = text
    try:
        value = Decimal(canonical)
    except InvalidOperation:
        return None
    if Decimal("0") <= value <= Decimal("100"):
        return value
    return None


def score_candidates(text: str) -> tuple[str, ...]:
    """Retém decimais compatíveis com a escala de pontuação do IPS."""
    values: list[str] = []
    for match in _SCORE_PATTERN.finditer(text):
        raw = match.group(1)
        if _parse_score_candidate(raw) is not None:
            values.append(raw)
    return tuple(values)


def _occurrences(text: str, label: str) -> tuple[int, ...]:
    folded = text.casefold()
    return tuple(
        match.start()
        for match in re.finditer(re.escape(label.casefold()), folded)
    )


def _label_has_score(text: str, label: str) -> bool:
    for position in _occurrences(text, label):
        start = position + len(label)
        segment = text[start : min(start + 1_200, len(text))]
        if score_candidates(segment):
            return True
    return False


def scorecard_diagnostics(
    rendered_text: str,
    *,
    year: int,
    municipality: str,
) -> ScorecardDiagnostics:
    """Mede se o LiveView já publicou os agregados numéricos."""
    text = normalize_rendered_text(rendered_text)
    marker = re.compile(rf"IPS\s+BRASIL\s+{year}\b", flags=re.IGNORECASE)
    marker_matches = list(marker.finditer(text))
    index_scores = 0
    for match in marker_matches:
        segment = text[match.end() : min(match.end() + 1_500, len(text))]
        if score_candidates(segment):
            index_scores += 1

    labels_present = sum(label.casefold() in text.casefold() for label in SUMMARY_LABELS)
    labels_with_score = sum(_label_has_score(text, label) for label in SUMMARY_LABELS)
    return ScorecardDiagnostics(
        municipality_present=municipality.casefold() in text.casefold(),
        year_marker_present=bool(marker_matches),
        labels_present=labels_present,
        labels_with_score=labels_with_score,
        index_scores=index_scores,
        score_candidates=len(score_candidates(text)),
    )


def validate_rendered_scorecard(
    rendered: RenderedScorecard,
    *,
    year: int,
    ibge_code: str,
    municipality: str,
) -> ScorecardDiagnostics:
    """Valida o DOM final, incluindo a presença das pontuações."""
    if rendered.status_code >= 400:
        raise ValueError(
            f"Falha HTTP no scorecard de {year}: status={rendered.status_code}."
        )
    if ibge_code not in rendered.html:
        raise ValueError(f"Código IBGE ausente no scorecard de {year}: {ibge_code}.")
    diagnostics = scorecard_diagnostics(
        rendered.text,
        year=year,
        municipality=municipality,
    )
    if not diagnostics.ready:
        raise ValueError(
            "Scorecard renderizado sem contrato numérico completo: "
            f"ano={year}, municipio={int(diagnostics.municipality_present)}, "
            f"marcador_ano={int(diagnostics.year_marker_present)}, "
            f"rotulos={diagnostics.labels_present}/{len(SUMMARY_LABELS)}, "
            f"rotulos_com_pontuacao={diagnostics.labels_with_score}/{len(SUMMARY_LABELS)}, "
            f"indices={diagnostics.index_scores}, "
            f"candidatos={diagnostics.score_candidates}"
        )
    return diagnostics


class PlaywrightScorecardRenderer:
    """Renderiza o scorecard em Chromium até o LiveView publicar os dados."""

    def __init__(self) -> None:
        try:
            from playwright.sync_api import sync_playwright
        except ImportError as exc:
            raise RuntimeError(
                "Playwright não está instalado. Execute `make bootstrap-browser`."
            ) from exc

        self._playwright = sync_playwright().start()
        try:
            self._browser = self._playwright.chromium.launch(headless=True)
        except Exception:
            self._playwright.stop()
            raise
        self._context = self._browser.new_context(
            locale="pt-BR",
            user_agent=(
                "SBMI/0.1 (territorial-market-intelligence; "
                "reproducible-liveview-render)"
            ),
        )
        self._page = self._context.new_page()

    def render(
        self,
        url: str,
        *,
        year: int,
        ibge_code: str,
        municipality: str,
        timeout_seconds: int,
    ) -> RenderedScorecard:
        timeout_ms = timeout_seconds * 1_000
        response = self._page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=timeout_ms,
        )
        status_code = int(response.status) if response is not None else 0
        deadline = time.monotonic() + timeout_seconds
        last_text = ""
        last_diagnostics: ScorecardDiagnostics | None = None

        while time.monotonic() < deadline:
            last_text = self._page.locator("body").inner_text(timeout=5_000)
            last_diagnostics = scorecard_diagnostics(
                last_text,
                year=year,
                municipality=municipality,
            )
            if last_diagnostics.ready:
                return RenderedScorecard(
                    html=self._page.content(),
                    text=normalize_rendered_text(last_text),
                    final_url=self._page.url,
                    status_code=status_code,
                )
            self._page.wait_for_timeout(500)

        detail = "sem diagnóstico"
        if last_diagnostics is not None:
            detail = (
                f"rotulos={last_diagnostics.labels_present}, "
                f"rotulos_com_pontuacao={last_diagnostics.labels_with_score}, "
                f"indices={last_diagnostics.index_scores}, "
                f"candidatos={last_diagnostics.score_candidates}"
            )
        raise TimeoutError(
            f"LiveView não publicou o contrato numérico de {year} em "
            f"{timeout_seconds}s: {detail}"
        )

    def close(self) -> None:
        self._context.close()
        self._browser.close()
        self._playwright.stop()


def snapshot_published_ips_pages(
    snapshots_root: Path,
    *,
    snapshot_id: str = DEFAULT_SNAPSHOT_ID,
    years: tuple[int, ...] = DEFAULT_YEARS,
    ibge_code: str = DEFAULT_IBGE_CODE,
    municipality: str = DEFAULT_MUNICIPALITY,
    renderer: ScorecardRenderer | None = None,
    timeout_seconds: int = 90,
    max_total_bytes: int = 20_000_000,
) -> IpsWebSnapshotResult:
    """Captura o DOM renderizado e publica somente após todas as validações."""
    if not snapshot_id or "/" in snapshot_id or ".." in snapshot_id:
        raise ValueError("Identificador de snapshot inválido.")
    if not years or len(set(years)) != len(years):
        raise ValueError("Os anos devem ser únicos e não vazios.")
    if not municipality.strip():
        raise ValueError("O município deve ser informado.")
    if timeout_seconds <= 0 or max_total_bytes <= 0:
        raise ValueError("Timeout e limite de bytes devem ser maiores que zero.")

    root = snapshots_root.expanduser().resolve()
    final_path = root / snapshot_id
    partial_path = root / f".{snapshot_id}.partial"
    if final_path.exists() or partial_path.exists():
        raise FileExistsError(f"A captura já existe ou está incompleta: {snapshot_id}")

    active_renderer = renderer or PlaywrightScorecardRenderer()
    owns_renderer = renderer is None
    partial_path.mkdir(parents=True, exist_ok=False)
    manifest_rows: list[dict[str, object]] = []
    stored_bytes = 0

    try:
        for year in years:
            url = scorecard_url(year, ibge_code=ibge_code)
            rendered = active_renderer.render(
                url,
                year=year,
                ibge_code=ibge_code,
                municipality=municipality,
                timeout_seconds=timeout_seconds,
            )
            diagnostics = validate_rendered_scorecard(
                rendered,
                year=year,
                ibge_code=ibge_code,
                municipality=municipality,
            )
            html_bytes = rendered.html.encode("utf-8")
            text_bytes = rendered.text.encode("utf-8")
            stored_bytes += len(html_bytes) + len(text_bytes)
            if stored_bytes > max_total_bytes:
                raise ValueError(
                    "Captura bloqueada pelo limite: "
                    f"armazenado={stored_bytes}, limite={max_total_bytes}"
                )

            html_filename = f"ips_brasil_scorecard_{year}.html"
            text_filename = f"ips_brasil_scorecard_{year}.txt"
            (partial_path / html_filename).write_bytes(html_bytes)
            (partial_path / text_filename).write_bytes(text_bytes)
            manifest_rows.append(
                {
                    "reference_year": year,
                    "requested_url": url,
                    "final_url": rendered.final_url,
                    "status_code": rendered.status_code,
                    "capture_mode": "PLAYWRIGHT_RENDERED_LIVEVIEW_DOM",
                    "html_bytes": len(html_bytes),
                    "text_bytes": len(text_bytes),
                    "html_sha256": hashlib.sha256(html_bytes).hexdigest(),
                    "text_sha256": hashlib.sha256(text_bytes).hexdigest(),
                    "ibge_code": ibge_code,
                    "municipality": municipality,
                    "year_marker_confirmed": True,
                    "summary_labels_observed": diagnostics.labels_present,
                    "summary_labels_with_score": diagnostics.labels_with_score,
                    "score_candidates_observed": diagnostics.score_candidates,
                    "retrieved_at_utc": datetime.now(UTC).isoformat(),
                    "local_html_file": html_filename,
                    "local_text_file": text_filename,
                }
            )

        pd.DataFrame(manifest_rows).to_csv(
            partial_path / "web_manifest.csv",
            index=False,
        )
        final_path.parent.mkdir(parents=True, exist_ok=True)
        partial_path.replace(final_path)
    except Exception:
        shutil.rmtree(partial_path, ignore_errors=True)
        raise
    finally:
        if owns_renderer:
            active_renderer.close()

    return IpsWebSnapshotResult(
        snapshot_path=final_path,
        pages=len(manifest_rows),
        stored_bytes=stored_bytes,
        years=tuple(years),
        browser_navigations=len(manifest_rows),
    )
