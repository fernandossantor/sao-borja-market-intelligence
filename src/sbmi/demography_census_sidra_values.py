"""Captura mínima e verificável de valores oficiais SIDRA para São Borja."""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

QUERIES = {
    "territory_4714": "https://apisidra.ibge.gov.br/values/t/4714/n6/4318002/p/2022/v/93,6318,614",
    "composition_9879": "https://apisidra.ibge.gov.br/values/t/9879/n6/4318002/p/2022/v/800,1000800/c460/12076,12077,12078,12079/c68/9902/c11561/100679/c12237/104570/c11562/72593",
}
EXPECTED_ROWS = {"territory_4714": 3, "composition_9879": 8}
REQUIRED_ROW_FIELDS = {"D1C", "D1N", "D2C", "D3C", "D3N", "MN", "V"}


@dataclass(frozen=True)
class ValuesResult:
    manifest: pd.DataFrame
    values: pd.DataFrame
    summary: pd.DataFrame
    snapshot_path: Path
    output_path: Path


def _atomic(root, ident):
    target = root.expanduser().resolve() / ident
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    partial.mkdir(parents=True)
    return target, partial


def _validate_identifier(ident, field):
    if not isinstance(ident, str) or not ident.strip():
        raise ValueError(f"{field} deve ser um identificador não vazio")
    if Path(ident).name != ident or ident in {".", ".."}:
        raise ValueError(f"{field} deve ser um nome simples")


def _fetch(session, qid, url, timeout, limit):
    response = session.get(
        url, timeout=timeout, headers={"User-Agent": "sbmi-sidra-values-snapshot/1.0"}
    )
    response.raise_for_status()
    content = bytes(response.content)
    if not content or len(content) > limit:
        raise ValueError(f"Resposta vazia ou acima do limite: {qid}")
    if "json" not in str(response.headers.get("Content-Type", "")).lower():
        raise ValueError(f"Tipo inesperado: {qid}")
    payload = json.loads(content)
    if not isinstance(payload, list) or len(payload) < 2:
        raise ValueError(f"Esquema SIDRA inválido: {qid}")
    rows = payload[1:]
    if len(rows) != EXPECTED_ROWS[qid]:
        raise ValueError(f"Quantidade inesperada de linhas: {qid}")
    for row in rows:
        if not isinstance(row, dict) or not REQUIRED_ROW_FIELDS.issubset(row):
            raise ValueError(f"Campos obrigatórios ausentes: {qid}")
        if row.get("D1C") != "4318002" or row.get("D2C") != "2022":
            raise ValueError(f"Geografia ou período divergente: {qid}")
    return content, rows, str(response.headers.get("Content-Type", "")), int(response.status_code)


def capture_sidra_values(
    session,
    *,
    snapshots_root,
    audit_root,
    snapshot_id,
    run_id,
    timeout_seconds=30.0,
    max_response_bytes=100_000,
):
    if timeout_seconds <= 0 or max_response_bytes <= 0:
        raise ValueError("Timeout e limite devem ser positivos")
    _validate_identifier(snapshot_id, "snapshot_id")
    _validate_identifier(run_id, "run_id")
    fetched = {
        qid: _fetch(session, qid, url, timeout_seconds, max_response_bytes)
        for qid, url in QUERIES.items()
    }
    sp, partial = _atomic(snapshots_root, snapshot_id)
    try:
        op, audit_partial = _atomic(audit_root, run_id)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    manifest = []
    try:
        for qid, (content, rows, ctype, status) in sorted(fetched.items()):
            name = f"{qid}.json"
            (partial / name).write_bytes(content)
            manifest.append(
                {
                    "query_id": qid,
                    "url": QUERIES[qid],
                    "status_code": status,
                    "content_type": ctype,
                    "rows": len(rows),
                    "bytes": len(content),
                    "sha256": hashlib.sha256(content).hexdigest(),
                    "local_file": name,
                    "nature": "observed",
                }
            )
        manifest = pd.DataFrame(manifest)
        manifest.to_csv(partial / "sidra_values_manifest.csv", index=False)
        sp.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(sp)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        shutil.rmtree(audit_partial, ignore_errors=True)
        raise
    records = []
    for qid, (_, rows, _, _) in fetched.items():
        for row in rows:
            records.append(
                {
                    "query_id": qid,
                    "municipality_code": row["D1C"],
                    "municipality_name": row["D1N"],
                    "period": row["D2C"],
                    "variable_id": row["D3C"],
                    "variable_name": row["D3N"],
                    "category_id": row.get("D4C", ""),
                    "category_name": row.get("D4N", ""),
                    "unit": row["MN"],
                    "value_text": row["V"],
                    "nature": "observed",
                }
            )
    values = pd.DataFrame(records)
    summary = pd.DataFrame(
        [
            ("responses_captured", 2, "observed"),
            ("value_rows", len(values), "calculated"),
            ("municipality_codes", values.municipality_code.nunique(), "calculated"),
            ("periods", values.period.nunique(), "calculated"),
        ],
        columns=["indicator", "value", "nature"],
    )
    try:
        values.to_csv(audit_partial / "sidra_observed_values.csv", index=False)
        summary.to_csv(audit_partial / "sidra_values_summary.csv", index=False)
        op.parent.mkdir(parents=True, exist_ok=True)
        audit_partial.replace(op)
    except Exception:
        shutil.rmtree(audit_partial, ignore_errors=True)
        raise
    return ValuesResult(manifest, values, summary, sp, op)
