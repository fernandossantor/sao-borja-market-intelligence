"""CLI do perfil agregado dos recursos públicos estaduais."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.state_rs_public_funds_profile import profile_state_rs_public_funds


def main() -> None:
    snapshots = Path(".data/snapshots/web/state_rs_public_funds")
    candidates = sorted(path for path in snapshots.iterdir() if path.is_dir())
    if not candidates:
        raise FileNotFoundError("Nenhum snapshot estadual encontrado")
    run_id = datetime.now(UTC).strftime(
        "state-rs-public-funds-profile-%Y%m%d-%H%M%S"
    )
    result = profile_state_rs_public_funds(
        snapshot_path=candidates[-1],
        output_root=Path(
            ".data/audit/base_territorial/state_rs_public_funds_profile"
        ),
        run_id=run_id,
    )
    print(f"run_id={run_id}")
    print(f"csv_members={len(result.schema_profile)}")
    print(f"rows_scanned={int(result.schema_profile.rows_scanned.sum())}")
    print(f"matched_rows={int(result.territorial_summary.matched_rows.sum())}")
    print("sensitive_values_persisted=0")
    print("canonical_rows_promoted=0")
    print(f"audit={result.output_path}")


if __name__ == "__main__":
    main()
