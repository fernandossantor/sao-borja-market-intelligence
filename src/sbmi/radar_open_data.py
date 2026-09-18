"""Auditoria exploratória dos CSVs públicos do Radar de Mercado/Receita RS.

Este módulo não promove dados para camadas canônicas. Ele inventaria schemas,
filtra a cesta-piloto de NCMs do arroz e calcula apenas métricas explicitamente
definidas na NT CIET 05/2026 quando os campos necessários estão presentes.
"""
from __future__ import annotations

import hashlib
import re
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

RICE_NCMS = (
    "10062010",
    "10062020",
    "10063011",
    "10063019",
    "10063021",
    "10063029",
    "10064000",
)

RICE_NCM_DESCRIPTIONS = {
    "10062010": "Arroz descascado (cargo/castanho), parboilizado",
    "10062020": "Arroz descascado (cargo/castanho), não parboilizado",
    "10063011": "Arroz semibranqueado ou branqueado, parboilizado, polido ou brunido",
    "10063019": "Outros tipos de arroz semibranqueado ou branqueado, parboilizado",
    "10063021": "Arroz semibranqueado ou branqueado, não parboilizado, polido ou brunido",
    "10063029": "Outros tipos de arroz semibranqueado ou branqueado, não parboilizado",
    "10064000": "Arroz quebrado",
}

_COLUMN_ALIASES = {
    "ncm": {"ncm", "co_ncm", "codigo_ncm", "cod_ncm", "codigo_do_ncm"},
    "period": {
        "ano_mes",
        "anomes",
        "ano_mes_referencia",
        "mes_ano",
        "periodo",
        "referencia",
        "competencia",
    },
    "value": {
        "valor",
        "valor_rs",
        "valor_r",
        "valor_milhoes",
        "vl_nfe",
        "valor_nominal",
        "vl_fob",
    },
    "origin_type": {
        "origem",
        "tipo_origem",
        "origem_mercado",
        "tipo_operacao",
        "tipo_de_operacao",
        "mercado",
    },
    "int": {"int", "producao_interna", "producao_int", "vendas_internas", "internas"},
    "ouf": {"ouf", "entradas_ouf", "compras_interestaduais", "interestadual"},
    "ext": {"ext", "entradas_ext", "importacoes", "importacao", "exterior"},
}

_ORIGIN_VALUE_ALIASES = {
    "INT": {"int", "interno", "interna", "internas", "producao_interna", "producao_int"},
    "OUF": {"ouf", "outras_ufs", "outras_uf", "interestadual", "interestaduais"},
    "EXT": {"ext", "exterior", "importacao", "importacoes"},
}


@dataclass(frozen=True)
class RadarOpenDataAuditResult:
    output_path: Path
    schema_inventory: pd.DataFrame
    ncm_matches: pd.DataFrame
    composition_summary: pd.DataFrame
    validation: pd.DataFrame
    limitations: pd.DataFrame


def _normalize(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text).strip("_")
    return text


def _read_csv(path: Path) -> tuple[pd.DataFrame, str, str]:
    errors: list[str] = []
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            frame = pd.read_csv(path, sep=None, engine="python", encoding=encoding, dtype=str)
            return frame, encoding, "sniffed"
        except Exception as exc:
            errors.append(f"{encoding}: {type(exc).__name__}: {exc}")
    raise ValueError(f"Falha ao ler {path.name}: {' | '.join(errors)}")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _column_map(columns: list[object]) -> dict[str, str]:
    normalized = {_normalize(col): str(col) for col in columns}
    mapping: dict[str, str] = {}
    for concept, aliases in _COLUMN_ALIASES.items():
        hits = [normalized[name] for name in aliases if name in normalized]
        if len(hits) == 1:
            mapping[concept] = hits[0]
        elif len(hits) > 1:
            mapping[concept] = sorted(hits)[0]
    return mapping


def _clean_ncm(series: pd.Series) -> pd.Series:
    return series.astype("string").str.replace(r"\D", "", regex=True).str.zfill(8)


def _to_number(series: pd.Series) -> pd.Series:
    s = series.astype("string").str.strip()
    both = s.str.contains(",", regex=False, na=False) & s.str.contains(".", regex=False, na=False)
    s = s.where(~both, s.str.replace(".", "", regex=False).str.replace(",", ".", regex=False))
    comma_only = (
        s.str.contains(",", regex=False, na=False)
        & ~s.str.contains(".", regex=False, na=False)
    )
    s = s.where(~comma_only, s.str.replace(",", ".", regex=False))
    s = s.str.replace(r"[^0-9eE+\-.]", "", regex=True)
    return pd.to_numeric(s, errors="coerce")


