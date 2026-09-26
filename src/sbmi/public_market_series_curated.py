"""Normalização auditável das séries públicas de dimensão de mercado do SBMI."""

from __future__ import annotations

import calendar
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd

RADAR_FILE_RE = re.compile(r"_(?P<month>\d{2})_(?P<year>\d{4})\.csv$")
CROSSWALK_COLUMNS = [
    "grupo_afinidade_final",
    "setor_principal_sbmi",
    "modulo_sbmi",
    "status_sbmi",
    "relacao_pof",
    "prioridade_sbmi",
    "justificativa",
]


@dataclass(frozen=True)
class CuratedBuildResult:
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


def _period_from_radar_filename(path: Path) -> str:
    match = RADAR_FILE_RE.search(path.name)
    if match is None:
        raise ValueError(f"Nome Radar sem mês/ano reconhecível: {path.name}")
    month = int(match.group("month"))
    year = int(match.group("year"))
    if not 1 <= month <= 12:
        raise ValueError(f"Mês inválido em {path.name}: {month}")
    return f"{year:04d}-{month:02d}"


def _normalize_ncm(series: pd.Series) -> pd.Series:
    return (
        series.astype("string")
        .str.replace(r"\.0$", "", regex=True)
        .str.replace(r"\D", "", regex=True)
        .str.zfill(8)
    )


def _numeric_decimal_comma(series: pd.Series) -> pd.Series:
    return pd.to_numeric(
        series.astype("string").str.replace(".", "", regex=False).str.replace(",", ".", regex=False),
        errors="coerce",
    )


def parse_crosswalk_markdown(path: Path) -> pd.DataFrame:
    """Extrai a tabela de 110 grupos do crosswalk editorial do Radar."""
    rows: list[list[str]] = []
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        if not raw.startswith("|") or "---" in raw or "Grupo de afinidade Radar" in raw:
            continue
        cells = [cell.strip() for cell in raw.split("|")[1:-1]]
        if len(cells) == len(CROSSWALK_COLUMNS):
            rows.append(cells)
    frame = pd.DataFrame(rows, columns=CROSSWALK_COLUMNS)
    if frame.empty:
        raise ValueError("Crosswalk NCM/SBMI não encontrado no Markdown")
    if frame["grupo_afinidade_final"].duplicated().any():
        raise ValueError("Crosswalk contém grupos de afinidade duplicados")
    return frame


def _read_taxonomy(taxonomy_csv: Path, crosswalk_md: Path) -> pd.DataFrame:
    taxonomy = pd.read_csv(taxonomy_csv, dtype="string", encoding="utf-8-sig")
    required = {"grupo_afinidade_final", "ncm8", "ncm4", "codxdescr_ncm8"}
    missing = required - set(taxonomy.columns)
    if missing:
        raise ValueError(f"Taxonomia sem colunas obrigatórias: {sorted(missing)}")
    taxonomy = taxonomy[list(required)].copy()
    taxonomy["ncm8"] = _normalize_ncm(taxonomy["ncm8"])
    taxonomy["ncm4"] = taxonomy["ncm8"].str[:4]
    if taxonomy["ncm8"].duplicated().any():
        raise ValueError("Taxonomia NCM8 não é unívoca")

    crosswalk = parse_crosswalk_markdown(crosswalk_md)
    groups_tax = set(taxonomy["grupo_afinidade_final"].dropna().unique())
    groups_cross = set(crosswalk["grupo_afinidade_final"].dropna().unique())
    if groups_tax != groups_cross:
        missing_cross = sorted(groups_tax - groups_cross)
        extra_cross = sorted(groups_cross - groups_tax)
        raise ValueError(
            "Crosswalk e taxonomia divergem: "
            f"missing_cross={missing_cross[:5]} extra_cross={extra_cross[:5]}"
        )
    return taxonomy.merge(crosswalk, on="grupo_afinidade_final", how="left", validate="many_to_one")


def _append_csv(frame: pd.DataFrame, path: Path, *, first: bool, float_format: str | None = None) -> None:
    frame.to_csv(
        path,
        index=False,
        mode="w" if first else "a",
        header=first,
        encoding="utf-8",
        float_format=float_format,
    )


