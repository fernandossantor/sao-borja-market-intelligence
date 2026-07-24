import hashlib
from pathlib import Path

import pandas as pd
import pytest

from sbmi.ips_web_snapshot import SUMMARY_LABELS
from sbmi.social_ips import (
    build_published_ips,
    extract_scorecard_summary,
    indicator_level,
    parse_published_number,
    write_published_ips,
)


def _rendered_text(year: int, index_score: str, *, fragmented: bool = False) -> str:
    score_value = index_score.replace(",", " , ") if fragmented else index_score
    menu = " ".join(SUMMARY_LABELS)
    sections = []
    for position, label in enumerate(SUMMARY_LABELS, start=1):
        score = f"{60 + position},{position % 10}"
        if fragmented:
            score = score.replace(",", " , ")
        sections.append(f"{label} posição {score}")
    return (
        f"{menu} São Borja IPS BRASIL {year} {score_value} "
        "pontuação de zero a cem "
        + " ".join(sections)
    )


def _snapshot(root: Path) -> Path:
    root.mkdir(parents=True)
    rows = []
    for year, score in ((2024, "59,10"), (2025, "61,38"), (2026, "62,40")):
        text = _rendered_text(year, score)
        html = (
            "<html><body>"
            f"<a href='/explore/scorecard/4318002?year={year}'>fonte</a>"
            f"<main>{text}</main></body></html>"
        )
        html_bytes = html.encode()
        text_bytes = text.encode()
        html_filename = f"ips_brasil_scorecard_{year}.html"
        text_filename = f"ips_brasil_scorecard_{year}.txt"
        (root / html_filename).write_bytes(html_bytes)
        (root / text_filename).write_bytes(text_bytes)
        rows.append(
            {
                "reference_year": year,
                "requested_url": f"https://example.test/scorecard/4318002?year={year}",
                "html_sha256": hashlib.sha256(html_bytes).hexdigest(),
                "text_sha256": hashlib.sha256(text_bytes).hexdigest(),
                "ibge_code": "4318002",
                "local_html_file": html_filename,
                "local_text_file": text_filename,
                "capture_mode": "PLAYWRIGHT_RENDERED_LIVEVIEW_DOM",
            }
        )
    pd.DataFrame(rows).to_csv(root / "web_manifest.csv", index=False)
    return root


def test_parses_brazilian_numbers_without_rounding() -> None:
    assert parse_published_number("1.234,56") == "1234.56"
    assert parse_published_number("61,38") == "61.38"
    assert parse_published_number("61 , 38") == "61.38"
    assert parse_published_number("1.234") == "1234"
    assert parse_published_number("-") is None


def test_classifies_structural_levels() -> None:
    assert indicator_level("Índice de Progresso Social") == "index"
    assert indicator_level("Necessidades Humanas Básicas") == "dimension"
    assert indicator_level("Água e Saneamento") == "component"
    with pytest.raises(ValueError, match="Rótulo agregado inesperado"):
        indicator_level("Indicador individual")


def test_extracts_rendered_scorecard_text() -> None:
    text = _rendered_text(2024, "59,10")
    result = extract_scorecard_summary(
        text,
        year=2024,
        ibge_code="4318002",
        municipality="São Borja",
        source_url="https://example.test/scorecard/4318002?year=2024",
        source_html_sha256="a" * 64,
        source_text_sha256=hashlib.sha256(text.encode()).hexdigest(),
    )

    assert len(result) == 16
    index = result.loc[result["indicator_level"].eq("index"), "value_numeric"].iloc[0]
    assert index == "59.10"
    assert result["value_numeric"].notna().all()


def test_extracts_scores_fragmented_in_rendered_text() -> None:
    text = _rendered_text(2024, "59,10", fragmented=True)
    result = extract_scorecard_summary(
        text,
        year=2024,
        ibge_code="4318002",
        municipality="São Borja",
        source_url="https://example.test/scorecard/4318002?year=2024",
        source_html_sha256="a" * 64,
        source_text_sha256=hashlib.sha256(text.encode()).hexdigest(),
    )

    assert len(result) == 16
    index = result.loc[result["indicator_level"].eq("index"), "value_numeric"].iloc[0]
    assert index == "59.10"
    assert result["value_numeric"].notna().all()


def test_builds_published_summaries_without_temporal_change(tmp_path: Path) -> None:
    result = build_published_ips(_snapshot(tmp_path / "snapshot"))

    assert set(result.published_summary_long["reference_year"]) == {2024, 2025, 2026}
    assert len(result.published_summary_long) == 48
    assert len(result.summary_2026) == 16
    assert result.metadata["capture_mode"] == "PLAYWRIGHT_RENDERED_LIVEVIEW_DOM"
    assert result.metadata["temporal_change_calculated"] is False
    assert (
        result.metadata["comparability_status"]
        == "NOT_STRICTLY_COMPARABLE_ACROSS_EDITIONS"
    )
    assert (
        result.metadata["individual_indicator_values_status"]
        == "NOT_PUBLISHED_AS_NUMERIC_VALUES_IN_RENDERED_SCORECARD"
    )
    current_index = result.summary_2026.loc[
        result.summary_2026["indicator_level"].eq("index"),
        "value_numeric",
    ].iloc[0]
    assert current_index == "62.40"


def test_rejects_html_hash_divergence(tmp_path: Path) -> None:
    snapshot = _snapshot(tmp_path / "snapshot")
    (snapshot / "ips_brasil_scorecard_2025.html").write_text("alterado")
    with pytest.raises(ValueError, match="HTML divergente"):
        build_published_ips(snapshot)


def test_rejects_text_hash_divergence(tmp_path: Path) -> None:
    snapshot = _snapshot(tmp_path / "snapshot")
    (snapshot / "ips_brasil_scorecard_2025.txt").write_text("alterado")
    with pytest.raises(ValueError, match="texto divergente"):
        build_published_ips(snapshot)


def test_write_is_atomic_and_refuses_overwrite(tmp_path: Path) -> None:
    result = build_published_ips(_snapshot(tmp_path / "snapshot"))
    output = tmp_path / "curated"
    written = write_published_ips(result, output)
    assert written == output.resolve()
    assert (output / "ips_published_summary_2024_2026.csv").is_file()
    assert (output / "ips_2026_summary.csv").is_file()
    assert (output / "ips_metadata.json").is_file()
    with pytest.raises(FileExistsError):
        write_published_ips(result, output)
