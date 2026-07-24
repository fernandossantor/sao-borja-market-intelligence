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
from sbmi.base_territorial_coverage_refinement import (
    refine_coverage_map,
    refine_files,
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


def test_refinement_excludes_technical_exports() -> None:
    inventory = _inventory(
        [
            {
                "relative_path": "exports/domain_coverage_summary.csv",
                "file_name": "domain_coverage_summary.csv",
                "extension": "csv",
            }
        ]
    )
    files = prepare_inventory(inventory)
    refined = refine_files(files).iloc[0]

    assert refined["primary_block"] == "governanca_documentacao"
    assert refined["classification_method"] == "EXPLICIT_NON_ANALYTICAL_ARTIFACT"
    assert not bool(refined["analytical_candidate"])


def test_refinement_maps_economic_and_labor_exports() -> None:
    inventory = _inventory(
        [
            {
                "relative_path": "exports/economic_factsheet.csv",
                "file_name": "economic_factsheet.csv",
                "extension": "csv",
            },
            {
                "relative_path": "exports/private_employment_calibrated.csv",
                "file_name": "private_employment_calibrated.csv",
                "extension": "csv",
            },
            {
                "relative_path": "processed/202601_servidores_siape/202601_Cadastro.parquet",
                "file_name": "202601_Cadastro.parquet",
                "extension": "parquet",
            },
        ]
    )
    refined = refine_files(prepare_inventory(inventory)).set_index("relative_path")

    assert (
        refined.loc[
            "exports/economic_factsheet.csv",
            "primary_block",
        ]
        == "economia_estrutura_produtiva"
    )
    assert (
        refined.loc[
            "exports/private_employment_calibrated.csv",
            "primary_block",
        ]
        == "renda_emprego_trabalho"
    )
    assert (
        refined.loc[
            "processed/202601_servidores_siape/202601_Cadastro.parquet",
            "primary_block",
        ]
        == "renda_emprego_trabalho"
    )


def test_institutional_review_separates_data_from_notes() -> None:
    inventory = _inventory(
        [
            {
                "relative_path": "raw/institucional/202601_Servidores_SIAPE/202601_Cadastro.csv",
                "file_name": "202601_Cadastro.csv",
                "extension": "csv",
            },
            {
                "relative_path": "raw/institucional/202601_Servidores_SIAPE/202601_Observacoes.csv",
                "file_name": "202601_Observacoes.csv",
                "extension": "csv",
            },
            {
                "relative_path": "processed/institucional/tabela5881_Tabela 1.parquet",
                "file_name": "tabela5881_Tabela 1.parquet",
                "extension": "parquet",
            },
            {
                "relative_path": "processed/institucional/tabela5881_Notas.parquet",
                "file_name": "tabela5881_Notas.parquet",
                "extension": "parquet",
            },
        ]
    )
    refined = refine_files(prepare_inventory(inventory)).set_index("relative_path")

    assert (
        refined.loc[
            "raw/institucional/202601_Servidores_SIAPE/202601_Cadastro.csv",
            "primary_block",
        ]
        == "renda_emprego_trabalho"
    )
    assert not bool(
        refined.loc[
            "raw/institucional/202601_Servidores_SIAPE/202601_Observacoes.csv",
            "analytical_candidate",
        ]
    )
    assert (
        refined.loc[
            "processed/institucional/tabela5881_Tabela 1.parquet",
            "primary_block",
        ]
        == "renda_emprego_trabalho"
    )
    assert not bool(
        refined.loc[
            "processed/institucional/tabela5881_Notas.parquet",
            "analytical_candidate",
        ]
    )


def test_reviewed_pdfs_receive_explicit_blocks() -> None:
    inventory = _inventory(
        [
            {
                "relative_path": "raw/pdfs/PlanoDiretorMAPA.pdf",
                "file_name": "PlanoDiretorMAPA.pdf",
                "extension": "pdf",
            },
            {
                "relative_path": "raw/pdfs/Sistema_motorizado.pdf",
                "file_name": "Sistema_motorizado.pdf",
                "extension": "pdf",
            },
            {
                "relative_path": "raw/pdfs/Plano_Municipal_de_Sade_2014_2017.pdf",
                "file_name": "Plano_Municipal_de_Sade_2014_2017.pdf",
                "extension": "pdf",
            },
            {
                "relative_path": "raw/pdfs/admin,+1.pdf",
                "file_name": "admin,+1.pdf",
                "extension": "pdf",
            },
        ]
    )
    refined = refine_files(prepare_inventory(inventory)).set_index("relative_path")

    assert (
        refined.loc["raw/pdfs/PlanoDiretorMAPA.pdf", "primary_block"]
        == "ambiente_politico_regulatorio"
    )
    assert (
        refined.loc["raw/pdfs/Sistema_motorizado.pdf", "primary_block"]
        == "infraestrutura_conectividade"
    )
    assert (
        refined.loc[
            "raw/pdfs/Plano_Municipal_de_Sade_2014_2017.pdf",
            "primary_block",
        ]
        == "saude_condicoes_sociais"
    )
    assert not bool(
        refined.loc["raw/pdfs/admin,+1.pdf", "analytical_candidate"]
    )
    assert (
        refined.loc["raw/pdfs/admin,+1.pdf", "primary_block"]
        == "fora_do_escopo_territorial"
    )


def test_dashboard_and_warehouse_are_not_independent_coverage() -> None:
    inventory = _inventory(
        [
            {
                "relative_path": "exports/dashboard_dataset.csv",
                "file_name": "dashboard_dataset.csv",
                "extension": "csv",
            },
            {
                "relative_path": "warehouse/sao_borja.duckdb",
                "file_name": "sao_borja.duckdb",
                "extension": "duckdb",
            },
        ]
    )
    refined = refine_files(prepare_inventory(inventory))

    assert not refined["analytical_candidate"].any()
    assert set(refined["primary_block"]) == {"governanca_documentacao"}


def test_refinement_recalculates_block_summary() -> None:
    inventory = _inventory(
        [
            {
                "relative_path": "exports/economic_factsheet.csv",
                "file_name": "economic_factsheet.csv",
                "extension": "csv",
            },
            {
                "relative_path": "exports/domain_signal_audit.csv",
                "file_name": "domain_signal_audit.csv",
                "extension": "csv",
            },
        ]
    )
    coarse = build_coverage_map(inventory)
    refined = refine_coverage_map(coarse, inventory)
    blocks = refined.block_summary.set_index("block")
    summary = refined.summary.set_index("indicator")

    assert int(
        blocks.loc[
            "economia_estrutura_produtiva",
            "candidate_files",
        ]
    ) == 1
    assert int(summary.loc["analytical_candidate_files", "value"]) == 1
    assert int(summary.loc["unclassified_candidate_files", "value"]) == 0


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
