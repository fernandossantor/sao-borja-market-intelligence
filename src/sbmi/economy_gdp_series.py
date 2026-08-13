"""Captura oficial e auditável das séries municipais de PIB e VAB."""

from __future__ import annotations

import hashlib
import io
import json
import shutil
import zipfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd

MUNICIPALITY_CODE = "4318002"
OLD_HOST = "ftp.ibge.gov.br"
SIDRA_HOST = "apisidra.ibge.gov.br"
MISSING = {"", "-", "..", "...", "X"}
VARIABLES = {
    "37": ("pib_total", "PIB a preços correntes", "absolute"),
    "543": ("taxes", "Impostos líquidos de subsídios", "absolute"),
    "498": ("vab_total", "VAB total", "absolute"),
    "513": ("agriculture", "Agropecuária", "absolute"),
    "516": ("agriculture", "Agropecuária", "percentage"),
    "517": ("industry", "Indústria", "absolute"),
    "520": ("industry", "Indústria", "percentage"),
    "6575": (
        "services_ex_public",
        "Comércio e demais serviços, exceto administração pública",
        "absolute",
    ),
    "6574": (
        "services_ex_public",
        "Comércio e demais serviços, exceto administração pública",
        "percentage",
    ),
    "525": ("public_administration", "Administração pública", "absolute"),
    "528": ("public_administration", "Administração pública", "percentage"),
}


@dataclass(frozen=True)
class GdpResult:
    values: pd.DataFrame
    manifest: pd.DataFrame
    validation: pd.DataFrame
    paths: dict[str, Path]


def _target(root: Path, identifier: str) -> tuple[Path, Path]:
    if Path(identifier).name != identifier or not identifier:
        raise ValueError("Identificador inválido")
    target = root.resolve() / identifier
    partial = target.with_name(f".{identifier}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(target)
    return target, partial


def _fetch(session, url: str, host: str, limit: int, timeout: float) -> tuple[bytes, dict]:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname != host:
        raise ValueError("URL fora do domínio oficial permitido")
    response = session.get(url, timeout=timeout, headers={"User-Agent": "sbmi-gdp-series/1.0"})
    response.raise_for_status()
    content = bytes(response.content)
    if not content or len(content) > limit:
        raise ValueError("Resposta vazia ou acima do limite")
    final_url = str(getattr(response, "url", url))
    final = urlparse(final_url)
    if final.scheme != "https" or final.hostname != host:
        raise ValueError("Redirecionamento fora do domínio permitido")
    content_type = str(response.headers.get("Content-Type", ""))
    expected_type = "json" if host == SIDRA_HOST else "zip"
    if expected_type not in content_type.lower():
        raise ValueError(f"Tipo de conteúdo inesperado: {content_type}")
    return content, {
        "source_url": url,
        "final_url": final_url,
        "content_type": content_type,
        "obtained_at": datetime.now(UTC).isoformat(),
        "bytes": len(content),
        "sha256": hashlib.sha256(content).hexdigest(),
        "source_institution": "IBGE",
        "nature": "observed",
    }


def _old_rows(content: bytes, source_url: str) -> list[dict]:
    with zipfile.ZipFile(io.BytesIO(content)) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".txt")]
        if len(names) != 1:
            raise ValueError("Arquivo histórico sem TXT único")
        raw = archive.read(names[0]).decode("latin-1")
    rows = []
    fields = {
        "agriculture": (223, 241, "Agropecuária"),
        "industry": (242, 260, "Indústria"),
        "services_including_public": (261, 279, "Serviços, incluindo administração pública"),
        "public_administration": (280, 298, "Administração pública"),
        "taxes": (299, 317, "Impostos líquidos de subsídios"),
        "pib_total": (318, 336, "PIB a preços correntes"),
    }
    for line in raw.splitlines():
        if line[34:41] != MUNICIPALITY_CODE:
            continue
        year = int(line[0:4])
        observed = {key: float(line[a:b].strip()) for key, (a, b, _) in fields.items()}
        vab = observed["agriculture"] + observed["industry"] + observed["services_including_public"]
        for key, value in observed.items():
            rows.append(
                _row(
                    year,
                    key,
                    fields[key][2],
                    "absolute",
                    value,
                    "old_1999_2001",
                    source_url,
                    "observed",
                )
            )
            if key in {
                "agriculture",
                "industry",
                "services_including_public",
                "public_administration",
            }:
                rows.append(
                    _row(
                        year,
                        key,
                        fields[key][2],
                        "percentage",
                        value / vab * 100,
                        "old_1999_2001",
                        source_url,
                        "calculated",
                    )
                )
    if {row["reference_year"] for row in rows} != {1999, 2000, 2001}:
        raise ValueError("Cobertura histórica inesperada")
    return rows


