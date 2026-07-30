"""Inventário HEAD dos arquivos mensais de despesas do Estado do RS."""

from __future__ import annotations

import re
import shutil
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import pandas as pd
import requests

API_URL = "https://dados.rs.gov.br/api/3/action/package_search"
ALLOWED_HOST = "dados.rs.gov.br"
YEAR_PATTERN = re.compile(r"\b(20(?:1[2-9]|2[0-6]))\b")
FILE_PERIOD_PATTERN = re.compile(r"(20\d{2})(\d{2})\.zip$", re.IGNORECASE)
MONTH_NAMES = {
    "janeiro": 1,
    "fevereiro": 2,
    "marco": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12,
}


@dataclass(frozen=True)
class StateExpenseHeadInventoryResult:
    output_path: Path
    inventory: pd.DataFrame
    annual_summary: pd.DataFrame
    validation: pd.DataFrame


def _package_year(package: dict[str, object]) -> int | None:
    text = f"{package.get('title', '')} {package.get('name', '')}"
    match = YEAR_PATTERN.search(text)
    if match and "despesa" in text.lower():
        return int(match.group(1))
    return None


def _filename_period(url: str) -> tuple[int | None, int | None]:
    match = FILE_PERIOD_PATTERN.search(urlparse(url).path)
    if not match:
        return None, None
    return int(match.group(1)), int(match.group(2))


def _resource_name_month(value: object) -> int | None:
    normalized = "".join(
        char
        for char in unicodedata.normalize("NFKD", str(value))
        if not unicodedata.combining(char)
    ).strip().lower()
    return MONTH_NAMES.get(normalized)


def _safe_head(
    session: requests.Session,
    url: str,
    *,
    timeout: float,
    max_redirects: int = 5,
) -> dict[str, object]:
    current = url
    redirects = 0
    while True:
        if urlparse(current).hostname != ALLOWED_HOST:
            raise ValueError(f"Domínio não autorizado: {current}")
        response = session.head(current, timeout=timeout, allow_redirects=False)
        status = int(response.status_code)
        if status in {301, 302, 303, 307, 308}:
            location = response.headers.get("Location", "")
            response.close()
            if not location or redirects >= max_redirects:
                raise ValueError("Redirecionamento inválido ou excessivo")
            current = urljoin(current, location)
            redirects += 1
            continue
        headers = dict(response.headers)
        final_url = str(getattr(response, "url", current) or current)
        response.close()
        if urlparse(final_url).hostname != ALLOWED_HOST:
            raise ValueError(f"Domínio final não autorizado: {final_url}")
        length = headers.get("Content-Length", "")
        return {
            "head_status": status,
            "final_url": final_url,
            "redirect_count": redirects,
            "content_type": headers.get("Content-Type", ""),
            "content_length": int(length) if str(length).isdigit() else None,
            "accept_ranges": headers.get("Accept-Ranges", ""),
            "head_error": "",
        }


def _head_or_error(
    session: requests.Session,
    resource: dict[str, object],
    *,
    timeout: float,
) -> dict[str, object]:
    try:
        return _safe_head(session, str(resource["source_url"]), timeout=timeout)
    except Exception as exc:
        return {
            "head_status": None,
            "final_url": "",
            "redirect_count": None,
            "content_type": "",
            "content_length": None,
            "accept_ranges": "",
            "head_error": f"{type(exc).__name__}: {exc}",
        }


def _catalog_resources(
    session: requests.Session,
    *,
    timeout: float,
) -> list[dict[str, object]]:
    response = session.get(
        API_URL,
        params={"q": "organization:cage", "rows": 100},
        timeout=timeout,
    )
    response.raise_for_status()
    payload = response.json()
    if not payload.get("success"):
        raise ValueError("Consulta CKAN sem sucesso")
    rows = []
    for package in payload["result"]["results"]:
        year = _package_year(package)
        if year is None:
            continue
        for resource in package.get("resources", []):
            url = str(resource.get("url", ""))
            if not urlparse(url).path.lower().endswith(".zip"):
                continue
            filename_year, filename_month = _filename_period(url)
            resource_name_month = _resource_name_month(resource.get("name", ""))
            rows.append({
                "package_id": package.get("id", ""),
                "package_name": package.get("name", ""),
                "package_title": package.get("title", ""),
                "catalog_year": year,
                "resource_id": resource.get("id", ""),
                "resource_name": resource.get("name", ""),
                "catalog_format": resource.get("format", ""),
                "catalog_size": resource.get("size"),
                "catalog_last_modified": resource.get("last_modified"),
                "source_url": url,
                "filename_year": filename_year,
                "filename_month": filename_month,
                "resource_name_month": resource_name_month,
                "government_sphere": "STATE_RS",
                "dimension": "financas_publicas_transferencias",
                "financial_family": "DIRECT_EXPENDITURE_OR_TRANSFER",
                "nature": "observed_catalog_and_head_metadata",
            })
    return rows


