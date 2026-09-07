from urllib.parse import urlparse

from sbmi.vaf_source_audit import (
    VAF_ARCHIVE_URL,
    VAF_WRAPPER_URL,
    extract_iframe_sources,
    extract_official_links,
    extract_table_rows,
    find_table_rows_containing,
    official_source_catalog,
    parse_vaf_form,
    summarize_form,
)

FORM_HTML = """
<html><body>
<form method="post" action="AIM-WEB-VAL-HIS_2.asp">
  <input type="hidden" name="token" value="abc">
  <select name="anoIni" id="anoIni">
    <option value="2023">2023</option>
    <option value="2024" selected>2024</option>
  </select>
  <select name="municipio">
    <option value="117">SAO BORJA</option>
  </select>
  <input type="submit" name="consultar" value="Consultar">
</form>
</body></html>
"""

ARCHIVE_HTML = """
<html><body>
<a href="https://receita.fazenda.rs.gov.br/download/vaf0912.xls">
  Valor Adicionado Municipios - 2009 a 2012
</a>
<a href="https://receita.fazenda.rs.gov.br/download/layout2007.pdf">
  Layout Sistema Proprio - AIM 2007
</a>
<a href="https://example.com/other.xls">Valor Adicionado Municipios - externo</a>
<a href="https://receita.fazenda.rs.gov.br/download/other.pdf">Outro documento</a>
</body></html>
"""

WRAPPER_HTML = """
<html><body>
<iframe src="/ASP/SEF_ROOT/AIM/AIM-WEB-VAL-HIS_1.asp"></iframe>
<iframe src="https://example.com/foreign"></iframe>
</body></html>
"""

RESULT_HTML = """
<html><body>
<table>
  <tr><th>Município</th><th>Ano</th><th>Campo publicado</th></tr>
  <tr><td>São Borja</td><td>2025</td><td>1.234,56</td></tr>
  <tr><td>São José</td><td>2025</td><td>2.345,67</td></tr>
</table>
<table>
  <tr><td>Nota</td><td>Texto auxiliar</td></tr>
</table>
</body></html>
"""


def test_parse_vaf_form_preserves_observed_structure() -> None:
    structure = parse_vaf_form(FORM_HTML)
    assert structure.method == "post"
    assert structure.action.endswith("/AIM/AIM-WEB-VAL-HIS_2.asp")
    assert len(structure.selects) == 2
    assert structure.selects[0]["name"] == "anoIni"
    assert structure.selects[0]["options"][1]["selected"] is True
    assert structure.selects[1]["options"][0]["text"] == "SAO BORJA"
    assert structure.inputs[0]["type"] == "hidden"


def test_summarize_form_does_not_relabel_fields() -> None:
    summary = summarize_form(parse_vaf_form(FORM_HTML))
    assert summary["select_count"] == 2
    assert summary["selects"][0]["name"] == "anoIni"
    assert summary["nature"] == "observed_official_form_structure"


def test_parse_vaf_form_rejects_non_official_host() -> None:
    try:
        parse_vaf_form(FORM_HTML, source_url="https://example.com/form")
    except ValueError as exc:
        assert "não autorizado" in str(exc)
    else:
        raise AssertionError("Host não oficial deveria ser recusado")


def test_official_source_catalog_uses_only_rs_revenue_hosts() -> None:
    catalog = official_source_catalog()
    assert {item["source_id"] for item in catalog} == {
        "ipm_service_portal",
        "vaf_current_wrapper",
        "vaf_legacy_form",
        "vaf_historical_archive",
    }
    assert all(urlparse(item["url"]).hostname.endswith("rs.gov.br") for item in catalog)


def test_extract_official_archive_links_filters_text_and_host() -> None:
    links = extract_official_links(
        ARCHIVE_HTML,
        source_url=VAF_ARCHIVE_URL,
        text_terms=("Valor Adicionado Municipios", "Layout Sistema Proprio"),
    )
    assert len(links) == 2
    assert links[0]["text"] == "Valor Adicionado Municipios - 2009 a 2012"
    assert links[1]["text"] == "Layout Sistema Proprio - AIM 2007"
    assert all(urlparse(item["url"]).hostname == "receita.fazenda.rs.gov.br" for item in links)


def test_extract_iframe_sources_keeps_only_official_route() -> None:
    iframes = extract_iframe_sources(WRAPPER_HTML, source_url=VAF_WRAPPER_URL)
    assert iframes == (
        "https://www.sefaz.rs.gov.br/ASP/SEF_ROOT/AIM/AIM-WEB-VAL-HIS_1.asp",
    )


def test_extract_table_rows_preserves_visible_headers_and_cells() -> None:
    tables = extract_table_rows(RESULT_HTML)
    assert len(tables) == 2
    first_cells = tables[0][0]["cells"]
    assert first_cells == [
        {"tag": "th", "text": "Município"},
        {"tag": "th", "text": "Ano"},
        {"tag": "th", "text": "Campo publicado"},
    ]
    assert tables[0][1]["cells"][2]["text"] == "1.234,56"


def test_find_table_rows_containing_normalizes_accents() -> None:
    rows = find_table_rows_containing(RESULT_HTML, "SAO BORJA")
    assert len(rows) == 1
    assert rows[0]["table_index"] == 0
    assert [cell["text"] for cell in rows[0]["cells"]] == [
        "São Borja",
        "2025",
        "1.234,56",
    ]
