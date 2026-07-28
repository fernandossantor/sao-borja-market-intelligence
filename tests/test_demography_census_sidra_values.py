import json
from pathlib import Path

import pytest

from sbmi.demography_census_sidra_values import QUERIES, capture_sidra_values


class Resp:
    def __init__(self, data, *, content_type="application/json"):
        self.content = data if isinstance(data, bytes) else json.dumps(data).encode()
        self.status_code = 200
        self.headers = {"Content-Type": content_type}

    def raise_for_status(self):
        pass


class Session:
    def __init__(self):
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append(url)
        qid = next(k for k, v in QUERIES.items() if v == url)
        count = 3 if qid == "territory_4714" else 8
        head = {"V": "Valor"}
        rows = [
            {
                "D1C": "4318002",
                "D1N": "São Borja (RS)",
                "D2C": "2022",
                "D3C": str(i),
                "D3N": "Variável",
                "D4C": "",
                "D4N": "",
                "MN": "Unidade",
                "V": str(i),
            }
            for i in range(count)
        ]
        return Resp([head, *rows])


def run(tmp_path, s=None):
    return capture_sidra_values(
        s or Session(),
        snapshots_root=tmp_path / "snap",
        audit_root=tmp_path / "audit",
        snapshot_id="s",
        run_id="r",
    )


def test_captures_exact_queries_and_rows(tmp_path: Path):
    s = Session()
    r = run(tmp_path, s)
    assert s.calls == list(QUERIES.values())
    assert len(r.values) == 11
    assert set(r.values.municipality_code) == {"4318002"}


def test_atomic_and_no_overwrite(tmp_path: Path):
    r = run(tmp_path)
    assert (r.output_path / "sidra_observed_values.csv").is_file()
    with pytest.raises(FileExistsError):
        run(tmp_path)
    assert not (tmp_path / "snap" / ".s.partial").exists()
    assert not (tmp_path / "audit" / ".r.partial").exists()


def test_rejects_wrong_geography(tmp_path: Path):
    class Bad(Session):
        def get(self, url, **kwargs):
            response = super().get(url, **kwargs)
            data = json.loads(response.content)
            data[1]["D1C"] = "0"
            return Resp(data)

    with pytest.raises(ValueError, match="Geografia"):
        run(tmp_path, Bad())


@pytest.mark.parametrize(
    ("mutate", "message"),
    [
        (lambda data: data.__setitem__(1, {**data[1], "D2C": "2010"}), "período"),
        (lambda data: data[1].pop("V"), "Campos obrigatórios"),
        (lambda data: data.pop(), "Quantidade inesperada"),
    ],
)
def test_rejects_invalid_rows(tmp_path: Path, mutate, message):
    class Bad(Session):
        def get(self, url, **kwargs):
            response = super().get(url, **kwargs)
            data = json.loads(response.content)
            mutate(data)
            return Resp(data)

    with pytest.raises(ValueError, match=message):
        run(tmp_path, Bad())


@pytest.mark.parametrize(
    ("response", "message"),
    [
        (Resp(b""), "vazia"),
        (Resp(b"not-json"), "Expecting value"),
        (Resp([{"V": "Valor"}]), "Esquema"),
        (Resp([{"V": "Valor"}, {}], content_type="text/html"), "Tipo inesperado"),
    ],
)
def test_rejects_invalid_response(tmp_path: Path, response, message):
    class Bad(Session):
        def get(self, url, **kwargs):
            return response

    with pytest.raises((ValueError, json.JSONDecodeError), match=message):
        run(tmp_path, Bad())


def test_rejects_response_above_limit(tmp_path: Path):
    with pytest.raises(ValueError, match="acima do limite"):
        capture_sidra_values(
            Session(),
            snapshots_root=tmp_path / "snap",
            audit_root=tmp_path / "audit",
            snapshot_id="s",
            run_id="r",
            max_response_bytes=10,
        )


@pytest.mark.parametrize("identifier", ["", ".", "..", "nested/name"])
def test_rejects_unsafe_identifiers(tmp_path: Path, identifier):
    with pytest.raises(ValueError, match="identificador|nome simples"):
        capture_sidra_values(
            Session(),
            snapshots_root=tmp_path / "snap",
            audit_root=tmp_path / "audit",
            snapshot_id=identifier,
            run_id="r",
        )


def test_audit_collision_does_not_publish_snapshot(tmp_path: Path):
    (tmp_path / "audit" / "r").mkdir(parents=True)
    with pytest.raises(FileExistsError):
        run(tmp_path)
    assert not (tmp_path / "snap" / "s").exists()
    assert not (tmp_path / "snap" / ".s.partial").exists()
