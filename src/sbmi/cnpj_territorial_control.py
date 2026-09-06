"""Curadoria territorial de matriz/filial a partir dos Dados Abertos CNPJ da RFB."""

from __future__ import annotations

import csv
import hashlib
import shutil
import zipfile
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

MUNICIPALITY_TOM_SAO_BORJA = "8863"
MUNICIPALITY_IBGE_SAO_BORJA = 4318002
ACTIVE_STATUS_CODE = "02"

ESTABLISHMENT_COLUMNS = [
    "cnpj_basico",
    "cnpj_ordem",
    "cnpj_dv",
    "identificador_matriz_filial",
    "nome_fantasia",
    "situacao_cadastral",
    "data_situacao_cadastral",
    "motivo_situacao_cadastral",
    "nome_cidade_exterior",
    "pais",
    "data_inicio_atividade",
    "cnae_fiscal_principal",
    "cnae_fiscal_secundaria",
    "tipo_logradouro",
    "logradouro",
    "numero",
    "complemento",
    "bairro",
    "cep",
    "uf",
    "municipio",
    "ddd_1",
    "telefone_1",
    "ddd_2",
    "telefone_2",
    "ddd_fax",
    "fax",
    "correio_eletronico",
    "situacao_especial",
    "data_situacao_especial",
]

COMPANY_COLUMNS = [
    "cnpj_basico",
    "razao_social",
    "natureza_juridica",
    "qualificacao_responsavel",
    "capital_social",
    "porte_empresa",
    "ente_federativo_responsavel",
]

MUNICIPALITY_COLUMNS = ["municipio", "municipio_nome"]


@dataclass(frozen=True)
class CnpjTerritorialResult:
    establishments: pd.DataFrame
    by_division: pd.DataFrame
    by_size: pd.DataFrame
    validation: pd.DataFrame
    manifest: pd.DataFrame
    paths: dict[str, Path]


