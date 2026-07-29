from pathlib import Path

import pandas as pd
import pytest

from sbmi.rais_lineage_audit import audit_rais_lineage, write_rais_lineage_audit


def _inputs(tmp_path: Path) -> tuple[Path, Path]:
    snapshot = tmp_path / "snapshot"
    raw = snapshot / "raw" / "rais"
    processed = tmp_path / "processed"
    raw.mkdir(parents=True)
    processed.mkdir()
    csv = pd.DataFrame({"Município - Código": [431800], "Valor": ["1,23"]})
    csv.to_csv(raw / "RAIS SB 2024.csv", index=False)
    pd.DataFrame({"municipio_codigo": [431800], "valor": [1.23]}).to_parquet(
        processed / "RAIS SB 2024.parquet", index=False
    )
    workbook = raw / "example.xlsx"
    pd.DataFrame([["Título", None], ["A", 1.23], ["B", "X"]]).to_excel(
        workbook, sheet_name="Tabela", index=False, header=False
    )
    pd.DataFrame(
        [["Título", None], ["A", 123], ["B", None]], columns=["col_0", "col_1"]
    ).to_parquet(processed / "example_Tabela.parquet", index=False)
    pd.DataFrame({"x": [1]}).to_parquet(processed / "orphan.parquet", index=False)
    (raw / "layout.xls").write_bytes(b"legacy")
    return snapshot, processed


def test_audit_confirms_and_blocks_pairs(tmp_path: Path) -> None:
    result = audit_rais_lineage(*_inputs(tmp_path))
    summary = result.summary.set_index("indicator")["value"]
    assert int(summary["content_equivalent_pairs"]) == 1
    assert int(summary["value_difference_pairs"]) == 1
    assert int(summary["decimal_separator_loss_cells"]) == 1
    assert int(summary["raw_value_lost_cells"]) == 1
    assert int(summary["unsupported_xls_files"]) == 1
    assert int(summary["unmatched_processed_files"]) == 1
    assert int(summary["promotion_allowed"]) == 0


def test_csv_pair_has_content_lineage_confirmed(tmp_path: Path) -> None:
    result = audit_rais_lineage(*_inputs(tmp_path))
    pair = result.pair_results.loc[result.pair_results["raw_file"].eq("RAIS SB 2024.csv")].iloc[0]
    assert pair["classification"] == "CONTENT_EQUIVALENT"
    assert pair["decision"] == "LINEAGE_CONTENT_CONFIRMED"


def test_write_is_atomic_and_refuses_overwrite(tmp_path: Path) -> None:
    result = audit_rais_lineage(*_inputs(tmp_path))
    target = tmp_path / "audit" / "run-1"
    assert write_rais_lineage_audit(result, target) == target.resolve()
    assert (target / "rais_lineage_manifest.csv").is_file()
    assert not (target.parent / ".run-1.partial").exists()
    with pytest.raises(FileExistsError):
        write_rais_lineage_audit(result, target)


def test_rejects_missing_inputs(tmp_path: Path) -> None:
    snapshot, processed = _inputs(tmp_path)
    for path in (snapshot / "raw" / "rais").iterdir():
        path.unlink()
    with pytest.raises(FileNotFoundError, match="Fontes raw/rais ausentes"):
        audit_rais_lineage(snapshot, processed)
