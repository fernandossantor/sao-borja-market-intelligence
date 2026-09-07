"""Auditoria estrutural das fontes oficiais de VAF da Receita Estadual/RS."""

from __future__ import annotations

import unicodedata
from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

PORTAL_IPM_URL = "https://atendimento.receita.rs.gov.br/ipm-indice-de-participacao-dos-municipios"
VAF_WRAPPER_URL = "https://www.sefaz.rs.gov.br/AIM/VAL-HIS.aspx"
VAF_HISTORY_FORM_URL = (
    "https://www.sefaz.rs.gov.br/ASP/SEF_ROOT/AIM/AIM-WEB-VAL-HIS_1.asp"
)
VAF_HISTORY_RESULT_URL = (
    "https://www.sefaz.rs.gov.br/ASP/SEF_ROOT/AIM/AIM-WEB-VAL-HIS_2.asp"
)
VAF_ARCHIVE_URL = "https://atendimento.receita.rs.gov.br/consultas-e-arquivos-antigos-ipm"
VAF_ARCHIVE_2009_2012_XLS_URL = (
    "https://receita.fazenda.rs.gov.br/download/"
    "20161109101939valor_adicionado_municipios___2009_a_2012.xls"
)
VAF_ARCHIVE_1989_1997_XLS_URL = (
    "https://receita.fazenda.rs.gov.br/download/"
    "20161109101430valor_adicionado_municipios___1989_a_1997.xls"
)
VAF_LEGACY_DOWNLOAD_INDEX_URL = "https://www.sefaz.rs.gov.br/ASP/SEF_root/DWN/"
VAF_LEGACY_1989_1997_BINARY_URL = (
    "https://www.sefaz.rs.gov.br/ASP/Download/AIM/tabvalor.exe"
)
SAO_BORJA_RANGE_VALUE = "SAO MARTINHSZZZZZZZZZZ"
ALLOWED_HOSTS = {
    "atendimento.receita.rs.gov.br",
    "receita.fazenda.rs.gov.br",
    "sefaz.rs.gov.br",
    "www.sefaz.rs.gov.br",
}

SOURCE_CATALOG: tuple[dict[str, str], ...] = (
    {
        "source_id": "ipm_service_portal",
        "kind": "official_service_index",
        "url": PORTAL_IPM_URL,
        "nature": "observed_official_source_route",
    },
    {
        "source_id": "vaf_current_wrapper",
        "kind": "official_current_query_wrapper",
        "url": VAF_WRAPPER_URL,
        "nature": "observed_official_source_route",
    },
    {
        "source_id": "vaf_legacy_form",
        "kind": "official_legacy_query_form",
        "url": VAF_HISTORY_FORM_URL,
        "nature": "observed_official_source_route",
    },
    {
        "source_id": "vaf_historical_archive",
        "kind": "official_historical_archive_index",
        "url": VAF_ARCHIVE_URL,
        "nature": "observed_official_source_route",
    },
    {
        "source_id": "vaf_archive_2009_2012_xls",
        "kind": "official_historical_archive_attachment",
        "url": VAF_ARCHIVE_2009_2012_XLS_URL,
        "nature": "observed_official_published_attachment_route",
    },
    {
        "source_id": "vaf_archive_1989_1997_xls",
        "kind": "official_historical_archive_attachment",
        "url": VAF_ARCHIVE_1989_1997_XLS_URL,
        "nature": "observed_official_published_attachment_route",
    },
    {
        "source_id": "vaf_legacy_download_index",
        "kind": "official_legacy_download_index",
        "url": VAF_LEGACY_DOWNLOAD_INDEX_URL,
        "nature": "observed_official_source_route",
    },
    {
        "source_id": "vaf_legacy_1989_1997_binary",
        "kind": "official_legacy_binary_attachment",
        "url": VAF_LEGACY_1989_1997_BINARY_URL,
        "nature": "observed_official_published_attachment_route",
    },
)


