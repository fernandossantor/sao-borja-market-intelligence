from pathlib import Path

import pandas as pd
import pytest

from sbmi.historical_integration_map import (
    HistoricalIntegrationMapResult,
    build_historical_integration_map,
    classify_candidate,
    name_similarity,
    normalize_file_stem,
    write_historical_integration_map,
)


def _inventory(rows: list[dict[str, object]]) -> pd.DataFrame:
    defaults = {
        "file_name": "",
        "extension": "xlsx",
        "is_folder": False,
        "size_bytes": 100,
        "sha256_checksum": "",
    }
    return pd.DataFrame([{**defaults, **row} for row in rows])


def _manifest(paths: list[tuple[str, str]]) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": path,
                "dataset": dataset,
                "disposition": "INCLUDED_IN_STAGING",
            }
            for path, dataset in paths
        ]
    )


def test_normalize_and_classify_exact_name() -> None:
    assert normalize_file_stem("Repasse Salário Educação Nacional.xlsx") == (
        "repasse salario educacao nacional"
    )
    similarities = name_similarity(
        "Repasse Salário Educação Nacional.xlsx",
        "REPASSE_SALARIO_EDUCACAO_NACIONAL.csv",
    )
    assert classify_candidate(
        source_sha256="",
        historical_sha256="",
        source_name="Repasse Salário Educação Nacional.xlsx",
        historical_name="REPASSE_SALARIO_EDUCACAO_NACIONAL.csv",
        similarities=similarities,
    ) == "EXACT_NORMALIZED_NAME"


def test_build_map_ranks_exact_hash_before_name_candidates() -> None:
    source = "raw/new_files/Federal/programa saude.xlsx"
    inventory = _inventory(
        [
            {
                "relative_path": source,
                "file_name": "programa saude.xlsx",
                "sha256_checksum": "a" * 64,
            },
            {
                "relative_path": "processed/programa saude.csv",
                "file_name": "programa saude.csv",
                "extension": "csv",
                "sha256_checksum": "b" * 64,
            },
            {
                "relative_path": "warehouse/copia binaria.parquet",
                "file_name": "copia binaria.parquet",
                "extension": "parquet",
                "sha256_checksum": "a" * 64,
            },
            {
                "relative_path": "exports/relatorio.pdf",
                "file_name": "relatorio.pdf",
                "extension": "pdf",
            },
        ]
    )
    result = build_historical_integration_map(
        inventory,
        _manifest([(source, "federal_transferencias")]),
        top_n=5,
    )

    candidates = result.candidates.sort_values("candidate_rank_for_source")
    assert list(candidates["candidate_class"]) == [
        "EXACT_SHA256",
        "EXACT_NORMALIZED_NAME",
    ]
    assert result.source_summary.loc[0, "mapping_status"] == "CANDIDATE_FOUND"
    summary = result.mapping_summary.set_index("indicator")
    assert int(summary.loc["exact_sha256_pairs", "value"]) == 1


def test_build_map_reports_source_without_metadata_candidate() -> None:
    source = "raw/new_files/Municipal/receita elemento.xlsx"
    inventory = _inventory(
        [
            {
                "relative_path": source,
                "file_name": "receita elemento.xlsx",
                "sha256_checksum": "c" * 64,
            },
            {
                "relative_path": "processed/populacao.csv",
                "file_name": "populacao.csv",
                "extension": "csv",
                "sha256_checksum": "d" * 64,
            },
        ]
    )
    result = build_historical_integration_map(
        inventory,
        _manifest([(source, "municipal_receita_elemento")]),
    )

    assert result.candidates.empty
    assert (
        result.source_summary.loc[0, "mapping_status"]
        == "NO_METADATA_CANDIDATE"
    )
    summary = result.mapping_summary.set_index("indicator")
    assert int(summary.loc["sources_without_candidates", "value"]) == 1


def test_write_mapping_is_atomic_and_refuses_overwrite(tmp_path: Path) -> None:
    result = HistoricalIntegrationMapResult(
        scope_summary=pd.DataFrame([{"scope": "processed", "files": 1}]),
        source_summary=pd.DataFrame([{"source_relative_path": "a.xlsx"}]),
        candidates=pd.DataFrame(),
        mapping_summary=pd.DataFrame(
            [
                {
                    "indicator": "active_staging_source_files",
                    "value": 1,
                    "nature": "observed",
                }
            ]
        ),
    )
    target = tmp_path / "mapping"
    written = write_historical_integration_map(result, target)

    assert written == target.resolve()
    assert (target / "historical_scope_summary.csv").is_file()
    assert (target / "staging_source_mapping_summary.csv").is_file()
    assert (target / "historical_integration_candidates.csv").is_file()
    assert (target / "historical_integration_summary.csv").is_file()
    with pytest.raises(FileExistsError):
        write_historical_integration_map(result, target)