def _build_radar_composition(
    raw_dir: Path,
    dim_ncm: pd.DataFrame,
    out_dir: Path,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object]]:
    fact_path = out_dir / "radar_composicao_rs_ncm_mensal.csv"
    files = sorted(raw_dir.glob("Composicao_de_Mercado_*.csv"), key=_period_from_radar_filename)
    if not files:
        raise ValueError("Nenhum arquivo Radar Composição encontrado")

    ncm_dim = dim_ncm[[
        "ncm8",
        "grupo_afinidade_final",
        "setor_principal_sbmi",
        "modulo_sbmi",
        "status_sbmi",
        "prioridade_sbmi",
    ]]
    coverage_rows: list[dict[str, object]] = []
    group_parts: list[pd.DataFrame] = []
    unmapped_parts: list[pd.DataFrame] = []
    total_rows = 0
    mapped_rows = 0

    for idx, file in enumerate(files):
        period = _period_from_radar_filename(file)
        frame = pd.read_csv(file, dtype="string", encoding="utf-8-sig")
        raw_anomes = frame["anomes"].astype("string")
        frame["ano_mes"] = period
        frame["anomes_fonte"] = raw_anomes
        frame["ncm8"] = _normalize_ncm(frame["cod_ncm"])
        frame["vlr_nominal"] = pd.to_numeric(frame["vlr_nominal"], errors="coerce")
        frame["corte_sigilo"] = pd.to_numeric(frame["corte_sigilo"], errors="coerce").astype("Int64")
        frame["source_file"] = file.name

        fact = frame[[
            "ano_mes",
            "anomes_fonte",
            "ncm8",
            "emit_uf",
            "tipo_operacao",
            "vlr_nominal",
            "corte_sigilo",
            "source_file",
        ]].copy()
        _append_csv(fact, fact_path, first=idx == 0, float_format="%.2f")

        joined = fact.merge(ncm_dim, on="ncm8", how="left", validate="many_to_one")
        total_rows += len(joined)
        mapped_rows += int(joined["grupo_afinidade_final"].notna().sum())
        non_suppressed = joined["corte_sigilo"].eq(0)
        suppressed = joined["corte_sigilo"].eq(1)
        coverage_rows.append(
            {
                "ano_mes": period,
                "rows": len(joined),
                "ncm8_unicos": joined["ncm8"].nunique(),
                "ncm8_taxonomia_mapeados": joined.loc[joined["grupo_afinidade_final"].notna(), "ncm8"].nunique(),
                "pct_ncm8_taxonomia_mapeados": joined.loc[joined["grupo_afinidade_final"].notna(), "ncm8"].nunique() / joined["ncm8"].nunique() * 100.0,
                "rows_taxonomia_mapeada": int(joined["grupo_afinidade_final"].notna().sum()),
                "pct_rows_taxonomia_mapeada": float(joined["grupo_afinidade_final"].notna().mean() * 100.0),
                "rows_corte_sigilo": int(suppressed.sum()),
                "pct_rows_corte_sigilo": float(suppressed.mean() * 100.0),
                "vlr_nominal_publicado_nao_sigilo": float(joined.loc[non_suppressed, "vlr_nominal"].sum()),
                "source_file": file.name,
            }
        )

        unmapped = joined.loc[joined["grupo_afinidade_final"].isna()].copy()
        if not unmapped.empty:
            unmapped["vlr_publicado_nao_sigilo"] = unmapped["vlr_nominal"].where(
                unmapped["corte_sigilo"].eq(0),
                0.0,
            )
            unmapped_parts.append(
                unmapped.groupby("ncm8", as_index=False).agg(
                    rows=("ncm8", "size"),
                    rows_corte_sigilo=("corte_sigilo", lambda s: int(s.eq(1).sum())),
                    vlr_publicado_nao_sigilo=("vlr_publicado_nao_sigilo", "sum"),
                ).assign(ano_mes=period)
            )

        benchmark_source = joined.loc[joined["grupo_afinidade_final"].notna()].copy()
        benchmark_source["vlr_nominal_publicado_nao_sigilo"] = benchmark_source[
            "vlr_nominal"
        ].where(
            benchmark_source["corte_sigilo"].eq(0),
            0.0,
        )
        grouped = (
            benchmark_source.groupby(
                [
                    "ano_mes",
                    "grupo_afinidade_final",
                    "setor_principal_sbmi",
                    "modulo_sbmi",
                    "status_sbmi",
                    "prioridade_sbmi",
                    "emit_uf",
                    "tipo_operacao",
                ],
                dropna=False,
                observed=True,
            )
            .agg(
                rows=("ncm8", "size"),
                ncm8_unicos=("ncm8", "nunique"),
                rows_corte_sigilo=("corte_sigilo", lambda s: int(s.eq(1).sum())),
                vlr_nominal_publicado_nao_sigilo=(
                    "vlr_nominal_publicado_nao_sigilo",
                    "sum",
                ),
            )
            .reset_index()
        )
        grouped["pct_rows_corte_sigilo"] = grouped["rows_corte_sigilo"] / grouped["rows"] * 100.0
        group_parts.append(grouped)

    coverage = pd.DataFrame(coverage_rows).sort_values("ano_mes").reset_index(drop=True)
    group_benchmark = pd.concat(group_parts, ignore_index=True).sort_values(
        ["ano_mes", "setor_principal_sbmi", "grupo_afinidade_final", "emit_uf", "tipo_operacao"]
    )
    unmapped_month = pd.concat(unmapped_parts, ignore_index=True) if unmapped_parts else pd.DataFrame()
    if not unmapped_month.empty:
        unmapped_summary = (
            unmapped_month.groupby("ncm8", as_index=False)
            .agg(
                first_month=("ano_mes", "min"),
                last_month=("ano_mes", "max"),
                rows=("rows", "sum"),
                rows_corte_sigilo=("rows_corte_sigilo", "sum"),
                vlr_publicado_nao_sigilo=("vlr_publicado_nao_sigilo", "sum"),
            )
            .sort_values(["rows", "ncm8"], ascending=[False, True])
        )
    else:
        unmapped_summary = pd.DataFrame(columns=["ncm8", "first_month", "last_month", "rows", "rows_corte_sigilo", "vlr_publicado_nao_sigilo"])
    return coverage, group_benchmark, unmapped_summary, {
        "files": len(files),
        "rows": total_rows,
        "taxonomy_rows_mapped": mapped_rows,
        "taxonomy_row_coverage_pct": mapped_rows / total_rows * 100.0 if total_rows else 0.0,
        "period_start": coverage["ano_mes"].min(),
        "period_end": coverage["ano_mes"].max(),
    }


