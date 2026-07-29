from pathlib import Path

import pandas as pd
import pytest

from sbmi.rais_semantic_audit import (
    RAIS_EXPORTS,
    audit_rais_semantics,
    write_rais_semantic_audit,
)


def _snapshot(tmp_path: Path) -> Path:
    root = tmp_path / "snapshot"
    processed, exports = root / "processed" / "rais", root / "exports"
    processed.mkdir(parents=True)
    exports.mkdir()
    pd.DataFrame(
        {
            "municipio_codigo": [431800],
            "vl_rem_media_nom": ["R$ 1,23"],
            "municipio_trab_codigo_1": [999999],
        }
    ).to_parquet(processed / "RAIS SB 2024.parquet", index=False)
    layout = pd.DataFrame({"code": [1], "label": ["A"]})
    layout.to_parquet(processed / "RAIS_vinculos_layout_municipio.parquet", index=False)
    layout.to_parquet(processed / "RAIS_vinculos_layout2020_municipio.parquet", index=False)
    for name in RAIS_EXPORTS:
        frame = pd.DataFrame({"value": [1]})
        if name == "rais_semantic_mapping.csv":
            frame = pd.DataFrame(
                {
                    "column_name": ["A", "B"],
                    "economic_domain": ["unmapped", "employees"],
                }
            )
        elif name == "rais_historical_coverage.csv":
            frame = pd.DataFrame(
                {
                    "file_name": ["x.xlsx"],
                    "start_year": [2020],
                    "end_year": [2030],
                }
            )
        elif name == "rais_consolidated.csv":
            frame = pd.DataFrame({"mixed": ["text", "1"], "value": ["", "2"]})
        frame.to_csv(exports / name, index=False)
    return root


def test_audit_detects_blockers(tmp_path: Path) -> None:
    result = audit_rais_semantics(_snapshot(tmp_path), current_year=2026)
    summary = result.summary.set_index("indicator")["value"]
    assert int(summary["processed_files"]) == 3
    assert int(summary["exact_duplicate_groups"]) == 1
    assert int(summary["unmapped_semantic_rows"]) == 1
    assert int(summary["future_period_rows"]) == 1
    issues = result.issues.set_index("issue_class")
    assert int(issues.loc["MONETARY_COLUMNS_AS_TEXT", "affected_items"]) == 1
    assert int(summary["promotion_allowed"]) == 0


def test_roles_are_explicitly_name_only(tmp_path: Path) -> None:
    result = audit_rais_semantics(_snapshot(tmp_path), current_year=2026)
    inventory = result.processed_inventory.set_index("file_name")
    assert inventory.loc["RAIS SB 2024.parquet", "role_hint"] == "MICRODATA_CANDIDATE"
    assert set(inventory["role_evidence"]) == {"FILE_NAME_ONLY"}


def test_write_is_atomic_and_refuses_overwrite(tmp_path: Path) -> None:
    result = audit_rais_semantics(_snapshot(tmp_path), current_year=2026)
    target = tmp_path / "audit" / "run-1"
    assert write_rais_semantic_audit(result, target) == target.resolve()
    assert (target / "rais_semantic_manifest.csv").is_file()
    assert not (target.parent / ".run-1.partial").exists()
    with pytest.raises(FileExistsError):
        write_rais_semantic_audit(result, target)


def test_rejects_missing_export_contract(tmp_path: Path) -> None:
    root = _snapshot(tmp_path)
    (root / "exports" / "rais_semantic_mapping.csv").unlink()
    with pytest.raises(FileNotFoundError, match="Exports RAIS ausentes"):
        audit_rais_semantics(root)
