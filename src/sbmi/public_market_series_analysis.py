"""Análise reprodutível das séries públicas normalizadas do SBMI."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class AnalysisBuildResult:
    output_dir: Path
    validation: pd.DataFrame
    manifest: pd.DataFrame
    summary: dict[str, object]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _safe_pct_change(current: pd.Series, previous: pd.Series) -> pd.Series:
    return (current / previous - 1.0) * 100.0


def build_dfe_monthly_panel(monthly: pd.DataFrame) -> pd.DataFrame:
    """Cria painel mensal comparável por modelo, sem somar modelos distintos."""
    frame = monthly.copy()
    frame["ano_mes"] = frame["ano_mes"].astype("string")
    frame["ano"] = frame["ano_mes"].str[:4].astype(int)
    frame["mes"] = frame["ano_mes"].str[5:7].astype(int)
    frame["valor_medio_dfe"] = frame["vlr_total_dfe"] / frame["qtde_dfe"]

    base = (
        frame.loc[(frame["ano"] == 2024) & (~frame["periodo_parcial"].astype(bool))]
        .groupby("modelo_dfe", as_index=False)
        .agg(
            base_qtde_2024=("qtde_dfe", "mean"),
            base_valor_2024=("vlr_total_dfe", "mean"),
            base_valor_medio_2024=("valor_medio_dfe", "mean"),
        )
    )
    if len(base) != frame["modelo_dfe"].nunique():
        raise ValueError("Base 2024 incompleta para algum modelo DFe")
    frame = frame.merge(base, on="modelo_dfe", how="left", validate="many_to_one")

    full = ~frame["periodo_parcial"].astype(bool)
    frame["indice_qtde_base_media_2024"] = (
        frame["qtde_dfe"] / frame["base_qtde_2024"] * 100.0
    ).where(full)
    frame["indice_valor_base_media_2024"] = (
        frame["vlr_total_dfe"] / frame["base_valor_2024"] * 100.0
    ).where(full)
    frame["indice_valor_medio_base_media_2024"] = (
        frame["valor_medio_dfe"] / frame["base_valor_medio_2024"] * 100.0
    ).where(full)

    prior = frame[
        [
            "modelo_dfe",
            "ano",
            "mes",
            "qtde_dfe",
            "vlr_total_dfe",
            "valor_medio_dfe",
            "periodo_parcial",
        ]
    ].copy()
    prior["ano"] = prior["ano"] + 1
    prior = prior.rename(
        columns={
            "qtde_dfe": "qtde_dfe_ano_anterior",
            "vlr_total_dfe": "vlr_total_dfe_ano_anterior",
            "valor_medio_dfe": "valor_medio_dfe_ano_anterior",
            "periodo_parcial": "periodo_parcial_ano_anterior",
        }
    )
    frame = frame.merge(prior, on=["modelo_dfe", "ano", "mes"], how="left")
    comparable = (
        ~frame["periodo_parcial"].astype(bool)
        & frame["periodo_parcial_ano_anterior"].astype("boolean").fillna(True).eq(False)
    )
    frame["qtde_yoy_pct"] = _safe_pct_change(
        frame["qtde_dfe"], frame["qtde_dfe_ano_anterior"]
    ).where(comparable)
    frame["valor_yoy_pct"] = _safe_pct_change(
        frame["vlr_total_dfe"], frame["vlr_total_dfe_ano_anterior"]
    ).where(comparable)
    frame["valor_medio_yoy_pct"] = _safe_pct_change(
        frame["valor_medio_dfe"], frame["valor_medio_dfe_ano_anterior"]
    ).where(comparable)
    frame["status_comparabilidade"] = frame["periodo_parcial"].astype(bool).map(
        {False: "mes_completo", True: "mes_parcial"}
    )
    return frame.loc[frame["ano"] >= 2024].sort_values(["ano_mes", "modelo_dfe"])


def build_dfe_ytd_comparable(daily: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    """Compara o ano corrente com o anterior até o mesmo dia de corte."""
    frame = daily.copy()
    frame["dt_emissao"] = pd.to_datetime(frame["dt_emissao"], errors="raise")
    cutoff = frame["dt_emissao"].max()
    current_year = int(cutoff.year)
    previous_year = current_year - 1
    cutoff_previous = pd.Timestamp(previous_year, cutoff.month, cutoff.day)

    rows: list[dict[str, object]] = []
    for model in sorted(frame["modelo_dfe"].unique()):
        current = frame.loc[
            (frame["modelo_dfe"] == model)
            & (frame["dt_emissao"] >= pd.Timestamp(current_year, 1, 1))
            & (frame["dt_emissao"] <= cutoff)
        ]
        previous = frame.loc[
            (frame["modelo_dfe"] == model)
            & (frame["dt_emissao"] >= pd.Timestamp(previous_year, 1, 1))
            & (frame["dt_emissao"] <= cutoff_previous)
        ]
        q_cur = int(current["qtde_dfe"].sum())
        q_prev = int(previous["qtde_dfe"].sum())
        v_cur = float(current["vlr_total_dfe"].sum())
        v_prev = float(previous["vlr_total_dfe"].sum())
        avg_cur = v_cur / q_cur
        avg_prev = v_prev / q_prev
        rows.append(
            {
                "modelo_dfe": model,
                "ano_anterior": previous_year,
                "ano_corrente": current_year,
                "data_corte_ano_corrente": cutoff.date().isoformat(),
                "data_corte_ano_anterior": cutoff_previous.date().isoformat(),
                "qtde_ano_anterior": q_prev,
                "qtde_ano_corrente": q_cur,
                "qtde_yoy_pct": (q_cur / q_prev - 1.0) * 100.0,
                "valor_ano_anterior": v_prev,
                "valor_ano_corrente": v_cur,
                "valor_yoy_pct": (v_cur / v_prev - 1.0) * 100.0,
                "valor_medio_ano_anterior": avg_prev,
                "valor_medio_ano_corrente": avg_cur,
                "valor_medio_yoy_pct": (avg_cur / avg_prev - 1.0) * 100.0,
            }
        )
    return pd.DataFrame(rows), {
        "current_year": current_year,
        "previous_year": previous_year,
        "cutoff_current": cutoff.date().isoformat(),
        "cutoff_previous": cutoff_previous.date().isoformat(),
    }


def build_cesta_yoy(
    cesta: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, object]]:
    """Calcula variações homólogas por produto e distribuições não ponderadas."""
    frame = cesta.copy()
    frame["ano_mes"] = frame["ano_mes"].astype("string")
    frame["ano"] = frame["ano_mes"].str[:4].astype(int)
    frame["mes"] = frame["ano_mes"].str[5:7].astype(int)

    prior = frame[["produto", "ano", "mes", "vlr_unidade"]].copy()
    prior["ano"] = prior["ano"] + 1
    prior = prior.rename(columns={"vlr_unidade": "vlr_unidade_ano_anterior"})
    yoy = frame.merge(prior, on=["produto", "ano", "mes"], how="left", validate="many_to_one")
    yoy["variacao_homologa_pct"] = _safe_pct_change(
        yoy["vlr_unidade"], yoy["vlr_unidade_ano_anterior"]
    )
    yoy = yoy.loc[yoy["vlr_unidade_ano_anterior"].notna()].copy()

    distribution = (
        yoy.groupby("ano_mes", as_index=False)
        .agg(
            produtos=("produto", "size"),
            mediana_variacao_pct=("variacao_homologa_pct", "median"),
            media_variacao_pct=("variacao_homologa_pct", "mean"),
            q1_variacao_pct=("variacao_homologa_pct", lambda s: s.quantile(0.25)),
            q3_variacao_pct=("variacao_homologa_pct", lambda s: s.quantile(0.75)),
            produtos_alta=("variacao_homologa_pct", lambda s: int(s.gt(0).sum())),
            produtos_queda=("variacao_homologa_pct", lambda s: int(s.lt(0).sum())),
        )
        .sort_values("ano_mes")
    )
    distribution["pct_produtos_alta"] = distribution["produtos_alta"] / distribution["produtos"] * 100.0
    distribution["pct_produtos_queda"] = distribution["produtos_queda"] / distribution["produtos"] * 100.0

    h1 = frame.loc[frame["ano"].isin([2025, 2026]) & frame["mes"].le(6)].copy()
    h1_product = h1.groupby(["produto", "ano"])["vlr_unidade"].mean().unstack()
    if not {2025, 2026}.issubset(h1_product.columns):
        raise ValueError("Cesta não possui H1 2025/2026 completo")
    h1_product = h1_product.rename(columns={2025: "media_2025_h1", 2026: "media_2026_h1"})
    h1_product["variacao_pct"] = _safe_pct_change(
        h1_product["media_2026_h1"], h1_product["media_2025_h1"]
    )
    h1_product = h1_product.reset_index().sort_values("variacao_pct", ascending=False)

    return yoy.sort_values(["ano_mes", "produto"]), distribution, h1_product, {
        "h1_products": int(len(h1_product)),
        "h1_median_yoy_pct": float(h1_product["variacao_pct"].median()),
        "h1_mean_yoy_pct": float(h1_product["variacao_pct"].mean()),
        "h1_q1_yoy_pct": float(h1_product["variacao_pct"].quantile(0.25)),
        "h1_q3_yoy_pct": float(h1_product["variacao_pct"].quantile(0.75)),
        "h1_products_up": int(h1_product["variacao_pct"].gt(0).sum()),
        "h1_products_down": int(h1_product["variacao_pct"].lt(0).sum()),
    }


def build_radar_sector_panel(
    group_monthly: pd.DataFrame,
    coverage_monthly: pd.DataFrame,
) -> tuple[pd.DataFrame, dict[str, object]]:
    """Agrega o benchmark estadual por setor/status e inclui controles de cobertura."""
    group = group_monthly.copy()
    panel = (
        group.groupby(["ano_mes", "setor_principal_sbmi", "status_sbmi"], as_index=False)
        .agg(
            grupos=("grupo_afinidade_final", "nunique"),
            rows=("rows", "sum"),
            rows_corte_sigilo=("rows_corte_sigilo", "sum"),
            valor_publicado_nao_sigilo=("vlr_nominal_publicado_nao_sigilo", "sum"),
        )
    )
    panel["pct_rows_corte_sigilo"] = panel["rows_corte_sigilo"] / panel["rows"] * 100.0

    total_mapped = panel.groupby("ano_mes")["valor_publicado_nao_sigilo"].sum()
    coverage = coverage_monthly.copy().set_index("ano_mes")
    coverage["valor_mapeado"] = total_mapped
    coverage["pct_valor_taxonomia_mapeada"] = (
        coverage["valor_mapeado"] / coverage["vlr_nominal_publicado_nao_sigilo"] * 100.0
    )
    controls = coverage[
        [
            "pct_rows_taxonomia_mapeada",
            "pct_rows_corte_sigilo",
            "pct_valor_taxonomia_mapeada",
            "source_numeric_rule",
        ]
    ].reset_index()
    panel = panel.merge(controls, on="ano_mes", how="left", validate="many_to_one")

    panel["ano"] = panel["ano_mes"].str[:4].astype(int)
    panel["mes"] = panel["ano_mes"].str[5:7].astype(int)
    prior = panel[
        ["setor_principal_sbmi", "status_sbmi", "ano", "mes", "valor_publicado_nao_sigilo"]
    ].copy()
    prior["ano"] = prior["ano"] + 1
    prior = prior.rename(columns={"valor_publicado_nao_sigilo": "valor_ano_anterior"})
    panel = panel.merge(
        prior,
        on=["setor_principal_sbmi", "status_sbmi", "ano", "mes"],
        how="left",
    )
    panel["variacao_nominal_yoy_pct"] = _safe_pct_change(
        panel["valor_publicado_nao_sigilo"], panel["valor_ano_anterior"]
    )

    jan_aug = panel.loc[panel["ano"].isin([2025, 2026]) & panel["mes"].le(8)]
    comparison = (
        jan_aug.groupby(["setor_principal_sbmi", "status_sbmi", "ano"])[
            "valor_publicado_nao_sigilo"
        ]
        .sum()
        .unstack()
    )
    comparison["variacao_pct"] = _safe_pct_change(comparison[2026], comparison[2025])
    summary_rows = []
    for sector, status in [
        ("Bens Essenciais", "CORE"),
        ("Bens Não Essenciais", "CORE"),
        ("Saúde/Higiene/Cuidados Pessoais", "CORE"),
        ("Serviços", "ADJACENT"),
    ]:
        key = (sector, status)
        if key in comparison.index:
            summary_rows.append(
                {
                    "sector": sector,
                    "status": status,
                    "jan_aug_2025": float(comparison.loc[key, 2025]),
                    "jan_aug_2026": float(comparison.loc[key, 2026]),
                    "nominal_yoy_pct": float(comparison.loc[key, "variacao_pct"]),
                }
            )
    return panel.sort_values(["ano_mes", "setor_principal_sbmi", "status_sbmi"]), {
        "jan_aug_comparison": summary_rows,
        "value_taxonomy_coverage_pct_overall": float(
            panel.groupby("ano_mes")["valor_publicado_nao_sigilo"].sum().sum()
            / coverage["vlr_nominal_publicado_nao_sigilo"].sum()
            * 100.0
        ),
    }


def build_taxonomy_gap_prefix(unmapped: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    """Resume NCMs não classificados pelo prefixo de dois dígitos, sem imputar grupo."""
    frame = unmapped.copy()
    frame["ncm8"] = frame["ncm8"].astype("string").str.zfill(8)
    frame["prefixo2"] = frame["ncm8"].str[:2]
    summary = (
        frame.groupby(["series", "prefixo2"], as_index=False)
        .agg(
            ncm8_unicos=("ncm8", "nunique"),
            rows=("rows", "sum"),
            valor_publicado=("valor_publicado", "sum"),
        )
    )
    totals = summary.groupby("series")["valor_publicado"].transform("sum")
    summary["pct_valor_nao_classificado"] = summary["valor_publicado"] / totals * 100.0
    comp = summary.loc[summary["series"].eq("radar_composicao_mercado")]
    prefix29 = comp.loc[comp["prefixo2"].eq("29")]
    return summary.sort_values(["series", "valor_publicado"], ascending=[True, False]), {
        "composition_prefix29_ncm8": int(prefix29["ncm8_unicos"].sum()),
        "composition_prefix29_rows": int(prefix29["rows"].sum()),
        "composition_prefix29_value": float(prefix29["valor_publicado"].sum()),
        "composition_prefix29_pct_unmapped_value": float(
            prefix29["pct_valor_nao_classificado"].sum()
        ),
    }


def _validation_row(check: str, value: object, passed: bool, note: str) -> dict[str, object]:
    return {"check": check, "value": value, "status": "PASS" if passed else "FAIL", "note": note}


def _build_manifest(output_dir: Path, files: list[Path]) -> pd.DataFrame:
    rows = []
    for path in sorted(files, key=lambda p: p.name):
        rows.append(
            {
                "file": path.name,
                "bytes": path.stat().st_size,
                "sha256": _sha256(path),
            }
        )
    return pd.DataFrame(rows)


def build_public_market_series_analysis(
    curated_root: Path,
    output_dir: Path,
    *,
    execution_id: str,
    source_run_id: str,
) -> AnalysisBuildResult:
    root = Path(curated_root)
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)

    monthly = pd.read_csv(root / "dfe_sao_borja_modelo_mensal.csv")
    daily = pd.read_csv(root / "dfe_sao_borja_diario.csv")
    cesta = pd.read_csv(root / "cesta_fronteira_oeste_produto_mensal.csv")
    radar_group = pd.read_csv(root / "radar_composicao_sbmi_grupo_mensal.csv")
    radar_coverage = pd.read_csv(root / "radar_composicao_rs_cobertura_mensal.csv")
    unmapped = pd.read_csv(root / "radar_ncm8_nao_classificados.csv")

    dfe_panel = build_dfe_monthly_panel(monthly)
    dfe_ytd, dfe_ytd_meta = build_dfe_ytd_comparable(daily)
    cesta_yoy, cesta_dist, cesta_h1, cesta_meta = build_cesta_yoy(cesta)
    radar_panel, radar_meta = build_radar_sector_panel(radar_group, radar_coverage)
    gap_prefix, gap_meta = build_taxonomy_gap_prefix(unmapped)

    outputs = {
        "dfe_sao_borja_painel_mensal_2024_2026.csv": dfe_panel,
        "dfe_sao_borja_ytd_comparavel.csv": dfe_ytd,
        "cesta_fronteira_oeste_yoy_produto_mensal.csv": cesta_yoy,
        "cesta_fronteira_oeste_yoy_distribuicao_mensal.csv": cesta_dist,
        "cesta_fronteira_oeste_h1_2026_vs_2025.csv": cesta_h1,
        "radar_rs_benchmark_setor_status_mensal.csv": radar_panel,
        "radar_taxonomia_gap_prefixo2.csv": gap_prefix,
    }
    for name, frame in outputs.items():
        frame.to_csv(target / name, index=False, encoding="utf-8", float_format="%.6f")

    validations = [
        _validation_row(
            "dfe_models",
            dfe_panel["modelo_dfe"].nunique(),
            dfe_panel["modelo_dfe"].nunique() == 3,
            "CT-e, NF-e e NFC-e devem permanecer separados.",
        ),
        _validation_row(
            "dfe_cutoff",
            dfe_ytd_meta["cutoff_current"],
            dfe_ytd_meta["cutoff_current"] == "2026-09-14",
            "Corte canônico do pacote-fonte.",
        ),
        _validation_row(
            "dfe_2026_sep_partial",
            int(
                dfe_panel.loc[
                    dfe_panel["ano_mes"].eq("2026-09"), "periodo_parcial"
                ].astype(bool).all()
            ),
            bool(
                dfe_panel.loc[
                    dfe_panel["ano_mes"].eq("2026-09"), "periodo_parcial"
                ].astype(bool).all()
            ),
            "Setembro/2026 é parcial e não recebe YoY de mês completo.",
        ),
        _validation_row(
            "cesta_h1_products",
            cesta_meta["h1_products"],
            cesta_meta["h1_products"] == 80,
            "Universo completo da Cesta Fronteira Oeste.",
        ),
        _validation_row(
            "cesta_2026_jun_products_yoy",
            int(cesta_yoy.loc[cesta_yoy["ano_mes"].eq("2026-06"), "produto"].nunique()),
            cesta_yoy.loc[cesta_yoy["ano_mes"].eq("2026-06"), "produto"].nunique() == 80,
            "Junho/2026 deve ter 80 comparações homólogas.",
        ),
        _validation_row(
            "radar_period_end",
            radar_panel["ano_mes"].max(),
            radar_panel["ano_mes"].max() == "2026-08",
            "Benchmark Radar encerra em agosto/2026.",
        ),
        _validation_row(
            "radar_value_taxonomy_coverage_pct",
            round(radar_meta["value_taxonomy_coverage_pct_overall"], 6),
            radar_meta["value_taxonomy_coverage_pct_overall"] > 99.0,
            "Benchmark por grupos deve cobrir mais de 99% do valor publicado não suprimido.",
        ),
        _validation_row(
            "gap_prefix29_value_share_pct",
            round(gap_meta["composition_prefix29_pct_unmapped_value"], 6),
            gap_meta["composition_prefix29_pct_unmapped_value"] > 99.0,
            "Concentração observada da lacuna monetária da Composição no prefixo NCM 29.",
        ),
    ]
    validation = pd.DataFrame(validations)
    validation.to_csv(target / "validation.csv", index=False, encoding="utf-8")
    if validation["status"].ne("PASS").any():
        failed = validation.loc[validation["status"].ne("PASS"), "check"].tolist()
        raise ValueError(f"Validações da camada analítica falharam: {failed}")

    summary = {
        "execution_id": execution_id,
        "source_run_id": source_run_id,
        "dfe_ytd": dfe_ytd.to_dict(orient="records"),
        "cesta_h1": cesta_meta,
        "radar": radar_meta,
        "taxonomy_gap": gap_meta,
        "governance": {
            "dfe_models_not_summed_for_market_share": True,
            "cesta_distribution_not_inflation_index": True,
            "radar_state_benchmark_not_municipal": True,
            "unmapped_ncm_not_imputed": True,
        },
    }
    (target / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    metadata = pd.DataFrame(
        [
            ["execution_id", execution_id, "lineage"],
            ["source_run_id", source_run_id, "lineage"],
            ["source_layer", "public-market-series-curated-v001", "lineage"],
            ["monetary_basis", "nominal", "method"],
            ["dfe_rule", "modelos separados", "governance"],
            ["cesta_rule", "variações relativas por produto; sem índice ponderado", "governance"],
            ["radar_rule", "benchmark estadual publicado não suprimido", "governance"],
        ],
        columns=["field", "value", "class"],
    )
    metadata.to_csv(target / "run_metadata.csv", index=False, encoding="utf-8")

    files = [p for p in target.iterdir() if p.is_file() and p.name != "manifest_analysis.csv"]
    manifest = _build_manifest(target, files)
    manifest.to_csv(target / "manifest_analysis.csv", index=False, encoding="utf-8")
    return AnalysisBuildResult(target, validation, manifest, summary)