def _build_radar_exports(
    raw_dir: Path,
    dim_ncm: pd.DataFrame,
    out_dir: Path,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, object]]:
    fact_path = out_dir / "radar_exportacoes_rs_ncm_pais_mensal.csv"
    files = sorted(raw_dir.glob("Exportacoes_NCM_*.csv"), key=_period_from_radar_filename)
    if not files:
        raise ValueError("Nenhum arquivo Radar Exportações encontrado")

    ncm_dim = dim_ncm[[
        "ncm8",
        "grupo_afinidade_final",
        "setor_principal_sbmi",
        "modulo_sbmi",
        "status_sbmi",
        "prioridade_sbmi",
    ]]
    coverage_rows: list[dict[str, object]] = []
    group_parts: list[pd.DataFrame] = []
    unmapped_parts: list[pd.DataFrame] = []
    total_rows = 0
    mapped_rows = 0

    for idx, file in enumerate(files):
        period = _period_from_radar_filename(file)
        frame = pd.read_csv(file, dtype="string", encoding="utf-8-sig")
        frame["ano_mes"] = period
        frame["anomes_fonte"] = frame["anomes"].astype("string")
        frame["ncm8"] = _normalize_ncm(frame["cod_ncm"])
        frame["cod_pais"] = frame["cod_pais"].astype("string").str.replace(r"\.0$", "", regex=True).str.zfill(3)
        frame["vlr_fob"] = pd.to_numeric(frame["vlr_fob"], errors="coerce")
        frame["source_file"] = file.name
        fact = frame[["ano_mes", "anomes_fonte", "ncm8", "cod_pais", "vlr_fob", "source_file"]].copy()
        _append_csv(fact, fact_path, first=idx == 0, float_format="%.2f")

        joined = fact.merge(ncm_dim, on="ncm8", how="left", validate="many_to_one")
        total_rows += len(joined)
        mapped_rows += int(joined["grupo_afinidade_final"].notna().sum())
        coverage_rows.append(
            {
                "ano_mes": period,
                "rows": len(joined),
                "ncm8_unicos": joined["ncm8"].nunique(),
                "ncm8_taxonomia_mapeados": joined.loc[joined["grupo_afinidade_final"].notna(), "ncm8"].nunique(),
                "pct_ncm8_taxonomia_mapeados": joined.loc[joined["grupo_afinidade_final"].notna(), "ncm8"].nunique() / joined["ncm8"].nunique() * 100.0,
                "paises_unicos": joined["cod_pais"].nunique(),
                "rows_taxonomia_mapeada": int(joined["grupo_afinidade_final"].notna().sum()),
                "pct_rows_taxonomia_mapeada": float(joined["grupo_afinidade_final"].notna().mean() * 100.0),
                "vlr_fob_publicado": float(joined["vlr_fob"].sum()),
                "source_file": file.name,
            }
        )
        unmapped = joined.loc[joined["grupo_afinidade_final"].isna()].copy()
        if not unmapped.empty:
            unmapped_parts.append(
                unmapped.groupby("ncm8", as_index=False).agg(
                    rows=("ncm8", "size"),
                    vlr_publicado=("vlr_fob", "sum"),
                ).assign(ano_mes=period)
            )

        benchmark_source = joined.loc[joined["grupo_afinidade_final"].notna()].copy()
        grouped = (
            benchmark_source.groupby(
                [
                    "ano_mes",
                    "grupo_afinidade_final",
                    "setor_principal_sbmi",
                    "modulo_sbmi",
                    "status_sbmi",
                    "prioridade_sbmi",
                ],
                dropna=False,
                observed=True,
            )
            .agg(
                rows=("ncm8", "size"),
                ncm8_unicos=("ncm8", "nunique"),
                paises_unicos=("cod_pais", "nunique"),
                vlr_fob_publicado=("vlr_fob", "sum"),
            )
            .reset_index()
        )
        group_parts.append(grouped)

    coverage = pd.DataFrame(coverage_rows).sort_values("ano_mes").reset_index(drop=True)
    group_benchmark = pd.concat(group_parts, ignore_index=True).sort_values(
        ["ano_mes", "setor_principal_sbmi", "grupo_afinidade_final"]
    )
    unmapped_month = pd.concat(unmapped_parts, ignore_index=True) if unmapped_parts else pd.DataFrame()
    if not unmapped_month.empty:
        unmapped_summary = (
            unmapped_month.groupby("ncm8", as_index=False)
            .agg(
                first_month=("ano_mes", "min"),
                last_month=("ano_mes", "max"),
                rows=("rows", "sum"),
                vlr_publicado=("vlr_publicado", "sum"),
            )
            .sort_values(["rows", "ncm8"], ascending=[False, True])
        )
    else:
        unmapped_summary = pd.DataFrame(columns=["ncm8", "first_month", "last_month", "rows", "vlr_publicado"])
    return coverage, group_benchmark, unmapped_summary, {
        "files": len(files),
        "rows": total_rows,
        "taxonomy_rows_mapped": mapped_rows,
        "taxonomy_row_coverage_pct": mapped_rows / total_rows * 100.0 if total_rows else 0.0,
        "period_start": coverage["ano_mes"].min(),
        "period_end": coverage["ano_mes"].max(),
    }


