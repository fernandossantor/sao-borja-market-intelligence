from pathlib import Path

import pandas as pd
import pytest

from sbmi.complementary_semantic_audit import (
    audit_complementary_semantics,
    normalize_name,
)


def _inputs(tmp_path: Path) -> tuple[Path, Path, Path]:
    values = pd.DataFrame([
        {
            "source_id": "ips_brasil_explorer",
            "query_id": "ips_brasil_2024",
            "dimension": "saude_condicoes_sociais",
            "reference_year": "2024",
            "indicator_id": "",
            "field_name": "Índice de Progresso Social",
            "raw_value": "60,83",
            "numeric_value": "60.83",
        },
        {
            "source_id": "ips_brasil_explorer",
            "query_id": "ips_brasil_2024",
            "dimension": "saude_condicoes_sociais",
            "reference_year": "2024",
            "indicator_id": "",
            "field_name": "Homicídios",
            "raw_value": "10,00",
            "numeric_value": "10",
        },
        {
            "source_id": "sebrae_observatorio_profile",
            "query_id": "sebrae_candidate_001",
            "dimension": "renda_emprego_trabalho",
            "reference_year": "2022",
            "indicator_id": "",
            "field_name": "Year",
            "raw_value": "2022",
            "numeric_value": "2022",
        },
        {
            "source_id": "sebrae_observatorio_profile",
            "query_id": "sebrae_candidate_001",
            "dimension": "renda_emprego_trabalho",
            "reference_year": "2022",
            "indicator_id": "",
            "field_name": "Workers",
            "raw_value": "100",
            "numeric_value": "100",
        },
        {
            "source_id": "ibge_censo_2022_panorama",
            "query_id": "censo_2022_01",
            "dimension": "transversal_multitematico",
            "reference_year": "2022",
            "indicator_id": "96385",
            "field_name": "96385",
            "raw_value": "59676",
            "numeric_value": "59676",
        },
        {
            "source_id": "ibge_cidades_panorama",
            "query_id": "ibge_cidades_panorama_values",
            "dimension": "transversal_multitematico",
            "reference_year": "2022",
            "indicator_id": "96385",
            "field_name": "96385",
            "raw_value": "59676",
            "numeric_value": "59676",
        },
    ])
    values_path = tmp_path / "values.csv"
    values.to_csv(values_path, index=False)

    inventory = pd.DataFrame([{
        "query_id": "sebrae_candidate_001",
        "query_url": (
            "https://example.invalid/data?drilldowns=Year&measures=Workers"
        ),
        "overlap_classification": "PARTIAL_OVERLAP",
        "recommended_decision": "Comparar com os produtos RAIS locais auditados.",
    }])
    inventory_path = tmp_path / "inventory.csv"
    inventory.to_csv(inventory_path, index=False)

    ips_row = values.iloc[0].to_dict()
    extra_values = []
    baseline_rows = []
    for year in (2024, 2025, 2026):
        for number in range(16):
            label = (
                "Índice de Progresso Social"
                if number == 0
                else f"Agregado IPS {number:02d}"
            )
            value = 60.83 + number
            if not (year == 2024 and number == 0):
                extra_values.append(ips_row | {
                    "query_id": f"ips_brasil_{year}",
                    "reference_year": str(year),
                    "field_name": label,
                    "raw_value": str(value),
                    "numeric_value": str(value),
                })
            baseline_rows.append({
                "reference_year": str(year),
                "indicator_label": label,
                "indicator_key": normalize_name(label),
                "value_numeric": str(value),
            })
    values = pd.concat([values, pd.DataFrame(extra_values)], ignore_index=True)
    values.to_csv(values_path, index=False)
    baseline = pd.DataFrame(baseline_rows)
    baseline_path = tmp_path / "ips.csv"
    baseline.to_csv(baseline_path, index=False)
    return values_path, inventory_path, baseline_path


def test_normalize_name_is_accent_and_case_insensitive() -> None:
    assert normalize_name("Saúde e Bem-estar") == "saude_e_bem_estar"


def test_audit_classifies_without_promoting(tmp_path: Path) -> None:
    values, inventory, baseline = _inputs(tmp_path)
    result = audit_complementary_semantics(
        values_path=values,
        sebrae_inventory_path=inventory,
        ips_baseline_path=baseline,
        output_root=tmp_path / "audit",
        audit_id="audit-001",
    )
    def classifications(source: str, field: str) -> set[str]:
        selected = result.register.loc[
            result.register.source_id.eq(source)
            & result.register.field_name.eq(field),
            "classification",
        ]
        return set(selected)

    def decisions(source: str, field: str) -> set[str]:
        selected = result.register.loc[
            result.register.source_id.eq(source)
            & result.register.field_name.eq(field),
            "decision",
        ]
        return set(selected)

    ips_index = result.register.loc[
        result.register.source_id.eq("ips_brasil_explorer")
        & result.register.field_name.eq("Índice de Progresso Social"),
        "classification",
    ]
    assert len(ips_index) == 3
    assert ips_index.eq("CONTENT_DUPLICATE").all()
    assert len(result.ips_reconciliation) == 48
    assert classifications("ips_brasil_explorer", "Homicídios") == {
        "COMPLEMENTARY"
    }
    assert decisions("sebrae_observatorio_profile", "Year") == {
        "EXCLUDE_TECHNICAL_KEY"
    }
    assert classifications("sebrae_observatorio_profile", "Workers") == {
        "PARTIAL_OVERLAP"
    }
    assert classifications("ibge_cidades_panorama", "96385") == {
        "CONTENT_DUPLICATE"
    }
    assert int(result.validation.set_index("indicator").loc[
        "canonical_rows_promoted", "value"
    ]) == 0
    assert (result.output_path / "indicator_semantic_register.csv").is_file()


def test_audit_refuses_overwrite(tmp_path: Path) -> None:
    values, inventory, baseline = _inputs(tmp_path)
    kwargs = {
        "values_path": values,
        "sebrae_inventory_path": inventory,
        "ips_baseline_path": baseline,
        "output_root": tmp_path / "audit",
        "audit_id": "audit-001",
    }
    audit_complementary_semantics(**kwargs)
    with pytest.raises(FileExistsError):
        audit_complementary_semantics(**kwargs)