def _target(root: Path, identifier: str) -> tuple[Path, Path]:
    if not identifier or Path(identifier).name != identifier:
        raise ValueError("Identificador inválido")
    target = root.resolve() / identifier
    partial = target.with_name(f".{identifier}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(target)
    return target, partial


def _zip_paths(value: Path | Iterable[Path], prefix: str) -> list[Path]:
    if isinstance(value, Path):
        paths = sorted(value.glob(f"{prefix}*.zip")) if value.is_dir() else [value]
    else:
        paths = sorted(Path(p) for p in value)
    if not paths:
        raise FileNotFoundError(f"Nenhum arquivo {prefix}*.zip encontrado")
    missing = [p for p in paths if not p.exists()]
    if missing:
        raise FileNotFoundError(missing[0])
    return paths


def _iter_zip_chunks(
    zip_paths: Iterable[Path],
    columns: list[str],
    *,
    chunksize: int,
) -> Iterable[pd.DataFrame]:
    for zip_path in zip_paths:
        with zipfile.ZipFile(zip_path) as zf:
            members = [m for m in zf.namelist() if not m.endswith("/")]
            if not members:
                raise ValueError(f"ZIP sem conteúdo tabular: {zip_path}")
            for member in members:
                with zf.open(member) as fh:
                    yield from pd.read_csv(
                        fh,
                        sep=";",
                        header=None,
                        names=columns,
                        dtype="string",
                        encoding="latin1",
                        keep_default_na=False,
                        na_filter=False,
                        quoting=csv.QUOTE_MINIMAL,
                        chunksize=chunksize,
                        low_memory=False,
                    )


def _full_cnpj(frame: pd.DataFrame) -> pd.Series:
    return (
        frame["cnpj_basico"].str.zfill(8)
        + frame["cnpj_ordem"].str.zfill(4)
        + frame["cnpj_dv"].str.zfill(2)
    )


def _collect_local_establishments(
    zip_paths: list[Path],
    *,
    municipality_tom: str,
    active_status_code: str,
    chunksize: int,
) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for chunk in _iter_zip_chunks(zip_paths, ESTABLISHMENT_COLUMNS, chunksize=chunksize):
        mask = (chunk["municipio"] == municipality_tom) & (
            chunk["situacao_cadastral"] == active_status_code
        )
        if mask.any():
            frames.append(chunk.loc[mask].copy())
    if not frames:
        raise ValueError("Nenhum estabelecimento ativo encontrado para o município")
    result = pd.concat(frames, ignore_index=True)
    result["cnpj"] = _full_cnpj(result)
    return result


def _collect_companies(
    zip_paths: list[Path],
    roots: set[str],
    *,
    chunksize: int,
) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for chunk in _iter_zip_chunks(zip_paths, COMPANY_COLUMNS, chunksize=chunksize):
        mask = chunk["cnpj_basico"].isin(roots)
        if mask.any():
            frames.append(chunk.loc[mask].copy())
    if not frames:
        raise ValueError("Nenhuma empresa correspondente às raízes locais foi encontrada")
    result = pd.concat(frames, ignore_index=True)
    if result["cnpj_basico"].duplicated().any():
        raise ValueError("Raiz CNPJ duplicada nos arquivos de empresas")
    return result


def _collect_matrices(
    zip_paths: list[Path],
    roots: set[str],
    *,
    active_status_code: str,
    chunksize: int,
) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for chunk in _iter_zip_chunks(zip_paths, ESTABLISHMENT_COLUMNS, chunksize=chunksize):
        mask = (
            chunk["cnpj_basico"].isin(roots)
            & (chunk["identificador_matriz_filial"] == "1")
            & (chunk["situacao_cadastral"] == active_status_code)
        )
        if mask.any():
            frames.append(chunk.loc[mask].copy())
    if not frames:
        return pd.DataFrame(columns=ESTABLISHMENT_COLUMNS + ["matrix_cnpj"])
    result = pd.concat(frames, ignore_index=True)
    result["matrix_cnpj"] = _full_cnpj(result)
    counts = result.groupby("cnpj_basico").size()
    if (counts > 1).any():
        raise ValueError("Mais de uma matriz ativa encontrada para a mesma raiz CNPJ")
    return result


def _read_municipalities(zip_path: Path) -> pd.DataFrame:
    if not zip_path.exists():
        raise FileNotFoundError(zip_path)
    frames = list(_iter_zip_chunks([zip_path], MUNICIPALITY_COLUMNS, chunksize=100_000))
    if not frames:
        raise ValueError("Tabela de municípios vazia")
    result = pd.concat(frames, ignore_index=True)
    if result["municipio"].duplicated().any():
        raise ValueError("Código de município duplicado")
    return result


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def curate_cnpj_territorial_control(
    *,
    establishments: Path | Iterable[Path],
    companies: Path | Iterable[Path],
    municipalities_zip: Path,
    roots: dict[str, Path],
    execution_id: str,
    municipality_tom: str = MUNICIPALITY_TOM_SAO_BORJA,
    municipality_ibge: int = MUNICIPALITY_IBGE_SAO_BORJA,
    active_status_code: str = ACTIVE_STATUS_CODE,
    chunksize: int = 200_000,
) -> CnpjTerritorialResult:
    """Classifica estabelecimentos locais pelo município da matriz oficial."""
    if set(roots) != {"staging", "curated", "exports", "audit"}:
        raise ValueError("Camadas obrigatórias ausentes")
    targets = {layer: _target(root, execution_id) for layer, root in roots.items()}
    establishment_zips = _zip_paths(establishments, "Estabelecimentos")
    company_zips = _zip_paths(companies, "Empresas")

    local = _collect_local_establishments(
        establishment_zips,
        municipality_tom=municipality_tom,
        active_status_code=active_status_code,
        chunksize=chunksize,
    )
    cnpj_roots = set(local["cnpj_basico"])
    company = _collect_companies(company_zips, cnpj_roots, chunksize=chunksize)
    matrices = _collect_matrices(
        establishment_zips,
        cnpj_roots,
        active_status_code=active_status_code,
        chunksize=chunksize,
    )
    municipalities = _read_municipalities(municipalities_zip)

    company_keep = company[
        ["cnpj_basico", "razao_social", "natureza_juridica", "capital_social", "porte_empresa"]
    ].copy()
    matrix_keep = matrices[["cnpj_basico", "matrix_cnpj", "municipio", "uf"]].rename(
        columns={"municipio": "matrix_municipality_tom", "uf": "matrix_uf"}
    )

    result = local.merge(company_keep, on="cnpj_basico", how="left", validate="many_to_one")
    result = result.merge(matrix_keep, on="cnpj_basico", how="left", validate="many_to_one")
    result = result.merge(
        municipalities.rename(
            columns={
                "municipio": "matrix_municipality_tom",
                "municipio_nome": "matrix_municipality_name",
            }
        ),
        on="matrix_municipality_tom",
        how="left",
        validate="many_to_one",
    )
    result["municipality_ibge"] = municipality_ibge
    result["cnae_division"] = result["cnae_fiscal_principal"].str[:2]
    result["matrix_branch_label"] = (
        result["identificador_matriz_filial"]
        .map({"1": "MATRIZ", "2": "FILIAL"})
        .fillna("DESCONHECIDO")
    )
    result["territorial_control_status"] = "INDETERMINADO"
    is_local_matrix = result["identificador_matriz_filial"] == "1"
    is_branch = result["identificador_matriz_filial"] == "2"
    matrix_local = result["matrix_municipality_tom"] == municipality_tom
    matrix_known = result["matrix_municipality_tom"].fillna("") != ""
    result.loc[is_local_matrix, "territorial_control_status"] = "MATRIZ_LOCAL"
    result.loc[is_branch & matrix_local, "territorial_control_status"] = "FILIAL_DE_MATRIZ_LOCAL"
    result.loc[
        is_branch & matrix_known & ~matrix_local, "territorial_control_status"
    ] = "FILIAL_DE_MATRIZ_EXTERNA"
    result.loc[is_branch & ~matrix_known, "territorial_control_status"] = (
        "FILIAL_MATRIZ_NAO_LOCALIZADA"
    )
    result["nature"] = "observed_rfb"
    result["source_scope"] = "Dados Abertos CNPJ — estabelecimento ativo em São Borja"

    keep = [
        "cnpj",
        "cnpj_basico",
        "cnpj_ordem",
        "cnpj_dv",
        "identificador_matriz_filial",
        "matrix_branch_label",
        "razao_social",
        "nome_fantasia",
        "cnae_fiscal_principal",
        "cnae_division",
        "porte_empresa",
        "capital_social",
        "uf",
        "municipio",
        "municipality_ibge",
        "matrix_cnpj",
        "matrix_municipality_tom",
        "matrix_municipality_name",
        "matrix_uf",
        "territorial_control_status",
        "nature",
        "source_scope",
    ]
    result = (
        result[keep]
        .sort_values(["territorial_control_status", "cnpj"])
        .reset_index(drop=True)
    )

    status_order = [
        "MATRIZ_LOCAL",
        "FILIAL_DE_MATRIZ_LOCAL",
        "FILIAL_DE_MATRIZ_EXTERNA",
        "FILIAL_MATRIZ_NAO_LOCALIZADA",
        "INDETERMINADO",
    ]
    by_division = (
        result.groupby(["cnae_division", "territorial_control_status"], dropna=False)
        .size()
        .unstack(fill_value=0)
        .reindex(columns=status_order, fill_value=0)
        .reset_index()
    )
    by_division["total_establishments"] = by_division[status_order].sum(axis=1)
    by_division["external_matrix_share"] = (
        by_division["FILIAL_DE_MATRIZ_EXTERNA"] / by_division["total_establishments"]
    )

    by_size = (
        result.groupby(["porte_empresa", "territorial_control_status"], dropna=False)
        .size()
        .unstack(fill_value=0)
        .reindex(columns=status_order, fill_value=0)
        .reset_index()
    )
    by_size["total_establishments"] = by_size[status_order].sum(axis=1)
    by_size["external_matrix_share"] = (
        by_size["FILIAL_DE_MATRIZ_EXTERNA"] / by_size["total_establishments"]
    )

    duplicate_cnpjs = int(result["cnpj"].duplicated().sum())
    matrix_missing = int(
        (
            (result["identificador_matriz_filial"] == "2")
            & (result["matrix_municipality_tom"].fillna("") == "")
        ).sum()
    )
    invalid_identifiers = sorted(set(result["identificador_matriz_filial"]) - {"1", "2"})
    validation = pd.DataFrame(
        [
            ("rows", len(result), "calculated", "PASS"),
            (
                "duplicate_cnpjs",
                duplicate_cnpjs,
                "calculated",
                "PASS" if not duplicate_cnpjs else "FAIL",
            ),
            (
                "municipality_tom_values",
                result["municipio"].nunique(),
                "calculated",
                "PASS" if set(result["municipio"]) == {municipality_tom} else "FAIL",
            ),
            (
                "invalid_matrix_branch_identifiers",
                len(invalid_identifiers),
                "calculated",
                "PASS" if not invalid_identifiers else "FAIL",
            ),
            (
                "branch_matrices_not_located",
                matrix_missing,
                "calculated",
                "WARN" if matrix_missing else "PASS",
            ),
            (
                "company_join_missing",
                int(result["razao_social"].isna().sum()),
                "calculated",
                "PASS",
            ),
        ],
        columns=["indicator", "value", "nature", "status"],
    )
    if "FAIL" in set(validation["status"]):
        raise ValueError("Validação do controle territorial falhou")

    source_paths = [*establishment_zips, *company_zips, municipalities_zip]
    manifest = pd.DataFrame(
        [
            {
                "source_file": path.name,
                "bytes": path.stat().st_size,
                "sha256": _sha256(path),
                "declared_source": "Receita Federal — Dados Abertos CNPJ",
                "nature": "observed",
            }
            for path in source_paths
        ]
    )

    for _, partial in targets.values():
        partial.mkdir(parents=True)

    try:
        result.to_csv(
            targets["staging"][1] / "cnpj_territorial_control_staging.csv", index=False
        )
        result.to_csv(targets["curated"][1] / "cnpj_territorial_control.csv", index=False)
        by_division.to_csv(
            targets["exports"][1] / "cnpj_territorial_control_by_division.csv", index=False
        )
        by_size.to_csv(
            targets["exports"][1] / "cnpj_territorial_control_by_size.csv", index=False
        )
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

    return CnpjTerritorialResult(
        establishments=result,
        by_division=by_division,
        by_size=by_size,
        validation=validation,
        manifest=manifest,
        paths={k: v[0] for k, v in targets.items()},
    )