def _build_portfolio(raw_dir: Path, dim_ncm: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    file = raw_dir / "Portfolio_NCMs_Setor.csv"
    frame = pd.read_csv(file, dtype="string", encoding="utf-8-sig")
    frame["ncm8"] = _normalize_ncm(frame["cod_ncm"])
    joined = frame.merge(
        dim_ncm[[
            "ncm8",
            "grupo_afinidade_final",
            "setor_principal_sbmi",
            "modulo_sbmi",
            "status_sbmi",
            "prioridade_sbmi",
        ]],
        on="ncm8",
        how="left",
        validate="many_to_one",
    )
    out = joined[[
        "emit_atividade",
        "emit_classe",
        "emit_setor",
        "ncm8",
        "ncm_descr",
        "grupo_afinidade_final",
        "setor_principal_sbmi",
        "modulo_sbmi",
        "status_sbmi",
        "prioridade_sbmi",
    ]].copy()
    mapped_rows = int(out["grupo_afinidade_final"].notna().sum())
    mapped_unique = out.loc[out["grupo_afinidade_final"].notna(), "ncm8"].nunique()
    ncm_unique = out["ncm8"].nunique()
    return out, {
        "rows": len(out),
        "ncm8_unique": ncm_unique,
        "mapped_rows": mapped_rows,
        "mapped_rows_pct": mapped_rows / len(out) * 100.0 if len(out) else 0.0,
        "mapped_ncm8_unique": mapped_unique,
        "mapped_ncm8_pct": mapped_unique / ncm_unique * 100.0 if ncm_unique else 0.0,
    }


def _build_cesta(raw_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object]]:
    parts: list[pd.DataFrame] = []
    files = sorted(raw_dir.glob("public_dados_mensais_*.csv"))
    for file in files:
        frame = pd.read_csv(file, dtype="string", encoding="latin-1")
        frame = frame.loc[frame["Corede"].eq("FRONTEIRA OESTE")].copy()
        frame["data"] = pd.to_datetime(frame["Data"], format="%Y-%m-%d", errors="raise")
        frame["ano_mes"] = frame["data"].dt.strftime("%Y-%m")
        frame["vlr_unidade"] = pd.to_numeric(frame["VlrUnidade"], errors="coerce")
        frame["source_file"] = file.name
        parts.append(frame[["data", "ano_mes", "Corede", "NMProduto", "vlr_unidade", "source_file"]])
    out = pd.concat(parts, ignore_index=True).rename(
        columns={"Corede": "corede", "NMProduto": "produto"}
    )
    out["data"] = out["data"].dt.strftime("%Y-%m-%d")
    out = out.sort_values(["ano_mes", "produto"]).reset_index(drop=True)
    coverage = (
        out.groupby("ano_mes", as_index=False)
        .agg(
            rows=("produto", "size"),
            produtos_unicos=("produto", "nunique"),
            valores_ausentes=("vlr_unidade", lambda s: int(s.isna().sum())),
            valores_nao_positivos=("vlr_unidade", lambda s: int((s <= 0).sum())),
        )
        .sort_values("ano_mes")
    )
    return out, coverage, {
        "files": len(files),
        "rows": len(out),
        "months": out["ano_mes"].nunique(),
        "products": out["produto"].nunique(),
        "period_start": out["ano_mes"].min(),
        "period_end": out["ano_mes"].max(),
    }