def _row(year, indicator, label, kind, value, methodology, url, nature):
    return {
        "municipality_code": MUNICIPALITY_CODE,
        "municipality_name": "São Borja (RS)",
        "reference_year": year,
        "indicator_id": indicator,
        "indicator_name": label,
        "value_kind": kind,
        "unit": "Mil Reais" if kind == "absolute" else "% do VAB total",
        "numeric_value": value,
        "value_status": "OBSERVED_NUMERIC",
        "methodology_series": methodology,
        "source_url": url,
        "nature": nature,
    }


def _sidra_rows(content: bytes, source_url: str) -> list[dict]:
    payload = json.loads(content)
    if not isinstance(payload, list) or len(payload) < 2:
        raise ValueError("Resposta SIDRA inválida")
    output = []
    for item in payload[1:]:
        if item.get("NC") != "6" or item.get("D1C") != MUNICIPALITY_CODE:
            raise ValueError("Geografia SIDRA divergente")
        variable = str(item.get("D3C", ""))
        if variable not in VARIABLES:
            raise ValueError("Variável SIDRA divergente")
        indicator, label, kind = VARIABLES[variable]
        raw = str(item.get("V", ""))
        row = _row(
            int(item["D2C"]),
            indicator,
            label,
            kind,
            float(raw) if raw not in MISSING else None,
            "current_2002_onward",
            source_url,
            "observed",
        )
        row.update(
            variable_id=variable,
            raw_value=raw,
            value_status="MISSING_OR_SUPPRESSED" if raw in MISSING else "OBSERVED_NUMERIC",
        )
        output.append(row)
    return output