@dataclass(frozen=True)
class FormStructure:
    """Estrutura mínima necessária para reproduzir uma submissão futura."""

    method: str
    action: str
    selects: tuple[dict[str, object], ...]
    inputs: tuple[dict[str, str], ...]


class _FormParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_form = False
        self.form_attrs: dict[str, str] = {}
        self.selects: list[dict[str, object]] = []
        self.inputs: list[dict[str, str]] = []
        self.current_select: dict[str, object] | None = None
        self.current_option: dict[str, object] | None = None
        self.option_text: list[str] = []

    @staticmethod
    def _attrs(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {key.lower(): value or "" for key, value in attrs}

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attr = self._attrs(attrs)
        tag = tag.lower()
        if tag == "form" and not self.in_form:
            self.in_form = True
            self.form_attrs = attr
        elif self.in_form and tag == "select":
            self.current_select = {
                "name": attr.get("name", ""),
                "id": attr.get("id", ""),
                "options": [],
            }
        elif self.in_form and tag == "option" and self.current_select is not None:
            self.current_option = {
                "value": attr.get("value", ""),
                "selected": "selected" in attr,
            }
            self.option_text = []
        elif self.in_form and tag == "input":
            self.inputs.append(
                {
                    "name": attr.get("name", ""),
                    "id": attr.get("id", ""),
                    "type": attr.get("type", "text").lower(),
                    "value": attr.get("value", ""),
                }
            )

    def handle_data(self, data: str) -> None:
        if self.current_option is not None:
            self.option_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "option" and self.current_option is not None:
            self.current_option["text"] = " ".join("".join(self.option_text).split())
            assert self.current_select is not None
            options = self.current_select["options"]
            assert isinstance(options, list)
            options.append(self.current_option)
            self.current_option = None
            self.option_text = []
        elif tag == "select" and self.current_select is not None:
            self.selects.append(self.current_select)
            self.current_select = None
        elif tag == "form" and self.in_form:
            self.in_form = False


class _RouteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[dict[str, str]] = []
        self.iframes: list[str] = []
        self.current_href: str | None = None
        self.current_text: list[str] = []

    @staticmethod
    def _attrs(attrs: list[tuple[str, str | None]]) -> dict[str, str]:
        return {key.lower(): value or "" for key, value in attrs}

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attr = self._attrs(attrs)
        tag = tag.lower()
        if tag == "a":
            self.current_href = attr.get("href", "")
            self.current_text = []
        elif tag == "iframe" and attr.get("src"):
            self.iframes.append(attr["src"])

    def handle_data(self, data: str) -> None:
        if self.current_href is not None:
            self.current_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self.current_href is not None:
            self.links.append(
                {
                    "href": self.current_href,
                    "text": " ".join("".join(self.current_text).split()),
                }
            )
            self.current_href = None
            self.current_text = []


class _TableParser(HTMLParser):
    """Captura texto visível de tabelas sem atribuir semântica posicional."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tables: list[list[dict[str, object]]] = []
        self.current_table: list[dict[str, object]] | None = None
        self.current_row: list[dict[str, str]] | None = None
        self.current_cell_tag: str | None = None
        self.current_cell_text: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        del attrs
        tag = tag.lower()
        if tag == "table" and self.current_table is None:
            self.current_table = []
        elif tag == "tr" and self.current_table is not None:
            self.current_row = []
        elif tag in {"th", "td"} and self.current_row is not None:
            self.current_cell_tag = tag
            self.current_cell_text = []

    def handle_data(self, data: str) -> None:
        if self.current_cell_tag is not None:
            self.current_cell_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"th", "td"} and self.current_cell_tag == tag:
            assert self.current_row is not None
            self.current_row.append(
                {
                    "tag": tag,
                    "text": " ".join("".join(self.current_cell_text).split()),
                }
            )
            self.current_cell_tag = None
            self.current_cell_text = []
        elif tag == "tr" and self.current_row is not None:
            assert self.current_table is not None
            if self.current_row:
                self.current_table.append({"cells": self.current_row})
            self.current_row = None
        elif tag == "table" and self.current_table is not None:
            self.tables.append(self.current_table)
            self.current_table = None


def _ensure_official_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.hostname not in ALLOWED_HOSTS:
        raise ValueError(f"Host VAF não autorizado: {parsed.hostname}")
    return url


def _normalized_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    without_marks = "".join(char for char in normalized if not unicodedata.combining(char))
    return " ".join(without_marks.casefold().split())


def official_source_catalog() -> tuple[dict[str, str], ...]:
    """Retorna apenas rotas oficiais explicitamente registradas no projeto."""
    for source in SOURCE_CATALOG:
        _ensure_official_url(source["url"])
    return SOURCE_CATALOG


def parse_vaf_form(html: str, *, source_url: str = VAF_HISTORY_FORM_URL) -> FormStructure:
    """Extrai método, action, selects e inputs sem inferir a semântica dos campos."""
    _ensure_official_url(source_url)

    parser = _FormParser()
    parser.feed(html)
    if not parser.form_attrs:
        raise ValueError("Formulário não encontrado na página VAF")

    method = parser.form_attrs.get("method", "get").lower()
    action = urljoin(source_url, parser.form_attrs.get("action", ""))
    _ensure_official_url(action)

    return FormStructure(
        method=method,
        action=action,
        selects=tuple(parser.selects),
        inputs=tuple(parser.inputs),
    )


def extract_official_links(
    html: str,
    *,
    source_url: str,
    text_terms: tuple[str, ...] = (),
) -> tuple[dict[str, str], ...]:
    """Extrai links oficiais, opcionalmente filtrados por termos do texto publicado."""
    _ensure_official_url(source_url)
    parser = _RouteParser()
    parser.feed(html)
    terms = tuple(term.casefold() for term in text_terms)
    results: list[dict[str, str]] = []
    for link in parser.links:
        text = link["text"]
        if terms and not any(term in text.casefold() for term in terms):
            continue
        url = urljoin(source_url, link["href"])
        try:
            _ensure_official_url(url)
        except ValueError:
            continue
        results.append({"text": text, "url": url})
    return tuple(results)


def extract_iframe_sources(html: str, *, source_url: str) -> tuple[str, ...]:
    """Extrai somente iframes hospedados em domínios oficiais autorizados."""
    _ensure_official_url(source_url)
    parser = _RouteParser()
    parser.feed(html)
    results: list[str] = []
    for iframe in parser.iframes:
        url = urljoin(source_url, iframe)
        try:
            _ensure_official_url(url)
        except ValueError:
            continue
        results.append(url)
    return tuple(results)


def extract_table_rows(html: str) -> tuple[tuple[dict[str, object], ...], ...]:
    """Extrai células de tabelas preservando apenas tag e texto visível."""
    parser = _TableParser()
    parser.feed(html)
    return tuple(tuple(row for row in table) for table in parser.tables)


def find_table_rows_containing(
    html: str,
    needle: str,
) -> tuple[dict[str, object], ...]:
    """Localiza linhas por texto normalizado, sem interpretar colunas ou valores."""
    target = _normalized_text(needle)
    matches: list[dict[str, object]] = []
    for table_index, table in enumerate(extract_table_rows(html)):
        for row_index, row in enumerate(table):
            cells = row["cells"]
            assert isinstance(cells, list)
            joined = " ".join(cell["text"] for cell in cells)
            if target in _normalized_text(joined):
                matches.append(
                    {
                        "table_index": table_index,
                        "row_index": row_index,
                        "cells": cells,
                    }
                )
    return tuple(matches)


def summarize_form(structure: FormStructure) -> dict[str, object]:
    """Gera resumo auditável sem atribuir significados não presentes no HTML."""
    return {
        "source_url": VAF_HISTORY_FORM_URL,
        "method": structure.method,
        "action": structure.action,
        "select_count": len(structure.selects),
        "input_count": len(structure.inputs),
        "selects": list(structure.selects),
        "inputs": list(structure.inputs),
        "nature": "observed_official_form_structure",
    }
