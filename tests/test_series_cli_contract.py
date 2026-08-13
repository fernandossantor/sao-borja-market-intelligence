"""Contratos de segurança dos CLIs das séries territoriais."""

import importlib
import sys
from pathlib import Path

import pytest

from sbmi.canonical_territorial_model_series_cli import SERIES_ARGUMENTS, build_parser


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


def test_canonical_cli_requires_explicit_inputs():
    arguments = ["--base-root", "base"]
    for option in SERIES_ARGUMENTS.values():
        arguments.extend([option, option.removeprefix("--") + ".csv"])
    parsed = build_parser().parse_args(arguments)
    assert parsed.base_root == Path("base")
    assert parsed.demography_historical_path == Path("demography-historical-path.csv")


def test_canonical_cli_rejects_missing_inputs():
    with pytest.raises(SystemExit) as raised:
        build_parser().parse_args(["--base-root", "base"])
    assert raised.value.code == 2
