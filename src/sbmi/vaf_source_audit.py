"""Auditoria estrutural da consulta histórica oficial de VAF da SEFAZ/RS."""

from __future__ import annotations

from dataclasses import dataclass
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

VAF_HISTORY_FORM_URL = (
    "https://www.sefaz.rs.gov.br/ASP/SEF_ROOT/AIM/AIM-WEB-VAL-HIS_1.asp"
)
ALLOWED_HOSTS = {"www.sefaz.rs.gov.br", "sefaz.rs.gov.br"}


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
            self.current_option["text"] = " ".join(
                "".join(self.option_text).split()
            )
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


def parse_vaf_form(html: str, *, source_url: str = VAF_HISTORY_FORM_URL) -> FormStructure:
    """Extrai método, action, selects e inputs sem inferir a semântica dos campos."""
    parsed_source = urlparse(source_url)
    if parsed_source.hostname not in ALLOWED_HOSTS:
        raise ValueError(f"Host VAF não autorizado: {parsed_source.hostname}")

    parser = _FormParser()
    parser.feed(html)
    if not parser.form_attrs:
        raise ValueError("Formulário não encontrado na página VAF")

    method = parser.form_attrs.get("method", "get").lower()
    action = urljoin(source_url, parser.form_attrs.get("action", ""))
    parsed_action = urlparse(action)
    if parsed_action.hostname not in ALLOWED_HOSTS:
        raise ValueError(f"Action VAF fora do host oficial: {action}")

    return FormStructure(
        method=method,
        action=action,
        selects=tuple(parser.selects),
        inputs=tuple(parser.inputs),
    )


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
