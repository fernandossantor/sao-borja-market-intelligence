from pathlib import Path

import pytest

from sbmi.drive import normalize_remote_name, normalize_remote_path, remote_spec, snapshot_raw


def test_remote_spec_normalizes_name_and_path() -> None:
    assert remote_spec("sbmi-drive:", "/raw/new_files/") == "sbmi-drive:raw/new_files"


def test_remote_name_rejects_arbitrary_specification() -> None:
    with pytest.raises(ValueError):
        normalize_remote_name("sbmi-drive;rm -rf")


def test_remote_path_rejects_parent_navigation() -> None:
    with pytest.raises(ValueError):
        normalize_remote_path("raw/../exports")


def test_snapshot_rejects_existing_nonempty_target(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    target = tmp_path / "snapshot-1" / "raw"
    target.mkdir(parents=True)
    (target / "existing.txt").write_text("preservar", encoding="utf-8")

    monkeypatch.setattr("sbmi.drive.run_rclone", lambda _arguments: None)

    with pytest.raises(FileExistsError):
        snapshot_raw(
            remote="sbmi-drive",
            remote_path="raw",
            snapshots_root=tmp_path,
            snapshot_id="snapshot-1",
        )