def _build_dfe_municipality(curated_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object]]:
    file = curated_dir / "DFe_Sao_Borja_serie_completa.csv"
    frame = pd.read_csv(file, dtype="string", encoding="utf-8-sig")
    frame["dt_emissao"] = pd.to_datetime(frame["dt_emissao"], format="%Y-%m-%d", errors="raise")
    frame["ano_mes"] = frame["dt_emissao"].dt.strftime("%Y-%m")
    frame["qtde_dfe"] = pd.to_numeric(frame["qtde_dfe"], errors="coerce").astype("Int64")
    frame["vlr_total_dfe"] = _numeric_decimal_comma(frame["vlr_total_dfe"]).round(2)
    daily = frame[[
        "modelo_dfe",
        "dt_emissao",
        "ano_mes",
        "cod_municipio",
        "nome_municipio",
        "qtde_dfe",
        "vlr_total_dfe",
        "source_year",
    ]].copy()
    daily["dt_emissao"] = daily["dt_emissao"].dt.strftime("%Y-%m-%d")

    grouped = (
        frame.groupby(["ano_mes", "modelo_dfe"], as_index=False)
        .agg(
            data_inicio=("dt_emissao", "min"),
            data_fim=("dt_emissao", "max"),
            dias_cobertos=("dt_emissao", "nunique"),
            qtde_dfe=("qtde_dfe", "sum"),
            vlr_total_dfe=("vlr_total_dfe", "sum"),
        )
        .sort_values(["ano_mes", "modelo_dfe"])
    )
    grouped["dias_mes_calendario"] = grouped["ano_mes"].map(
        lambda p: calendar.monthrange(int(p[:4]), int(p[5:7]))[1]
    )
    grouped["cobertura_dias_pct"] = grouped["dias_cobertos"] / grouped["dias_mes_calendario"] * 100.0
    grouped["periodo_parcial"] = grouped["dias_cobertos"] < grouped["dias_mes_calendario"]
    grouped["data_inicio"] = pd.to_datetime(grouped["data_inicio"]).dt.strftime("%Y-%m-%d")
    grouped["data_fim"] = pd.to_datetime(grouped["data_fim"]).dt.strftime("%Y-%m-%d")
    grouped["vlr_total_dfe"] = grouped["vlr_total_dfe"].round(2)
    return daily, grouped, {
        "rows_daily": len(daily),
        "months": daily["ano_mes"].nunique(),
        "models": daily["modelo_dfe"].nunique(),
        "period_start": daily["ano_mes"].min(),
        "period_end": daily["ano_mes"].max(),
        "last_date": daily["dt_emissao"].max(),
    }


def _build_dfe_cnae(curated_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object]]:
    file = curated_dir / "DFe_CNAE_Classe_mensal_serie_completa.csv"
    frame = pd.read_csv(file, dtype="string", encoding="utf-8-sig")
    frame["ano_mes"] = frame["ano_mes"].astype("string")
    frame["cod_cnae_classe"] = frame["cod_cnae_classe"].astype("string").str.replace(r"\.0$", "", regex=True)
    frame["qtde_dfe"] = pd.to_numeric(frame["qtde_dfe"], errors="coerce").astype("Int64")
    frame["vlr_total_dfe"] = pd.to_numeric(frame["vlr_total_dfe"], errors="coerce").round(2)
    out = frame[[
        "ano_mes",
        "modelo_dfe",
        "cod_cnae_classe",
        "descricao_cnae",
        "qtde_dfe",
        "vlr_total_dfe",
        "source_year",
    ]].copy().sort_values(["ano_mes", "modelo_dfe", "cod_cnae_classe"])

    coverage = (
        out.groupby("ano_mes", as_index=False)
        .agg(
            rows=("cod_cnae_classe", "size"),
            cnaes_unicos=("cod_cnae_classe", "nunique"),
            modelos_unicos=("modelo_dfe", "nunique"),
            qtde_dfe_publicada=("qtde_dfe", "sum"),
            vlr_total_dfe_publicado=("vlr_total_dfe", "sum"),
        )
        .sort_values("ano_mes")
    )
    coverage["vlr_total_dfe_publicado"] = coverage["vlr_total_dfe_publicado"].round(2)
    return out, coverage, {
        "rows": len(out),
        "months": out["ano_mes"].nunique(),
        "cnaes": out["cod_cnae_classe"].nunique(),
        "models": out["modelo_dfe"].nunique(),
        "period_start": out["ano_mes"].min(),
        "period_end": out["ano_mes"].max(),
    }


def _validation_row(check: str, value: object, passed: bool, note: str) -> dict[str, object]:
    return {
        "check": check,
        "value": value,
        "status": "PASS" if passed else "FAIL",
        "note": note,
    }


