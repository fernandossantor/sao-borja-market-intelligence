import hashlib
from pathlib import Path

import duckdb
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from sbmi.derived_products_audit import (
    audit_derived_products_snapshot,
    write_derived_products_audit,
)


def _manifest_row(root: Path, relative_path: str) -> dict[str, object]:
    path = root / relative_path
    content = path.read_bytes()
    return {
        "drive_file_id": relative_path,
        "relative_path": relative_path,
        "scope": relative_path.split("/", 1)[0],
        "expected_size_bytes": len(content),
        "downloaded_size_bytes": len(content),
        "expected_sha256": hashlib.sha256(content).hexdigest(),
        "local_sha256": hashlib.sha256(content).hexdigest(),
        "verification_status": "VERIFIED",
    }


def _build_snapshot(root: Path) -> Path:
    parquet_path = root / "processed/agro/serie.parquet"
    parquet_path.parent.mkdir(parents=True)
    table = pa.table(
        {
            "municipio": ["São Borja", "São Borja"],
            "ano": [2023, 2024],
            "valor": [10.0, 12.0],
        }
    )
    pq.write_table(table, parquet_path)

    csv_path = root / "exports/resumo.csv"
    csv_path.parent.mkdir(parents=True)
    csv_path.write_text("municipio,ano,total\nSão Borja,2024,12\n", encoding="utf-8")

    json_path = root / "exports/metadata.json"
    json_path.write_text('{"fonte": "teste", "periodo": 2024}', encoding="utf-8")

    database_path = root / "warehouse/sao_borja.duckdb"
    database_path.parent.mkdir(parents=True)
    connection = duckdb.connect(str(database_path))
    connection.execute(
        "CREATE TABLE indicadores AS SELECT 'São Borja' municipio, 2024 ano, 12 valor"
    )
    connection.close()

    manifest = pd.DataFrame(
        [
            _manifest_row(root, "processed/agro/serie.parquet"),
            _manifest_row(root, "exports/resumo.csv"),
            _manifest_row(root, "exports/metadata.json"),
            _manifest_row(root, "warehouse/sao_borja.duckdb"),
        ]
    )
    manifest.to_csv(root / "snapshot_manifest.csv", index=False)
    return root


def test_audit_reads_parquet_csv_json_and_duckdb(tmp_path: Path) -> None:
    snapshot = _build_snapshot(tmp_path / "snapshot")
    result = audit_derived_products_snapshot(snapshot)

    summary = result.summary.set_index("indicator")
    assert int(summary.loc["snapshot_files", "value"]) == 4
    assert int(summary.loc["files_error", "value"]) == 0
    assert int(summary.loc["tables_observed", "value"]) == 4
    assert set(result.families["family"]) == {
        "exports",
        "processed/agro",
        "warehouse",
    }
    agro = result.tables.loc[result.tables["family"].eq("processed/agro")].iloc[0]
    assert bool(agro["geography_signal_estimate"])
    assert bool(agro["time_signal_estimate"])
    assert bool(agro["measure_signal_estimate"])
    assert agro["utility_estimate"] == "ANALYTICAL_SIGNAL_PRESENT"


def test_audit_reports_missing_local_file(tmp_path: Path) -> None:
    snapshot = tmp_path / "snapshot"
    snapshot.mkdir()
    pd.DataFrame(
        [
            {
                "relative_path": "processed/agro/missing.parquet",
                "scope": "processed",
                "local_sha256": "a" * 64,
                "downloaded_size_bytes": 10,
            }
        ]
    ).to_csv(snapshot / "snapshot_manifest.csv", index=False)

    result = audit_derived_products_snapshot(snapshot)
    assert result.files.loc[0, "read_status"] == "ERROR"
    assert result.files.loc[0, "error_type"] == "FileNotFoundError"


def test_audit_reports_exact_duplicates_as_observed_not_error(tmp_path: Path) -> None:
    snapshot = tmp_path / "snapshot"
    first = snapshot / "exports/a.csv"
    second = snapshot / "exports/b.csv"
    first.parent.mkdir(parents=True)
    content = "ano,valor\n2024,1\n"
    first.write_text(content, encoding="utf-8")
    second.write_text(content, encoding="utf-8")
    digest = hashlib.sha256(content.encode()).hexdigest()
    rows = []
    for path in (first, second):
        rows.append(
            {
                "relative_path": path.relative_to(snapshot).as_posix(),
                "scope": "exports",
                "local_sha256": digest,
                "downloaded_size_bytes": path.stat().st_size,
            }
        )
    pd.DataFrame(rows).to_csv(snapshot / "snapshot_manifest.csv", index=False)

    result = audit_derived_products_snapshot(snapshot)
    assert result.exact_duplicates["duplicate_group"].nunique() == 1
    assert len(result.exact_duplicates) == 2
    assert not result.files["read_status"].eq("ERROR").any()


def test_write_audit_is_atomic_and_refuses_overwrite(tmp_path: Path) -> None:
    result = audit_derived_products_snapshot(_build_snapshot(tmp_path / "snapshot"))
    target = tmp_path / "audit"
    written = write_derived_products_audit(result, target)
    assert written == target.resolve()
    assert (target / "derived_file_profile.csv").is_file()
    assert (target / "derived_family_summary.csv").is_file()
    with pytest.raises(FileExistsError):
        write_derived_products_audit(result, target)
