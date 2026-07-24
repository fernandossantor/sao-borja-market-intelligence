import pandas as pd

from sbmi.base_territorial_coverage import build_coverage_map
from sbmi.base_territorial_coverage_refinement import refine_coverage_map
from sbmi.base_territorial_secondary_coverage import (
    apply_secondary_topic_coverage,
)


def _inventory(path: str) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": path,
                "file_name": path.rsplit("/", 1)[-1],
                "extension": path.rsplit(".", 1)[-1],
                "is_folder": False,
                "size_bytes": 100,
                "sha256_checksum": "a" * 64,
                "audit_status": "PENDING_AUDIT",
            }
        ]
    )


def test_secondary_topic_does_not_become_primary_source() -> None:
    inventory = _inventory(
        "raw/pdfs/São_Borja-Relatorio_Versão_Final.pdf"
    )
    result = build_coverage_map(inventory)
    result = refine_coverage_map(result, inventory)
    result = apply_secondary_topic_coverage(result, inventory)
    blocks = result.block_summary.set_index("block")

    assert int(blocks.loc["educacao", "candidate_files"]) == 1
    assert int(blocks.loc["educacao", "primary_candidate_files"]) == 0
    assert int(blocks.loc["educacao", "secondary_candidate_files"]) == 1
    assert (
        blocks.loc["educacao", "coverage_status"]
        == "SECONDARY_TOPIC_CANDIDATES_PRESENT"
    )


def test_primary_reviewed_raw_source_keeps_raw_status() -> None:
    inventory = _inventory("raw/pdfs/Sistema_motorizado.pdf")
    result = build_coverage_map(inventory)
    result = refine_coverage_map(result, inventory)
    result = apply_secondary_topic_coverage(result, inventory)
    blocks = result.block_summary.set_index("block")

    assert int(
        blocks.loc[
            "infraestrutura_conectividade",
            "primary_candidate_files",
        ]
    ) == 1
    assert (
        blocks.loc[
            "infraestrutura_conectividade",
            "coverage_status",
        ]
        == "RAW_SOURCES_PRESENT"
    )