def _build_catalog() -> pd.DataFrame:
    rows = [
        ["dim_ncm8_taxonomia_sbmi.csv", "dimensão", "Rio Grande do Sul / taxonomia", "NCM8", "Radar NCM completo + crosswalk SBMI", "associação taxonômica", "Usar para joins NCM→grupo→caderno; não contém valor monetário."],
        ["radar_composicao_rs_ncm_mensal.csv", "fato", "Rio Grande do Sul", "mês × NCM8 × UF emissor × tipo de operação", "Radar do Mercado — Composição de Mercado", "vlr_nominal conforme fonte", "Corte de sigilo deve ser preservado; zero sob sigilo não é zero econômico."],
        ["radar_composicao_rs_cobertura_mensal.csv", "controle", "Rio Grande do Sul", "mês", "Derivado calculado", "contagens e valor não suprimido", "Valor publicado não suprimido é piso observável, não dimensão integral do mercado."],
        ["radar_composicao_sbmi_grupo_mensal.csv", "benchmark", "Rio Grande do Sul", "mês × grupo SBMI × UF emissor × operação", "Derivado calculado", "valor publicado não suprimido", "Benchmark estadual; proibido atribuir diretamente a São Borja."],
        ["radar_exportacoes_rs_ncm_pais_mensal.csv", "fato", "Rio Grande do Sul", "mês × NCM8 × país", "Radar do Mercado — Exportações NCM", "vlr_fob conforme fonte", "NCM×país não é tratado como chave única global entre arquivos."],
        ["radar_exportacoes_sbmi_grupo_mensal.csv", "benchmark", "Rio Grande do Sul", "mês × grupo SBMI", "Derivado calculado", "vlr_fob publicado", "Contexto exportador; não é mercado consumidor municipal."],
        ["radar_ncm8_nao_classificados.csv", "controle", "Rio Grande do Sul", "série × NCM8", "Derivado calculado", "contagens/valores publicados", "Inventário dos NCM8 presentes nas séries mas ausentes do catálogo de 110 grupos; não imputar grupo automaticamente."],
        ["radar_portfolio_ncm_setor_normalizado.csv", "dimensão auxiliar", "Rio Grande do Sul", "associação NCM8 × classe/setor", "Radar Portfólio NCM/Setor", "classificação", "NCM pode aparecer em várias associações no Portfólio."],
        ["cesta_fronteira_oeste_produto_mensal.csv", "fato", "COREDE Fronteira Oeste", "mês × produto", "Cesta Alimentos — Receita Estadual RS", "VlrUnidade conforme fonte", "COREDE não deve ser rotulado como município de São Borja."],
        ["cesta_fronteira_oeste_cobertura_mensal.csv", "controle", "COREDE Fronteira Oeste", "mês", "Derivado calculado", "contagens", "Controle de completude; não constitui índice de preços calculado."],
        ["dfe_sao_borja_diario.csv", "fato", "São Borja/RS", "dia × modelo DFe", "DFe — Receita Estadual RS", "qtde_dfe e vlr_total_dfe", "Envelope fiscal local por modelo; não identifica mercado por produto."],
        ["dfe_sao_borja_modelo_mensal.csv", "benchmark local", "São Borja/RS", "mês × modelo DFe", "Derivado calculado", "qtde_dfe e vlr_total_dfe", "Não somar modelos para market share sem regra conceitual adicional."],
        ["dfe_rs_cnae_mensal.csv", "fato", "Rio Grande do Sul", "mês × modelo DFe × CNAE classe", "DFe CNAE — Receita Estadual RS", "qtde_dfe e vlr_total_dfe", "Benchmark estadual; não ratear para São Borja."],
        ["dfe_rs_cnae_cobertura_mensal.csv", "controle", "Rio Grande do Sul", "mês", "Derivado calculado", "contagens e totais publicados", "Totais são estaduais e servem apenas a controle/benchmark."],
    ]
    return pd.DataFrame(rows, columns=["arquivo", "tipo", "geografia", "granularidade", "fonte", "unidade_medida", "limitacao_uso"])