def inventory_state_rs_expense_heads(
    *,
    output_root: Path,
    run_id: str,
    session: requests.Session | None = None,
    timeout: float = 20,
    max_workers: int = 8,
) -> StateExpenseHeadInventoryResult:
    """Consulta catálogo e HEAD sem baixar os corpos dos recursos."""
    if not run_id or Path(run_id).name != run_id:
        raise ValueError("run_id deve ser um identificador simples")
    if not 1 <= max_workers <= 16:
        raise ValueError("max_workers deve estar entre 1 e 16")
    target = output_root.resolve() / run_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError("Execução existente ou incompleta")
    client = session or requests.Session()
    resources = _catalog_resources(client, timeout=timeout)
    if not resources:
        raise ValueError("Nenhum recurso mensal localizado")
    obtained_at = datetime.now(UTC).isoformat()
    partial.mkdir(parents=True)
    try:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(
                    _head_or_error, client, row, timeout=timeout
                ): index
                for index, row in enumerate(resources)
            }
            for future in as_completed(futures):
                resources[futures[future]].update(future.result())
        for row in resources:
            row["obtained_at_utc"] = obtained_at
            row["body_downloaded"] = False
            row["catalog_filename_period_matches"] = bool(
                row["filename_year"] == row["catalog_year"]
                and row["filename_month"] == row["resource_name_month"]
            )
        inventory = pd.DataFrame(resources).sort_values(
            ["catalog_year", "resource_name", "resource_id"]
        )
        annual = (
            inventory.groupby("catalog_year", as_index=False)
            .agg(
                resources=("resource_id", "count"),
                head_successes=("head_status", lambda values: int(
                    pd.to_numeric(values, errors="coerce")
                    .between(200, 299)
                    .sum()
                )),
                sizes_observed=("content_length", lambda values: int(
                    values.notna().sum()
                )),
                observed_bytes=("content_length", "sum"),
                filename_period_matches=(
                    "catalog_filename_period_matches", "sum"
                ),
                head_errors=("head_error", lambda values: int(
                    values.astype(bool).sum()
                )),
            )
            .sort_values("catalog_year")
        )
        annual["nature"] = "calculated_from_head_metadata"
        head_successes = int(
            pd.to_numeric(inventory.head_status, errors="coerce")
            .between(200, 299)
            .sum()
        )
        sizes_observed = int(inventory.content_length.notna().sum())
        errors = int(inventory.head_error.astype(bool).sum())
        validation = pd.DataFrame(
            [
                ("resources_cataloged", len(inventory), "calculated", "PASS"),
                (
                    "head_successes",
                    head_successes,
                    "calculated",
                    "PASS" if head_successes == len(inventory) else "WARN",
                ),
                (
                    "sizes_observed",
                    sizes_observed,
                    "calculated",
                    "PASS" if sizes_observed == len(inventory) else "WARN",
                ),
                (
                    "head_errors",
                    errors,
                    "calculated",
                    "PASS" if errors == 0 else "WARN",
                ),
                ("response_bodies_downloaded", 0, "calculated", "PASS"),
                ("canonical_rows_promoted", 0, "calculated", "PASS"),
            ],
            columns=["indicator", "value", "nature", "status"],
        )
        inventory.to_csv(partial / "resource_head_inventory.csv", index=False)
        annual.to_csv(partial / "annual_summary.csv", index=False)
        validation.to_csv(partial / "validation.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return StateExpenseHeadInventoryResult(
        target, inventory, annual, validation
    )