def collect_economy_gdp_series(
    session,
    *,
    old_url: str,
    sidra_url: str,
    roots: dict[str, Path],
    execution_id: str,
    timeout_seconds: float = 45,
    max_bytes: int = 15_000_000,
) -> GdpResult:
    """Captura, normaliza, valida e publica sem sobrescrever."""
    if set(roots) != {"raw", "staging", "curated", "exports", "audit"}:
        raise ValueError("Camadas obrigatórias ausentes")
    targets = {layer: _target(root, execution_id) for layer, root in roots.items()}
    old, old_meta = _fetch(session, old_url, OLD_HOST, max_bytes, timeout_seconds)
    sidra, sidra_meta = _fetch(session, sidra_url, SIDRA_HOST, max_bytes, timeout_seconds)
    old_meta["raw_file"] = "pib_municipios_1999_2001.zip"
    sidra_meta["raw_file"] = "sidra_5938.json"
    values = pd.DataFrame(_old_rows(old, old_url) + _sidra_rows(sidra, sidra_url)).sort_values(
        ["methodology_series", "reference_year", "indicator_id", "value_kind"]
    )
    duplicate_count = int(
        values.duplicated(
            ["methodology_series", "reference_year", "indicator_id", "value_kind"]
        ).sum()
    )
    current = values[
        (values.methodology_series == "current_2002_onward")
        & (values.value_status == "OBSERVED_NUMERIC")
    ]
    abs_current = current[current.value_kind == "absolute"].pivot(
        index="reference_year", columns="indicator_id", values="numeric_value"
    )
    years = abs_current.dropna(
        subset=[
            "vab_total",
            "agriculture",
            "industry",
            "services_ex_public",
            "public_administration",
            "taxes",
            "pib_total",
        ]
    )
    vab_error = (
        (
            years.vab_total
            - years[["agriculture", "industry", "services_ex_public", "public_administration"]].sum(
                axis=1
            )
        )
        .abs()
        .max()
    )
    pib_error = (years.pib_total - years.vab_total - years.taxes).abs().max()
    old_abs = values[
        (values.methodology_series == "old_1999_2001") & (values.value_kind == "absolute")
    ].pivot(index="reference_year", columns="indicator_id", values="numeric_value")
    old_error = (
        (
            old_abs.pib_total
            - old_abs.agriculture
            - old_abs.industry
            - old_abs.services_including_public
            - old_abs.taxes
        )
        .abs()
        .max()
    )
    validation = pd.DataFrame(
        [
            ("rows", len(values), "calculated", "PASS"),
            (
                "duplicate_keys",
                duplicate_count,
                "calculated",
                "PASS" if not duplicate_count else "FAIL",
            ),
            (
                "old_years",
                old_abs.shape[0],
                "calculated",
                "PASS" if old_abs.shape[0] == 3 else "FAIL",
            ),
            (
                "current_complete_sector_years",
                years.shape[0],
                "calculated",
                "PASS" if years.shape[0] == 20 else "FAIL",
            ),
            (
                "old_pib_reconciliation_max_thousand_reais",
                old_error,
                "calculated",
                "PASS" if old_error <= 0.02 else "FAIL",
            ),
            (
                "current_vab_reconciliation_max_thousand_reais",
                vab_error,
                "calculated",
                "PASS" if vab_error <= 4 else "FAIL",
            ),
            (
                "current_pib_reconciliation_max_thousand_reais",
                pib_error,
                "calculated",
                "PASS" if pib_error <= 4 else "FAIL",
            ),
            (
                "missing_sidra_values",
                int((values.value_status == "MISSING_OR_SUPPRESSED").sum()),
                "calculated",
                "INFORMATIONAL",
            ),
        ],
        columns=["indicator", "value", "nature", "status"],
    )
    if duplicate_count or "FAIL" in set(validation.status):
        raise ValueError("Validação econômica falhou")
    manifest = pd.DataFrame([old_meta, sidra_meta])
    for _, partial in targets.values():
        partial.mkdir(parents=True)
    try:
        (targets["raw"][1] / old_meta["raw_file"]).write_bytes(old)
        (targets["raw"][1] / sidra_meta["raw_file"]).write_bytes(sidra)
        manifest.to_csv(targets["raw"][1] / "manifest.csv", index=False)
        values.to_csv(targets["staging"][1] / "economy_gdp_series_staging.csv", index=False)
        values.to_csv(targets["curated"][1] / "economy_gdp_series.csv", index=False)
        values.to_csv(targets["exports"][1] / "economy_gdp_series.csv", index=False)
        manifest.to_csv(targets["audit"][1] / "source_manifest.csv", index=False)
        validation.to_csv(targets["audit"][1] / "validation.csv", index=False)
        promoted: list[Path] = []
        for target, partial in targets.values():
            target.parent.mkdir(parents=True, exist_ok=True)
            partial.replace(target)
            promoted.append(target)
    except Exception:
        for _, partial in targets.values():
            shutil.rmtree(partial, ignore_errors=True)
        for target in reversed(locals().get("promoted", [])):
            shutil.rmtree(target, ignore_errors=True)
        raise
    return GdpResult(
        values, manifest, validation, {layer: pair[0] for layer, pair in targets.items()}
    )
