import hashlib
from pathlib import Path

import pandas as pd
import pytest

from sbmi.social_ips import (
    build_published_ips,
    indicator_level,
    parse_published_number,
    write_published_ips,
)


def _html(score: str) -> bytes:
    return (
        "<html><body><table id='data'>"
        "<thead><tr>"
        "<th>Código IBGE</th><th>Município</th><th>UF</th>"
        "<th>Índice de Progresso Social</th>"
        "<th>Necessidades Humanas Básicas</th>"
        "<th>Água e Saneamento</th>"
        "<th>Indicador Exemplo</th>"
        "</tr></thead>"
        "<tbody><tr>"
        "<td>4318002</td><td><span>São Borja (RS)</span></td><td>RS</td>"
        f"<td>{score}</td><td>70,25</td><td>80,10</td><td>1.234,56</td>"
        "</tr></tbody></table></body></html>"
    ).encode()


def _snapshot(root: Path) -> Path:
    root.mkdir(parents=True)
    rows = []
    for year, score in ((2024, "59,10"), (2025, "61,38"), (2026, "62,40")):
        content = _html(score)
        filename = f"ips_brasil_published_{year}.html"
        (root / filename).write_bytes(content)
        rows.append(
            {
                "reference_year": year,
                "requested_url": f"https://example.test/data?year={year}",
                "sha256": hashlib.sha256(content).hexdigest(),
                "ibge_code": "4318002",
                "local_file": filename,
            }
        )
    pd.DataFrame(rows).to_csv(root / "web_manifest.csv", index=False)
    return root


def test_parses_brazilian_numbers_without_rounding() -> None:
    assert parse_published_number("1.234,56") == "1234.56"
    assert parse_published_number("61,38") == "61.38"
    assert parse_published_number("1.234") == "1234"
    assert parse_published_number("-") is None


def test_classifies_structural_levels() -> None:
    assert indicator_level("Índice de Progresso Social") == "index"
    assert indicator_level("Necessidades Humanas Básicas") == "dimension"
    assert indicator_level("Água e Saneamento") == "component"
    assert indicator_level("Indicador Exemplo") == "indicator"


def test_builds_published_profiles_without_temporal_change(tmp_path: Path) -> None:
    result = build_published_ips(_snapshot(tmp_path / "snapshot"))

    assert set(result.published_long["reference_year"]) == {2024, 2025, 2026}
    assert len(result.profile_2026) == 7
    assert len(result.summary_2026) == 3
    assert result.metadata["temporal_change_calculated"] is False
    assert (
        result.metadata["comparability_status"]
        == "NOT_STRICTLY_COMPARABLE_ACROSS_EDITIONS"
    )
    current_index = result.summary_2026.loc[
        result.summary_2026["indicator_level"].eq("index"),
        "value_numeric",
    ].iloc[0]
    assert current_index == "62.40"


def test_rejects_hash_divergence(tmp_path: Path) -> None:
    snapshot = _snapshot(tmp_path / "snapshot")
    (snapshot / "ips_brasil_published_2025.html").write_text("alterado")
    with pytest.raises(ValueError, match="SHA-256 divergente"):
        build_published_ips(snapshot)


def test_write_is_atomic_and_refuses_overwrite(tmp_path: Path) -> None:
    result = build_published_ips(_snapshot(tmp_path / "snapshot"))
    output = tmp_path / "curated"
    written = write_published_ips(result, output)
    assert written == output.resolve()
    assert (output / "ips_2026_summary.csv").is_file()
    assert (output / "ips_metadata.json").is_file()
    with pytest.raises(FileExistsError):
        write_published_ips(result, output)
