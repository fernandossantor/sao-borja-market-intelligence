from __future__ import annotations

import hashlib
import zipfile

import pytest

from sbmi.ipm_archive_audit import audit_ipm_archive, audit_results_table


def _zip(tmp_path, member_name="DAIM545X.TXT", payload=None):
    path = tmp_path / "ipm.zip"
    text = payload or "COD;MUNICIPIO;INDICE\n4318002;SÃO BORJA;0,533647\n"
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(member_name, text.encode("cp1252"))
        archive.writestr("DAIM545R.TXT", b"relatorio")
    return path


def test_audit_ipm_archive_finds_municipality_and_integrity(tmp_path):
    path = _zip(tmp_path)
    result = audit_ipm_archive(path, distribution_year=2026)

    assert result.distribution_year == 2026
    assert result.import_member == "DAIM545X.TXT"
    assert len(result.matched_lines) == 1
    assert "SÃO BORJA" in result.matched_lines[0]
    assert result.archive_bytes == path.stat().st_size
    assert result.archive_sha256 == hashlib.sha256(path.read_bytes()).hexdigest()

    table = audit_results_table([result])
    assert len(table) == 1
    assert table.iloc[0]["nature"] == "observed_official_archive_layout"


def test_audit_ipm_archive_requires_single_import_member(tmp_path):
    path = tmp_path / "bad.zip"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("DAIM545X_A.TXT", b"SAO BORJA")
        archive.writestr("DAIM545X_B.TXT", b"SAO BORJA")

    with pytest.raises(ValueError, match="exatamente um membro DAIM545X"):
        audit_ipm_archive(path, distribution_year=2026)


def test_audit_ipm_archive_requires_municipality(tmp_path):
    path = _zip(tmp_path, payload="COD;MUNICIPIO;INDICE\n1;OUTRO;0,1\n")
    with pytest.raises(ValueError, match="Município não localizado"):
        audit_ipm_archive(path, distribution_year=2026)
