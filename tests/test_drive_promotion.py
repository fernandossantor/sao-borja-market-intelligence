from __future__ import annotations

import hashlib

import pytest

import sbmi.drive_promotion as promotion
from sbmi.drive_promotion import ExpectedDerivative, promote_derivatives, validate_local_derivatives


def test_validate_local_derivatives_checks_size_and_hash(tmp_path):
    path = tmp_path / "sample.csv"
    path.write_bytes(b"a,b\n1,2\n")
    expected = [
        ExpectedDerivative(
            "sample.csv",
            path.stat().st_size,
            hashlib.sha256(path.read_bytes()).hexdigest(),
        )
    ]

    validated = validate_local_derivatives(tmp_path, expected)
    assert validated["sample.csv"] == path

    bad = [ExpectedDerivative("sample.csv", path.stat().st_size, "0" * 64)]
    with pytest.raises(ValueError, match="SHA-256 divergente"):
        validate_local_derivatives(tmp_path, bad)


def test_promote_derivatives_reuses_matching_existing_file(tmp_path, monkeypatch):
    path = tmp_path / "sample.csv"
    path.write_bytes(b"a,b\n1,2\n")
    sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
    expected = [ExpectedDerivative("sample.csv", path.stat().st_size, sha256)]

    monkeypatch.setattr(
        promotion,
        "get_file_metadata",
        lambda session, file_id: {"id": file_id, "mimeType": promotion.FOLDER_MIME_TYPE},
    )
    monkeypatch.setattr(
        promotion,
        "list_children",
        lambda session, parent_id: [
            {
                "id": "existing-file-id",
                "name": "sample.csv",
                "size": str(path.stat().st_size),
                "sha256Checksum": sha256,
            }
        ],
    )
    monkeypatch.setattr(
        promotion,
        "_upload_one",
        lambda *args, **kwargs: pytest.fail("matching existing file must be reused"),
    )

    result = promote_derivatives(
        object(),
        output_dir=tmp_path,
        parent_folder_id="folder-id",
        expected=expected,
    )

    assert len(result) == 1
    assert result[0].drive_file_id == "existing-file-id"
    assert result[0].reused_existing is True