def _dependency(part_rs: float | None) -> str:
    if part_rs is None or pd.isna(part_rs):
        return "NAO_CALCULADO"
    if part_rs < 0.05:
        return "CRITICA"
    if part_rs < 0.15:
        return "ALTA"
    if part_rs < 0.30:
        return "MEDIA"
    return "FORA_DAS_FAIXAS_NT"


def _classify_file(path: Path, mapping: dict[str, str]) -> str:
    name = _normalize(path.stem)
    if "categoria" in name:
        return "categorias_produtos"
    if "portfolio" in name:
        return "portfolio_ncm_setor"
    if "export" in name and "ncm" in name:
        return "exportacoes_ncm"
    if "import" in name and "ncm" in name:
        return "importacoes_ncm"
    if "composicao" in name or "composicao_de_mercado" in name:
        return "composicao_mercado"
    if "saida" in name and "setor" in name:
        return "saidas_setor"
    if "ncm" in mapping and "vl_fob" in {_normalize(c) for c in mapping.values()}:
        return "ncm_comercio_exterior_nao_classificado"
    return "desconhecido"


def _summarize_composition(
    frame: pd.DataFrame, mapping: dict[str, str], source_file: str
) -> pd.DataFrame:
    if "ncm" not in mapping:
        return pd.DataFrame()
    work = frame.copy()
    work["_ncm"] = _clean_ncm(work[mapping["ncm"]])
    work = work[work["_ncm"].isin(ncm_basket)].copy()
    if work.empty:
        return pd.DataFrame()

    wide = {key: mapping[key] for key in ("int", "ouf", "ext") if key in mapping}
    if len(wide) == 3:
        for key, column in wide.items():
            work[f"_{key}"] = _to_number(work[column])
        grouped = work.groupby("_ncm", dropna=False)[["_int", "_ouf", "_ext"]].sum(min_count=1)
    elif "origin_type" in mapping and "value" in mapping:
        work["_value"] = _to_number(work[mapping["value"]])
        work["_origin_norm"] = work[mapping["origin_type"]].map(_normalize)
        reverse = {
            alias: standard
            for standard, aliases in _ORIGIN_VALUE_ALIASES.items()
            for alias in aliases
        }
        work["_origin"] = work["_origin_norm"].map(reverse)
        work = work[work["_origin"].notna()].copy()
        if work.empty:
            return pd.DataFrame()
        pivot = work.pivot_table(
            index="_ncm", columns="_origin", values="_value", aggfunc="sum", fill_value=0
        )
        for col in ("INT", "OUF", "EXT"):
            if col not in pivot.columns:
                pivot[col] = 0.0
        grouped = pivot[["INT", "OUF", "EXT"]].rename(
            columns={"INT": "_int", "OUF": "_ouf", "EXT": "_ext"}
        )
    else:
        return pd.DataFrame()

    out = grouped.reset_index().rename(
        columns={"_ncm": "ncm", "_int": "int_rs", "_ouf": "ouf", "_ext": "ext"}
    )
    out["demanda_rs"] = out[["int_rs", "ouf", "ext"]].sum(axis=1, min_count=1)
    out["part_rs"] = out["int_rs"] / out["demanda_rs"].where(out["demanda_rs"] != 0)
    out["dependencia_nt"] = out["part_rs"].map(_dependency)
    out["descricao_ncm"] = out["ncm"].map(ncm_basket)
    out["source_file"] = source_file
    out["natureza"] = "DADO_CALCULADO_SOBRE_DADO_OBSERVADO"
    out["formula_part_rs"] = "INT/(INT+OUF+EXT) — NT CIET 05/2026"
    return out[[
        "ncm", "descricao_ncm", "int_rs", "ouf", "ext", "demanda_rs", "part_rs",
        "dependencia_nt", "source_file", "natureza", "formula_part_rs",
    ]]


