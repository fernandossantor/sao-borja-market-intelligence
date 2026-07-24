from pathlib import Path

import pandas as pd
import pytest

from sbmi.base_territorial_coverage import (
    build_coverage_map,
    classify_path,
    detect_local_module_evidence,
    prepare_inventory,
    write_coverage_map,
)


def _inventory(rows: list[dict[str, object]]) -> pd.DataFrame:
    defaults = {
        "file_name": "",
        "extension": "xlsx",
        "is_folder": False,
        "size_bytes": 100,
        "sha256_checksum": "a" * 64,
        "audit_status": "PENDING_AUDIT",
    }
    return pd.DataFrame([{**defaults, **row} for row in rows])


def test_raw_new_files_is_explicit_public_finance_coverage() -> None:
    classification = classify_path(
        "raw/new_files/Federal/TRANSFERENCIA PARA SAUDE.xlsx"
    )

    assert (
        classification["primary_block"]
        == "financas_publicas_transferencias"
    )
    assert classification["classification_method"] == "EXPLICIT_PATH_OVERRIDE"
    assert classification["classification_confidence"] == "HIGH"


def test_prepare_inventory_excludes_governance_from_analytical_candidates() -> None:
    inventory = _inventory(
        [
            {
                "relative_path": "governance/Memória de situação.docx",
                "file_name": "Memória de situação.docx",
                "extension": "docx",
            },
            {
                "relative_path": "processed/demografia/populacao.csv",
                "file_name": "populacao.csv",
                "extension": "csv",
            },
        ]
    )

    files = prepare_inventory(inventory).set_index("relative_path")

    assert not bool(
        files.loc[
            "governance/Memória de situação.docx",
            "analytical_candidate",
        ]
    )
    assert (
        files.loc[
            "processed/demografia/populacao.csv",
            "primary_block",
        ]
        == "demografia"
    )


def test_build_map_preserves_validated_finance_staging_and_local_modules(
    tmp_path: Path,
) -> None:
    inventory = _inventory(
        [
            {
                "relative_path": "raw/new_files/Estadual/icms.xlsx",
                "file_name": "icms.xlsx",
            },
            {
                "relative_path": "processed/demografia/populacao.csv",
                "file_name": "populacao.csv",
                "extension": "csv",
            },
        ]
    )
    manifest = pd.DataFrame(
        [
            {
                "relative_path": "raw/new_files/Estadual/icms.xlsx",
                "dataset": "estadual_icms",
                "output_rows": 3818,
                "disposition": "INCLUDED_IN_STAGING",
            }
        ]
    )
    validation = pd.DataFrame(
        [
            {
                "dataset": "estadual_icms",
                "rows": 3818,
                "source_files": 1,
                "date_min": "2024-01-01",
                "date_max": "2024-12-31",
                "duplicate_flagged_rows": 29,
                "status": "OK",
            }
        ]
    )
    curated_root = tmp_path / "curated"
    (curated_root / "social/idsc").mkdir(parents=True)
    (curated_root / "social/idsc/factsheet.csv").write_text(
        "indicator,value\nscore,1\n",
        encoding="utf-8",
    )
    (curated_root / "social/ips").mkdir(parents=True)
    (curated_root / "social/ips/summary.csv").write_text(
        "indicator,value\nscore,1\n",
        encoding="utf-8",
    )

    result = build_coverage_map(
        inventory,
        manifest=manifest,
        dataset_validation=validation,
        local_modules=detect_local_module_evidence(curated_root),
    )
    blocks = result.block_summary.set_index("block")
    evidence = result.evidence_register.set_index("evidence_id")

    assert (
        blocks.loc[
            "financas_publicas_transferencias",
            "coverage_status",
        ]
        == "STAGING_VALIDATED_PRESENT"
    )
    assert int(
        blocks.loc[
            "financas_publicas_transferencias",
            "validated_staging_datasets",
        ]
    ) == 1
    assert (
        evidence.loc[
            "staging:estadual_icms",
            "validation_status",
        ]
        == "STRUCTURAL_VALIDATION_OK"
    )
    assert "29 linhas" in evidence.loc[
        "staging:estadual_icms",
        "limitation",
    ]
    assert (
        blocks.loc["saude_condicoes_sociais", "coverage_status"]
        == "CURATED_VALIDATED_PRESENT"
    )
    assert (
        blocks.loc["transversal_multitematico", "coverage_status"]
        == "CURATED_VALIDATED_PRESENT"
    )


def test_derived_products_remain_structural_evidence_only() -> None:
    inventory = _inventory(
        [
            {
                "relative_path": "processed/economia/pib.csv",
                "file_name": "pib.csv",
                "extension": "csv",
            }
        ]
    )
    families = pd.DataFrame(
        [
            {
                "family": "processed/economia",
                "files": 2,
                "tables": 2,
                "rows_observed": 100,
                "family_status": "OK",
            }
        ]
    )

    result = build_coverage_map(inventory, derived_families=families)
    evidence = result.evidence_register.iloc[0]
    blocks = result.block_summary.set_index("block")

    assert evidence["layer"] == "historical_derived_product"
    assert evidence["validation_status"] == "STRUCTURAL_AUDIT_OK"
    assert "não validade metodológica" in evidence["limitation"]
    assert (
        blocks.loc[
            "economia_estrutura_produtiva",
            "coverage_status",
        ]
        == "DERIVED_PRODUCTS_AUDITED_PRESENT"
    )


def test_write_coverage_map_is_atomic_and_refuses_overwrite(
    tmp_path: Path,
) -> None:
    inventory = _inventory(
        [
            {
                "relative_path": "raw/new_files/Municipal/receita.xlsx",
                "file_name": "receita.xlsx",
            }
        ]
    )
    result = build_coverage_map(inventory)
    target = tmp_path / "coverage"

    written = write_coverage_map(result, target)

    assert written == target.resolve()
    assert (target / "coverage_file_inventory.csv").is_file()
    assert (target / "coverage_source_family_summary.csv").is_file()
    assert (target / "coverage_evidence_register.csv").is_file()
    assert (target / "coverage_block_summary.csv").is_file()
    assert (target / "coverage_gap_register.csv").is_file()
    assert (target / "coverage_map_summary.csv").is_file()
    with pytest.raises(FileExistsError):
        write_coverage_map(result, target)
