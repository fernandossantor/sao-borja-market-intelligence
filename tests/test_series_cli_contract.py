"""Contratos de segurança dos CLIs das séries territoriais."""

import importlib
import sys

import pytest


@pytest.mark.parametrize(
    ("module_name", "builder_name"),
    [
        ("sbmi.business_employment_series_cli", "curate_business_employment_series"),
        ("sbmi.canonical_territorial_model_series_cli", "build_series_canonical_model"),
        ("sbmi.demography_census_series_cli", "collect_demography_census_series"),
        ("sbmi.demography_historical_values_cli", "collect_sidra_historical_values"),
        ("sbmi.economy_gdp_series_cli", "collect_economy_gdp_series"),
        ("sbmi.education_series_cli", "curate_education_series"),
    ],
)
def test_help_does_not_execute_pipeline(monkeypatch, module_name, builder_name):
    module = importlib.import_module(module_name)

    def unexpected_execution(*args, **kwargs):
        raise AssertionError("pipeline executado durante --help")

    monkeypatch.setattr(module, builder_name, unexpected_execution)
    monkeypatch.setattr(sys, "argv", [module_name, "--help"])
    with pytest.raises(SystemExit) as raised:
        module.main()
    assert raised.value.code == 0
