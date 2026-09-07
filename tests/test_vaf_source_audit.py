from __future__ import annotations

import pytest

from sbmi.vaf_source_audit import parse_vaf_form, summarize_form


HTML = """
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


def test_parse_vaf_form_preserves_observed_structure() -> None:
    structure = parse_vaf_form(HTML)
    assert structure.method == "post"
    assert structure.action.endswith("/AIM/AIM-WEB-VAL-HIS_2.asp")
    assert len(structure.selects) == 2
    assert structure.selects[0]["name"] == "anoIni"
    assert structure.selects[0]["options"][1]["selected"] is True
    assert structure.selects[1]["options"][0]["text"] == "SAO BORJA"
    assert structure.inputs[0]["type"] == "hidden"


def test_summarize_form_does_not_relabel_fields() -> None:
    summary = summarize_form(parse_vaf_form(HTML))
    assert summary["select_count"] == 2
    assert summary["selects"][0]["name"] == "anoIni"
    assert summary["nature"] == "observed_official_form_structure"


def test_parse_vaf_form_rejects_non_official_host() -> None:
    with pytest.raises(ValueError, match="não autorizado"):
        parse_vaf_form(HTML, source_url="https://example.com/form")
