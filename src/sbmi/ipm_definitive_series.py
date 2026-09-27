"""Série canônica de IPM definitivo de São Borja a partir dos arquivos oficiais."""

from __future__ import annotations

import re
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path

import pandas as pd

from sbmi.ipm_archive_audit import IpmArchiveAuditResult, audit_ipm_archive
from sbmi.ipm_definitive_sources import IPM_DEFINITIVE_ARCHIVE_URLS

IPM_FINAL_PATTERN = re.compile(r"(?P<value>\d+,\d{6})\s*$")
EXPECTED_YEARS = tuple(range(2003, 2027))
EXPECTED_BENCHMARKS = {2025: Decimal("0.527880"), 2026: Decimal("0.533647")}


@dataclass(frozen=True)
class IpmSeriesOutputs:
    """Tabelas derivadas de uma execução canônica de IPM definitivo."""

    series: pd.DataFrame
    validation: pd.DataFrame
    source_manifest: pd.DataFrame
    run_metadata: pd.DataFrame


def parse_final_ipm(raw_line: str) -> Decimal:
    """Extrai somente o último campo de seis casas do DAIM545X."""
    match = IPM_FINAL_PATTERN.search(str(raw_line))
    if match is None:
        raise ValueError("Linha municipal não termina com IPM decimal de seis casas")
    try:
        value = Decimal(match.group("value").replace(",", "."))
    except InvalidOperation as exc:
        raise ValueError("IPM final inválido") from exc
    if not Decimal("0") < value < Decimal("100"):
        raise ValueError(f"IPM fora da faixa plausível: {value}")
    return value


def _validation_row(indicator: str, value: object, passed: bool) -> dict[str, object]:
    return {"indicator": indicator, "value": value, "status": "PASS" if passed else "FAIL"}


def _build_validation(series: pd.DataFrame) -> pd.DataFrame:
    years = series["distribution_year"].astype(int).tolist()
    unique_years = sorted(set(years))
    ipm = series.set_index("distribution_year")["ipm_definitive"].to_dict()
    rows = [
        _validation_row("rows", len(series), len(series) == len(EXPECTED_YEARS)),
        _validation_row(
            "unique_years",
            len(unique_years),
            len(unique_years) == len(EXPECTED_YEARS),
        ),
        _validation_row(
            "year_range_complete",
            f"{min(years)}-{max(years)}",
            tuple(years) == EXPECTED_YEARS,
        ),
        _validation_row(
            "municipality_match_exactly_one_per_year",
            int(series["municipality_match_count"].sum()),
            bool((series["municipality_match_count"] == 1).all()),
        ),
        _validation_row(
            "ipm_positive",
            int((series["ipm_definitive"] > 0).sum()),
            bool((series["ipm_definitive"] > 0).all()),
        ),
    ]
    for year, expected in EXPECTED_BENCHMARKS.items():
        observed = Decimal(f"{float(ipm[year]):.6f}")
        rows.append(
            _validation_row(
                f"benchmark_{year}",
                f"{observed:.6f}",
                observed == expected,
            )
        )
    return pd.DataFrame(rows)


def build_ipm_series_from_audits(
    results: list[IpmArchiveAuditResult],
    *,
    execution_id: str,
    municipality: str = "São Borja",
) -> IpmSeriesOutputs:
    """Constrói a série definitiva sem interpretar componentes internos do leiaute."""
    rows: list[dict[str, object]] = []
    manifest_rows: list[dict[str, object]] = []

    for result in sorted(results, key=lambda item: item.distribution_year):
        if len(result.matched_lines) != 1:
            raise ValueError(
                f"Ano {result.distribution_year}: esperado um único match municipal; "
                f"observado={len(result.matched_lines)}"
            )
        value = parse_final_ipm(result.matched_lines[0])
        rows.append(
            {
                "distribution_year": result.distribution_year,
                "geography": "São Borja/RS",
                "municipality": municipality,
                "ipm_definitive": float(value),
                "ipm_definitive_text": f"{value:.6f}",
                "yoy_change_pct": pd.NA,
                "nature_ipm": "observed_official_definitive",
                "nature_yoy": "calculated",
                "source_scope": "Receita Estadual/RS — IPM Definitivos — DAIM545X",
                "archive_file": result.archive_path.name,
                "archive_sha256": result.archive_sha256,
                "archive_bytes": result.archive_bytes,
                "import_member": result.import_member,
                "encoding": result.encoding,
                "municipality_match_count": len(result.matched_lines),
            }
        )
        manifest_rows.append(
            {
                "distribution_year": result.distribution_year,
                "source_url": IPM_DEFINITIVE_ARCHIVE_URLS[result.distribution_year],
                "archive_file": result.archive_path.name,
                "archive_bytes": result.archive_bytes,
                "archive_sha256": result.archive_sha256,
                "import_member": result.import_member,
                "encoding": result.encoding,
                "nature": "observed_official_source",
            }
        )

    series = pd.DataFrame(rows).sort_values("distribution_year").reset_index(drop=True)
    if not series.empty:
        series["yoy_change_pct"] = series["ipm_definitive"].pct_change() * 100.0

    validation = _build_validation(series)
    failed = validation.loc[validation["status"] != "PASS"]
    if not failed.empty:
        raise ValueError(f"Validações IPM falharam: {failed.to_dict(orient='records')}")

    source_manifest = pd.DataFrame(manifest_rows).sort_values("distribution_year")
    run_metadata = pd.DataFrame(
        [
            {"field": "execution_id", "value": execution_id, "nature": "parameter"},
            {"field": "geography", "value": "São Borja/RS", "nature": "parameter"},
            {
                "field": "distribution_years",
                "value": "2003-2026",
                "nature": "observed_source_period",
            },
            {
                "field": "source",
                "value": "Receita Estadual/RS — IPM Definitivos — DAIM545X",
                "nature": "observed_source",
            },
            {
                "field": "extraction_rule",
                "value": (
                    "último campo da linha única de São Borja em DAIM545X; "
                    "seis casas decimais"
                ),
                "nature": "method",
            },
            {
                "field": "layout_rule",
                "value": (
                    "componentes intermediários não interpretados porque o número "
                    "de campos muda entre anos"
                ),
                "nature": "limitation",
            },
            {
                "field": "comparability",
                "value": (
                    "IPM é comparável como índice final publicado; pesos e critérios "
                    "legais mudam ao longo do tempo"
                ),
                "nature": "limitation",
            },
        ]
    )
    return IpmSeriesOutputs(series, validation, source_manifest, run_metadata)


def build_ipm_series_from_archives(
    archive_root: Path,
    *,
    execution_id: str,
    municipality: str = "São Borja",
) -> IpmSeriesOutputs:
    """Audita os 24 arquivos e constrói a série definitiva canônica."""
    root = Path(archive_root)
    results = [
        audit_ipm_archive(
            root / f"ipm_{year}.zip",
            distribution_year=year,
            municipality=municipality,
        )
        for year in EXPECTED_YEARS
    ]
    return build_ipm_series_from_audits(
        results,
        execution_id=execution_id,
        municipality=municipality,
    )


def write_ipm_series_outputs(outputs: IpmSeriesOutputs, output_dir: Path) -> None:
    """Grava apenas derivados pequenos e auditáveis."""
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=False)
    outputs.series.to_csv(target / "sao_borja_ipm_definitive_2003_2026.csv", index=False)
    outputs.validation.to_csv(target / "validation.csv", index=False)
    outputs.source_manifest.to_csv(target / "source_manifest.csv", index=False)
    outputs.run_metadata.to_csv(target / "run_metadata.csv", index=False)
