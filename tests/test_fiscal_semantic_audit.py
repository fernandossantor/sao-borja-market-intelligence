from pathlib import Path

import pandas as pd
import pytest

from sbmi.fiscal_semantic_audit import (
    audit_fiscal_semantics,
    write_fiscal_semantic_audit,
)

BUSINESS = [
    "mes_ano", "tipo", "tipo_de_favorecido", "uf", "nome_do_favorecido",
    "cpf_cnpj", "municipio", "funcao", "programa_orcamentario",
    "acao_orcamentaria", "linguagem_cidada", "valor_transferido",
]


def _federal(date: str, action: str, value: float, source: str) -> dict:
    return {
        "mes_ano": date, "tipo": "Tipo", "tipo_de_favorecido": "Público",
        "uf": "RS", "nome_do_favorecido": "São Borja", "cpf_cnpj": "1",
        "municipio": "SÃO BORJA", "funcao": "Função", "programa_orcamentario": "Programa",
        "acao_orcamentaria": action, "linguagem_cidada": "Sem informação",
        "valor_transferido": value, "_source_file": source,
    }


def _inputs(tmp_path: Path) -> tuple[Path, Path]:
    staging = tmp_path / "staging"
    historical = tmp_path / "historical"
    staging.mkdir()
    historical.mkdir()
    suspicious = (
        "ATENCAO A SAUDE DA POPULACAO PARA PROCEDIMENTOS EM MEDIA "
        "E ALTA COMPLEXIDADE.xlsx"
    )
    federal = pd.DataFrame([
        _federal("2020-02-01", "FPM", 10, suspicious),
        _federal("2026-01-01", "Nova", 20, "novo.xlsx"),
    ])
    federal.to_parquet(staging / "federal_transferencias.parquet", index=False)
    historical_row = pd.DataFrame([_federal("fev/20", "FPM", 10, "")])[BUSINESS]
    historical_row.to_parquet(historical / "a.parquet", index=False)
    historical_row.to_parquet(historical / "b.parquet", index=False)
    simple = {
        "estadual_transferencias": pd.DataFrame({"data": ["2024-01-01"], "valor": [1]}),
        "municipal_despesas_instituicao": pd.DataFrame({"instituicao": ["A"]}),
        "municipal_despesas_elemento": pd.DataFrame({"elemento": ["A"]}),
        "municipal_receita_elemento": pd.DataFrame({"instituicao": ["A"]}),
        "estadual_icms": pd.DataFrame({
            "data": ["2024-01-01"], "valor": [1], "descricao": ["IPVA"],
            "_duplicate_group_id": ["group-1"],
        }),
    }
    for name, frame in simple.items():
        frame.to_parquet(staging / f"{name}.parquet", index=False)
    return staging, historical


def test_audit_classifies_overlap_and_blockers(tmp_path: Path) -> None:
    staging, historical = _inputs(tmp_path)
    result = audit_fiscal_semantics(staging, historical)
    summary = result.summary.set_index("indicator")["value"]
    assert int(summary["federal_overlap_rows"]) == 1
    assert int(summary["federal_staging_only_rows"]) == 1
    assert int(summary["historical_duplicate_excess"]) == 1
    years = result.overlap_by_year.set_index("year")
    assert int(years["overlap_rows"].sum()) == int(summary["federal_overlap_rows"])
    assert years.loc[2020, "classification"] == "CONTENT_DUPLICATE"
    assert years.loc[2026, "classification"] == "UNIQUE"
    contracts = result.contracts.set_index("dataset")
    assert contracts.loc["estadual_icms", "promotion_blocker"] == (
        "PENDING_SOURCE_DUPLICATE_VALIDATION"
    )
    assert contracts.loc["estadual_transferencias", "promotion_blocker"] == (
        "EXPENDITURE_PHASE_SEPARATION_REQUIRED"
    )


def test_audit_detects_filename_content_mismatch(tmp_path: Path) -> None:
    result = audit_fiscal_semantics(*_inputs(tmp_path))
    issues = result.issues.set_index("issue_class")
    assert issues.loc["FILE_NAME_CONTENT_MISMATCH", "decision"] == (
        "DO_NOT_CLASSIFY_FROM_FILENAME"
    )
    assert "DATASET_NAME_CONTENT_MISMATCH" in issues.index


def test_write_is_atomic_and_refuses_overwrite(tmp_path: Path) -> None:
    result = audit_fiscal_semantics(*_inputs(tmp_path))
    target = tmp_path / "audit" / "run-1"
    assert write_fiscal_semantic_audit(result, target) == target.resolve()
    assert (target / "fiscal_semantic_manifest.csv").is_file()
    assert not (target.parent / ".run-1.partial").exists()
    with pytest.raises(FileExistsError):
        write_fiscal_semantic_audit(result, target)


def test_rejects_missing_staging_contract(tmp_path: Path) -> None:
    staging, historical = _inputs(tmp_path)
    (staging / "estadual_icms.parquet").unlink()
    with pytest.raises(FileNotFoundError, match="Staging ausente"):
        audit_fiscal_semantics(staging, historical)