def audit_radar_open_data(
    *, source_dir: Path, output_root: Path, execution_id: str
) -> RadarOpenDataAuditResult:
    if not execution_id or Path(execution_id).name != execution_id:
        raise ValueError("execution_id deve ser um identificador simples")
    source_dir = source_dir.resolve()
    if not source_dir.is_dir():
        raise FileNotFoundError(f"Diretório de origem inexistente: {source_dir}")
    files = sorted(
        path
        for path in source_dir.iterdir()
        if path.is_file() and path.suffix.lower() == ".csv"
    )
    if not files:
        raise FileNotFoundError(f"Nenhum CSV encontrado em {source_dir}")

    target = output_root.resolve() / execution_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")

    schema_rows: list[dict[str, object]] = []
    match_frames: list[pd.DataFrame] = []
    composition_frames: list[pd.DataFrame] = []
    limitation_rows: list[dict[str, object]] = []

    for path in files:
        try:
            frame, encoding, separator_mode = _read_csv(path)
        except Exception as exc:
            schema_rows.append({
                "source_file": path.name,
                "sha256": _sha256(path),
                "status": "READ_ERROR",
                "rows": None,
                "columns": None,
                "encoding": None,
                "separator_mode": None,
                "file_type": "desconhecido",
                "column_mapping": "",
                "raw_columns": "",
                "error": str(exc),
            })
            continue

        mapping = _column_map(list(frame.columns))
        file_type = _classify_file(path, mapping)
        schema_rows.append({
            "source_file": path.name,
            "sha256": _sha256(path),
            "status": "READ_OK",
            "rows": len(frame),
            "columns": len(frame.columns),
            "encoding": encoding,
            "separator_mode": separator_mode,
            "file_type": file_type,
            "column_mapping": " | ".join(f"{k}={v}" for k, v in sorted(mapping.items())),
            "raw_columns": " | ".join(map(str, frame.columns)),
            "error": "",
        })

        if "ncm" not in mapping:
            limitation_rows.append({
                "source_file": path.name,
                "code": "NCM_COLUMN_NOT_IDENTIFIED",
                "description": (
                    "Arquivo não possui coluna NCM identificável pelos aliases "
                    "auditáveis."
                ),
            })
            continue

        work = frame.copy()
        work["_ncm"] = _clean_ncm(work[mapping["ncm"]])
        matches = work[work["_ncm"].isin(basket)].copy()
        if not matches.empty:
            matches.insert(0, "source_file", path.name)
            matches.insert(1, "file_type", file_type)
            matches.insert(2, "ncm_sbmi", matches.pop("_ncm"))
            matches.insert(3, "descricao_ncm_sbmi", matches["ncm_sbmi"].map(basket))
            match_frames.append(matches)

        summary = _summarize_composition(frame, mapping, path.name, basket)
        if not summary.empty:
            composition_frames.append(summary)
        elif file_type == "composicao_mercado":
            limitation_rows.append({
                "source_file": path.name,
                "code": "COMPOSITION_FIELDS_NOT_IDENTIFIED",
                "description": (
                    "NCM foi identificado, mas o schema não permitiu mapear INT/OUF/EXT "
                    "com segurança. Nenhum market share foi calculado."
                ),
            })

    schema = pd.DataFrame(schema_rows)
    matches = pd.concat(match_frames, ignore_index=True) if match_frames else pd.DataFrame(
        columns=["source_file", "file_type", "ncm_sbmi", "descricao_ncm_sbmi"]
    )
    composition = (
        pd.concat(composition_frames, ignore_index=True)
        if composition_frames
        else pd.DataFrame(
            columns=[
                "ncm", "descricao_ncm", "int_rs", "ouf", "ext", "demanda_rs", "part_rs",
                "dependencia_nt", "source_file", "natureza", "formula_part_rs",
            ]
        )
    )
    limitations = pd.DataFrame(limitation_rows, columns=["source_file", "code", "description"])

    found_ncms = set(matches.get("ncm_sbmi", pd.Series(dtype=str)).astype(str))
    calculated_ncms = set(composition.get("ncm", pd.Series(dtype=str)).astype(str))
    validation = pd.DataFrame([
        ("csv_files_found", len(files), "DADO_CALCULADO", "PASS" if files else "FAIL"),
        (
            "csv_files_read_ok",
            int((schema["status"] == "READ_OK").sum()),
            "DADO_CALCULADO",
            "PASS",
        ),
        ("ncm_codes_expected", len(basket), "PARÂMETRO", "PASS"),
        (
            "ncm_codes_found_any_file",
            len(found_ncms),
            "DADO_CALCULADO",
            "PASS" if found_ncms else "WARN",
        ),
        (
            "ncm_codes_with_composition",
            len(calculated_ncms),
            "DADO_CALCULADO",
            "PASS" if calculated_ncms else "WARN",
        ),
        ("canonical_rows_promoted", 0, "DADO_OBSERVADO", "PASS"),
    ], columns=["indicator", "value", "nature", "status"])

    partial.mkdir(parents=True)
    try:
        schema.to_csv(partial / "schema_inventory.csv", index=False)
        matches.to_csv(partial / "rice_ncm_matches.csv", index=False)
        composition.to_csv(partial / "rice_composition_summary.csv", index=False)
        validation.to_csv(partial / "validation.csv", index=False)
        limitations.to_csv(partial / "limitations.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise

    return RadarOpenDataAuditResult(target, schema, matches, composition, validation, limitations)