def _build_manifest(output_dir: Path, data_files: Iterable[Path]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for path in sorted(data_files, key=lambda item: item.name):
        try:
            with path.open("r", encoding="utf-8") as handle:
                row_count = max(sum(1 for _ in handle) - 1, 0)
        except UnicodeDecodeError:
            row_count = pd.NA
        rows.append(
            {
                "file": path.name,
                "bytes": path.stat().st_size,
                "sha256": _sha256(path),
                "rows": row_count,
            }
        )
    return pd.DataFrame(rows)


def build_curated_public_market_series(
    public_series_root: Path,
    taxonomy_csv: Path,
    crosswalk_md: Path,
    output_dir: Path,
    *,
    execution_id: str,
    source_run_id: str,
    taxonomy_run_id: str,
) -> CuratedBuildResult:
    root = Path(public_series_root)
    target = Path(output_dir)
    if target.exists():
        raise FileExistsError(f"Diretório de saída já existe: {target}")
    target.mkdir(parents=True)

    dim_ncm = _read_taxonomy(taxonomy_csv, crosswalk_md)
    dim_ncm.to_csv(target / "dim_ncm8_taxonomia_sbmi.csv", index=False, encoding="utf-8")

    comp_cov, comp_group, comp_unmapped, comp_meta = _build_radar_composition(root / "raw_radar", dim_ncm, target)
    comp_cov.to_csv(target / "radar_composicao_rs_cobertura_mensal.csv", index=False, encoding="utf-8", float_format="%.4f")
    comp_group.to_csv(target / "radar_composicao_sbmi_grupo_mensal.csv", index=False, encoding="utf-8", float_format="%.2f")

    exp_cov, exp_group, exp_unmapped, exp_meta = _build_radar_exports(root / "raw_radar", dim_ncm, target)
    exp_cov.to_csv(target / "radar_exportacoes_rs_cobertura_mensal.csv", index=False, encoding="utf-8", float_format="%.2f")
    exp_group.to_csv(target / "radar_exportacoes_sbmi_grupo_mensal.csv", index=False, encoding="utf-8", float_format="%.2f")

    comp_unmapped = comp_unmapped.rename(columns={"vlr_publicado_nao_sigilo": "valor_publicado"}).assign(
        series="radar_composicao_mercado",
        metrica_valor="vlr_nominal_publicado_nao_sigilo",
    )
    exp_unmapped = exp_unmapped.rename(columns={"vlr_publicado": "valor_publicado"}).assign(
        series="radar_exportacoes_ncm",
        metrica_valor="vlr_fob_publicado",
        rows_corte_sigilo=pd.NA,
    )
    unmapped_all = pd.concat([comp_unmapped, exp_unmapped], ignore_index=True, sort=False)
    unmapped_all = unmapped_all[[
        "series",
        "ncm8",
        "first_month",
        "last_month",
        "rows",
        "rows_corte_sigilo",
        "metrica_valor",
        "valor_publicado",
    ]]
    unmapped_all.to_csv(
        target / "radar_ncm8_nao_classificados.csv",
        index=False,
        encoding="utf-8",
        float_format="%.2f",
    )

    portfolio, portfolio_meta = _build_portfolio(root / "raw_radar", dim_ncm)
    portfolio.to_csv(target / "radar_portfolio_ncm_setor_normalizado.csv", index=False, encoding="utf-8")

    cesta, cesta_cov, cesta_meta = _build_cesta(root / "raw_cesta")
    cesta.to_csv(target / "cesta_fronteira_oeste_produto_mensal.csv", index=False, encoding="utf-8", float_format="%.10f")
    cesta_cov.to_csv(target / "cesta_fronteira_oeste_cobertura_mensal.csv", index=False, encoding="utf-8")

    dfe_sb_daily, dfe_sb_monthly, dfe_sb_meta = _build_dfe_municipality(root / "curated_dfe_municipio")
    dfe_sb_daily.to_csv(target / "dfe_sao_borja_diario.csv", index=False, encoding="utf-8", float_format="%.2f")
    dfe_sb_monthly.to_csv(target / "dfe_sao_borja_modelo_mensal.csv", index=False, encoding="utf-8", float_format="%.2f")

    dfe_cnae, dfe_cnae_cov, dfe_cnae_meta = _build_dfe_cnae(root / "curated_dfe_cnae")
    dfe_cnae.to_csv(target / "dfe_rs_cnae_mensal.csv", index=False, encoding="utf-8", float_format="%.2f")
    dfe_cnae_cov.to_csv(target / "dfe_rs_cnae_cobertura_mensal.csv", index=False, encoding="utf-8", float_format="%.2f")

    catalog = _build_catalog()
    catalog.to_csv(target / "series_catalog_v001.csv", index=False, encoding="utf-8")

    validation_rows = [
        _validation_row("taxonomy_ncm8_unique", dim_ncm["ncm8"].nunique(), dim_ncm["ncm8"].nunique() == 11765, "Taxonomia canônica esperada: 11.765 NCM8."),
        _validation_row("taxonomy_groups", dim_ncm["grupo_afinidade_final"].nunique(), dim_ncm["grupo_afinidade_final"].nunique() == 110, "Universo canônico do Radar: 110 grupos."),
        _validation_row("radar_composition_files", comp_meta["files"], comp_meta["files"] == 26, "Cobertura esperada: 2024-07 a 2026-08."),
        _validation_row("radar_composition_taxonomy_coverage_pct", f"{comp_meta['taxonomy_row_coverage_pct']:.6f}", comp_meta["taxonomy_row_coverage_pct"] > 95.0, "Cobertura de linhas deve permanecer acima de 95%; ausências são inventariadas separadamente."),
        _validation_row("radar_composition_unmapped_ncm8", len(comp_unmapped), len(comp_unmapped) == 2200, "NCM8 presentes na Composição e ausentes do catálogo canônico de 110 grupos."),
        _validation_row("radar_export_files", exp_meta["files"], exp_meta["files"] == 26, "Cobertura esperada: 2024-07 a 2026-08."),
        _validation_row("radar_export_taxonomy_coverage_pct", f"{exp_meta['taxonomy_row_coverage_pct']:.6f}", exp_meta["taxonomy_row_coverage_pct"] > 99.0, "Cobertura de linhas deve permanecer acima de 99%; ausências são inventariadas separadamente."),
        _validation_row("radar_export_unmapped_ncm8", len(exp_unmapped), len(exp_unmapped) == 126, "NCM8 presentes nas Exportações e ausentes do catálogo canônico de 110 grupos."),
        _validation_row("portfolio_rows", portfolio_meta["rows"], portfolio_meta["rows"] == 1900, "Snapshot auditado do Portfólio."),
        _validation_row("portfolio_taxonomy_coverage_pct", f"{portfolio_meta['mapped_ncm8_pct']:.6f}", portfolio_meta["mapped_ncm8_pct"] > 98.0, "Cobertura conhecida ~98,81%."),
        _validation_row("cesta_months", cesta_meta["months"], cesta_meta["months"] == 66, "2021-01 a 2026-06."),
        _validation_row("cesta_products", cesta_meta["products"], cesta_meta["products"] == 80, "80 produtos por mês na Fronteira Oeste."),
        _validation_row("cesta_monthly_rows", int(cesta_cov["rows"].min()), cesta_cov["rows"].eq(80).all(), "Cada mês deve conter 80 produtos."),
        _validation_row("dfe_sao_borja_code", dfe_sb_daily["cod_municipio"].nunique(), dfe_sb_daily["cod_municipio"].astype(str).eq("4318002").all(), "Somente São Borja, código 4318002."),
        _validation_row("dfe_sao_borja_last_date", dfe_sb_meta["last_date"], dfe_sb_meta["last_date"] == "2026-09-14", "Corte observado no pacote-fonte."),
        _validation_row("dfe_cnae_period_end", dfe_cnae_meta["period_end"], dfe_cnae_meta["period_end"] == "2026-09", "Após correção do parser, não deve haver meses espúrios."),
        _validation_row("dfe_cnae_rows", dfe_cnae_meta["rows"], dfe_cnae_meta["rows"] == 71491, "Quantidade auditada no run canônico."),
    ]
    validation = pd.DataFrame(validation_rows)
    validation.to_csv(target / "validation.csv", index=False, encoding="utf-8")
    failed = validation.loc[validation["status"] != "PASS"]
    if not failed.empty:
        raise ValueError(f"Validações falharam: {failed.to_dict(orient='records')}")

    summary: dict[str, object] = {
        "execution_id": execution_id,
        "source_run_id": source_run_id,
        "taxonomy_run_id": taxonomy_run_id,
        "geographic_layers": ["São Borja/RS", "COREDE Fronteira Oeste", "Rio Grande do Sul"],
        "radar_composition": {**comp_meta, "unmapped_ncm8": len(comp_unmapped)},
        "radar_exports": {**exp_meta, "unmapped_ncm8": len(exp_unmapped)},
        "radar_portfolio": portfolio_meta,
        "cesta_fronteira_oeste": cesta_meta,
        "dfe_sao_borja": dfe_sb_meta,
        "dfe_cnae_rs": dfe_cnae_meta,
        "governance": {
            "radar_suppressed_zero_rule": "zero com corte_sigilo=1 é censura, não zero econômico",
            "corede_rule": "COREDE Fronteira Oeste não é dado municipal de São Borja",
            "state_benchmark_rule": "benchmarks estaduais não podem ser rateados ad hoc para São Borja",
            "dfe_model_rule": "modelos DFe não são somados para market share sem regra conceitual adicional",
        },
    }
    (target / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

    run_metadata = pd.DataFrame(
        [
            ["execution_id", execution_id, "parameter"],
            ["source_run_id", source_run_id, "source_lineage"],
            ["taxonomy_run_id", taxonomy_run_id, "source_lineage"],
            ["source_scope", "Radar + Cesta + DFe públicos da Receita Estadual/RS", "observed_source"],
            ["geography_rule", "São Borja / COREDE Fronteira Oeste / RS permanecem separados", "governance"],
            ["suppression_rule", "corte_sigilo=1 não é zero econômico", "governance"],
            ["normalization_rule", "ano_mes Radar derivado do nome do arquivo; anomes_fonte preservado", "method"],
            ["monetary_rule", "DFe arredondado a 2 casas; Cesta preservada a 10 casas; Radar conforme fonte", "method"],
        ],
        columns=["field", "value", "nature"],
    )
    run_metadata.to_csv(target / "run_metadata.csv", index=False, encoding="utf-8")

    files_for_manifest = [p for p in target.iterdir() if p.is_file() and p.name != "manifest_curated.csv"]
    manifest = _build_manifest(target, files_for_manifest)
    manifest.to_csv(target / "manifest_curated.csv", index=False, encoding="utf-8")
    return CuratedBuildResult(target, validation, manifest, summary)