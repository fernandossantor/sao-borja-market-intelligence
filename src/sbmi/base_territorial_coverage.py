"""Mapeamento de cobertura da Base Territorial Comum."""

from __future__ import annotations

import re
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import pandas as pd

INVENTORY_REQUIRED_COLUMNS = {
    "relative_path",
    "file_name",
    "extension",
    "is_folder",
    "size_bytes",
}
BLOCKS = (
    "demografia",
    "economia_estrutura_produtiva",
    "renda_emprego_trabalho",
    "educacao",
    "infraestrutura_conectividade",
    "financas_publicas_transferencias",
    "saude_condicoes_sociais",
    "ambiente_politico_regulatorio",
    "ambiente_sociocultural_territorial",
    "transversal_multitematico",
)
BLOCK_LABELS = {
    "demografia": "Demografia",
    "economia_estrutura_produtiva": "Economia e estrutura produtiva",
    "renda_emprego_trabalho": "Renda, emprego e trabalho",
    "educacao": "Educação",
    "infraestrutura_conectividade": "Infraestrutura e conectividade",
    "financas_publicas_transferencias": (
        "Finanças públicas e transferências governamentais"
    ),
    "saude_condicoes_sociais": "Saúde e condições sociais",
    "ambiente_politico_regulatorio": "Ambiente político e regulatório",
    "ambiente_sociocultural_territorial": (
        "Ambiente sociocultural e territorial"
    ),
    "transversal_multitematico": "Indicadores transversais e multitemáticos",
    "nao_classificado": "Não classificado",
    "governanca_documentacao": "Governança e documentação",
}
ANALYTICAL_EXTENSIONS = {
    "csv",
    "tsv",
    "txt",
    "xlsx",
    "xls",
    "xlsm",
    "ods",
    "parquet",
    "feather",
    "json",
    "jsonl",
    "duckdb",
    "db",
    "sqlite",
    "sqlite3",
    "pdf",
    "doc",
    "docx",
    "odt",
    "rtf",
    "html",
    "htm",
}
PATH_OVERRIDES = (
    (
        "raw/new_files/",
        "financas_publicas_transferencias",
        "PATH_OVERRIDE_RAW_NEW_FILES",
    ),
    (
        "raw/social/",
        "saude_condicoes_sociais",
        "PATH_OVERRIDE_RAW_SOCIAL",
    ),
    (
        "governance/",
        "governanca_documentacao",
        "PATH_OVERRIDE_GOVERNANCE",
    ),
)
KEYWORD_RULES = (
    (
        "financas_publicas_transferencias",
        (
            "transferencia",
            "transferencias",
            "repasse",
            "repasses",
            "receita",
            "receitas",
            "despesa",
            "despesas",
            "fiscal",
            "orcamento",
            "orcamentaria",
            "icms",
            "arrecadacao",
            "empenhado",
            "liquidado",
            "tesouro",
            "fpm",
            "finbra",
            "siconfi",
        ),
    ),
    (
        "renda_emprego_trabalho",
        (
            "rais",
            "caged",
            "emprego",
            "empregos",
            "trabalho",
            "ocupacao",
            "desocupacao",
            "remuneracao",
            "salario",
            "renda",
        ),
    ),
    (
        "demografia",
        (
            "populacao",
            "populacional",
            "demografia",
            "demografico",
            "censo",
            "natalidade",
            "fecundidade",
            "migracao",
            "domicilio",
        ),
    ),
    (
        "educacao",
        (
            "educacao",
            "escolar",
            "escola",
            "ensino",
            "ideb",
            "enem",
            "alfabetizacao",
            "matricula",
            "matriculas",
        ),
    ),
    (
        "infraestrutura_conectividade",
        (
            "saneamento",
            "agua",
            "esgoto",
            "energia",
            "internet",
            "banda larga",
            "telecom",
            "conectividade",
            "transporte",
            "rodovia",
            "frota",
            "habitacao",
            "infraestrutura",
        ),
    ),
    (
        "saude_condicoes_sociais",
        (
            "saude",
            "mortalidade",
            "vulnerabilidade",
            "assistencia social",
            "cadunico",
            "bolsa familia",
            "pobreza",
            "sus",
            "idsc",
        ),
    ),
    (
        "economia_estrutura_produtiva",
        (
            "economia",
            "economico",
            "pib",
            "empresa",
            "empresas",
            "estabelecimento",
            "estabelecimentos",
            "cnae",
            "agro",
            "agricultura",
            "pecuaria",
            "producao",
            "valor adicionado",
            "comercio",
            "servicos",
            "exportacao",
            "importacao",
        ),
    ),
    (
        "ambiente_politico_regulatorio",
        (
            "eleicao",
            "eleitoral",
            "legislacao",
            "regulacao",
            "regulatorio",
            "plano diretor",
            "camara municipal",
        ),
    ),
    (
        "ambiente_sociocultural_territorial",
        (
            "cultura",
            "turismo",
            "midia",
            "religiao",
            "bairro",
            "territorio",
            "territorial",
            "urbano",
            "rural",
        ),
    ),
    (
        "transversal_multitematico",
        (
            "ips brasil",
            "progresso social",
            "ods",
            "indicadores municipais",
            "painel municipal",
        ),
    ),
)
STAGING_DATASET_BLOCKS = {
    "federal_transferencias": "financas_publicas_transferencias",
    "estadual_icms": "financas_publicas_transferencias",
    "estadual_transferencias": "financas_publicas_transferencias",
    "municipal_despesas_instituicao": "financas_publicas_transferencias",
    "municipal_despesas_elemento": "financas_publicas_transferencias",
    "municipal_receita_elemento": "financas_publicas_transferencias",
}
EVIDENCE_COLUMNS = [
    "evidence_id",
    "block",
    "block_label",
    "layer",
    "object_name",
    "source_reference",
    "geographic_scope",
    "period_reference",
    "unit",
    "observed_rows",
    "source_files",
    "validation_status",
    "limitation",
    "nature",
]


@dataclass(frozen=True)
class CoverageMapResult:
    files: pd.DataFrame
    source_families: pd.DataFrame
    evidence_register: pd.DataFrame
    block_summary: pd.DataFrame
    gap_register: pd.DataFrame
    summary: pd.DataFrame


def normalize_text(value: object) -> str:
    """Normaliza texto para regras explícitas de classificação."""
    decomposed = unicodedata.normalize("NFKD", str(value or ""))
    ascii_text = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    normalized = re.sub(r"[^a-z0-9]+", " ", ascii_text.casefold()).strip()
    return re.sub(r"\s+", " ", normalized)


def _extension(value: object) -> str:
    return str(value or "").strip().lower().lstrip(".")


def _folder_mask(series: pd.Series) -> pd.Series:
    return series.map(
        lambda value: value is True
        or str(value).strip().casefold() in {"true", "1", "yes"}
    )


def _stage(path: object) -> str:
    parts = PurePosixPath(str(path or "").strip("/")).parts
    return parts[0] if parts else ""


def _source_family(path: object) -> str:
    parts = PurePosixPath(str(path or "").strip("/")).parts
    if not parts:
        return ""
    return "/".join(parts[:2]) if len(parts) >= 2 else parts[0]


def _contains_keyword(normalized_text: str, keyword: str) -> bool:
    normalized_keyword = normalize_text(keyword)
    if " " in normalized_keyword:
        return normalized_keyword in normalized_text
    return normalized_keyword in set(normalized_text.split())


def classify_path(relative_path: object, file_name: object = "") -> dict[str, object]:
    """Classifica por caminho e palavras-chave sem inferir validade substantiva."""
    path = str(relative_path or "").strip("/")
    normalized_path = path.casefold()
    for prefix, block, basis in PATH_OVERRIDES:
        if normalized_path.startswith(prefix):
            return {
                "primary_block": block,
                "matched_blocks": block,
                "classification_method": "EXPLICIT_PATH_OVERRIDE",
                "classification_basis": basis,
                "classification_confidence": "HIGH",
                "coverage_eligible": block != "governanca_documentacao",
            }

    text = normalize_text(f"{path} {file_name}")
    matched: list[str] = []
    bases: list[str] = []
    for block, keywords in KEYWORD_RULES:
        block_matches = [
            keyword for keyword in keywords if _contains_keyword(text, keyword)
        ]
        if block_matches:
            matched.append(block)
            bases.extend(
                f"{block}:{normalize_text(keyword)}" for keyword in block_matches
            )

    if matched:
        return {
            "primary_block": matched[0],
            "matched_blocks": "|".join(dict.fromkeys(matched)),
            "classification_method": "KEYWORD_RULE",
            "classification_basis": "|".join(bases),
            "classification_confidence": "MEDIUM",
            "coverage_eligible": True,
        }
    return {
        "primary_block": "nao_classificado",
        "matched_blocks": "",
        "classification_method": "UNCLASSIFIED",
        "classification_basis": "",
        "classification_confidence": "UNASSESSED",
        "coverage_eligible": True,
    }


def prepare_inventory(inventory: pd.DataFrame) -> pd.DataFrame:
    """Prepara o inventário do Drive para o mapa de cobertura."""
    missing = INVENTORY_REQUIRED_COLUMNS.difference(inventory.columns)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes no inventário: " f"{sorted(missing)}"
        )

    frame = inventory.loc[~_folder_mask(inventory["is_folder"])].copy()
    frame["relative_path"] = frame["relative_path"].fillna("").astype(str)
    frame["file_name"] = frame["file_name"].fillna("").astype(str)
    frame["extension"] = frame["extension"].map(_extension)
    frame["size_bytes"] = pd.to_numeric(
        frame["size_bytes"], errors="coerce"
    ).fillna(0)
    frame["source_stage"] = frame["relative_path"].map(_stage)
    frame["source_family"] = frame["relative_path"].map(_source_family)
    frame["analytical_extension"] = frame["extension"].isin(
        ANALYTICAL_EXTENSIONS
    )
    classifications = pd.DataFrame(
        [
            classify_path(row.relative_path, row.file_name)
            for row in frame.itertuples(index=False)
        ],
        index=frame.index,
    )
    frame = pd.concat([frame, classifications], axis=1)
    frame["block_label"] = frame["primary_block"].map(BLOCK_LABELS)
    frame["analytical_candidate"] = (
        frame["coverage_eligible"] & frame["analytical_extension"]
    )

    if "sha256_checksum" not in frame.columns:
        frame["sha256_checksum"] = ""
    frame["sha256_checksum"] = (
        frame["sha256_checksum"].fillna("").astype(str)
    )
    if "audit_status" not in frame.columns:
        frame["audit_status"] = ""

    columns = [
        "relative_path",
        "file_name",
        "extension",
        "size_bytes",
        "source_stage",
        "source_family",
        "primary_block",
        "block_label",
        "matched_blocks",
        "classification_method",
        "classification_basis",
        "classification_confidence",
        "coverage_eligible",
        "analytical_extension",
        "analytical_candidate",
        "sha256_checksum",
        "audit_status",
    ]
    columns.extend(
        column
        for column in ("created_at_utc", "modified_at_utc", "mime_type")
        if column in frame.columns
    )
    return frame[columns].sort_values(
        ["source_stage", "source_family", "relative_path"]
    ).reset_index(drop=True)


def build_source_family_summary(files: pd.DataFrame) -> pd.DataFrame:
    """Agrega candidatos analíticos por família e bloco primário."""
    eligible = files.loc[files["analytical_candidate"]]
    columns = [
        "source_stage",
        "source_family",
        "primary_block",
        "block_label",
        "files",
        "known_bytes",
        "files_with_sha256",
        "extensions",
        "classification_methods",
    ]
    if eligible.empty:
        return pd.DataFrame(columns=columns)

    records: list[dict[str, object]] = []
    group_columns = [
        "source_stage",
        "source_family",
        "primary_block",
        "block_label",
    ]
    for key, group in eligible.groupby(group_columns, dropna=False, sort=True):
        stage, family, block, label = key
        records.append(
            {
                "source_stage": stage,
                "source_family": family,
                "primary_block": block,
                "block_label": label,
                "files": len(group),
                "known_bytes": int(group["size_bytes"].sum()),
                "files_with_sha256": int(
                    group["sha256_checksum"].ne("").sum()
                ),
                "extensions": "|".join(
                    sorted(set(group["extension"]) - {""})
                ),
                "classification_methods": "|".join(
                    sorted(set(group["classification_method"]))
                ),
            }
        )
    return pd.DataFrame(records, columns=columns)


def _empty_evidence() -> pd.DataFrame:
    return pd.DataFrame(columns=EVIDENCE_COLUMNS)


def staging_evidence(
    manifest: pd.DataFrame | None,
    dataset_validation: pd.DataFrame | None,
) -> pd.DataFrame:
    """Registra contratos de staging de ``raw/new_files`` como evidência."""
    if manifest is None or manifest.empty:
        return _empty_evidence()
    required = {"relative_path", "dataset", "output_rows", "disposition"}
    missing = required.difference(manifest.columns)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes no manifesto do staging: "
            f"{sorted(missing)}"
        )

    validation_lookup: dict[str, object] = {}
    if dataset_validation is not None and not dataset_validation.empty:
        if "dataset" not in dataset_validation.columns:
            raise ValueError("A validação do staging não contém a coluna dataset.")
        validation_lookup = {
            str(row.dataset): row
            for row in dataset_validation.itertuples(index=False)
        }

    included = manifest.loc[
        manifest["disposition"].eq("INCLUDED_IN_STAGING")
    ]
    records: list[dict[str, object]] = []
    for dataset, group in included.groupby("dataset", sort=True):
        dataset_name = str(dataset)
        block = STAGING_DATASET_BLOCKS.get(dataset_name, "nao_classificado")
        validation = validation_lookup.get(dataset_name)
        period = ""
        status = "STAGING_PRESENT_NOT_VALIDATED_BY_COVERAGE_MAP"
        observed_rows = int(
            pd.to_numeric(group["output_rows"], errors="coerce")
            .fillna(0)
            .sum()
        )
        source_files = int(group["relative_path"].nunique())
        limitation = (
            "A estrutura foi registrada; unidade, abrangência geográfica e "
            "comparabilidade conceitual exigem curadoria temática."
        )
        if validation is not None:
            date_min = str(getattr(validation, "date_min", "") or "")
            date_max = str(getattr(validation, "date_max", "") or "")
            period = (
                date_min
                if date_min and date_min == date_max
                else " a ".join(
                    value for value in (date_min, date_max) if value
                )
            )
            status = (
                "STRUCTURAL_VALIDATION_OK"
                if str(getattr(validation, "status", "")) == "OK"
                else "STRUCTURAL_VALIDATION_REVIEW_REQUIRED"
            )
            observed_rows = int(getattr(validation, "rows", observed_rows))
            source_files = int(
                getattr(validation, "source_files", source_files)
            )
            flagged = int(
                getattr(validation, "duplicate_flagged_rows", 0)
            )
            if flagged:
                limitation += (
                    f" Há {flagged} linhas sinalizadas para revisão de "
                    "duplicidade na fonte."
                )

        records.append(
            {
                "evidence_id": f"staging:{dataset_name}",
                "block": block,
                "block_label": BLOCK_LABELS[block],
                "layer": "staging",
                "object_name": dataset_name,
                "source_reference": "raw/new_files",
                "geographic_scope": (
                    "Abrangência a confirmar substantivamente na fonte"
                ),
                "period_reference": period,
                "unit": (
                    "Valores monetários conforme declaração ou contexto da fonte"
                ),
                "observed_rows": observed_rows,
                "source_files": source_files,
                "validation_status": status,
                "limitation": limitation,
                "nature": "observed_and_calculated",
            }
        )
    return pd.DataFrame(records, columns=EVIDENCE_COLUMNS)


def derived_product_evidence(
    derived_families: pd.DataFrame | None,
) -> pd.DataFrame:
    """Registra famílias históricas já auditadas estruturalmente."""
    if derived_families is None or derived_families.empty:
        return _empty_evidence()
    required = {"family", "files", "tables", "rows_observed", "family_status"}
    missing = required.difference(derived_families.columns)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes na auditoria de derivados: "
            f"{sorted(missing)}"
        )

    records: list[dict[str, object]] = []
    for row in derived_families.itertuples(index=False):
        classification = classify_path(row.family, row.family)
        block = str(classification["primary_block"])
        if block == "governanca_documentacao":
            continue
        records.append(
            {
                "evidence_id": f"historical:{row.family}",
                "block": block,
                "block_label": BLOCK_LABELS[block],
                "layer": "historical_derived_product",
                "object_name": str(row.family),
                "source_reference": str(row.family),
                "geographic_scope": (
                    "Abrangência não confirmada pela auditoria estrutural"
                ),
                "period_reference": "",
                "unit": "Não confirmada pela auditoria estrutural",
                "observed_rows": int(row.rows_observed),
                "source_files": int(row.files),
                "validation_status": f"STRUCTURAL_AUDIT_{row.family_status}",
                "limitation": (
                    "A auditoria comprovou legibilidade e estrutura, não validade "
                    "metodológica, atualidade ou comparabilidade."
                ),
                "nature": "observed_and_estimated",
            }
        )
    return pd.DataFrame(records, columns=EVIDENCE_COLUMNS)


def detect_local_module_evidence(curated_root: Path) -> pd.DataFrame:
    """Detecta somente módulos locais com contratos já documentados."""
    root = curated_root.expanduser().resolve()
    specifications = (
        {
            "module_id": "idsc_2025",
            "relative_path": Path("social/idsc"),
            "block": "saude_condicoes_sociais",
            "period": "2025",
            "unit": "Pontuação de 0 a 100",
            "limitation": (
                "As classes interpretativas internas não substituem "
                "classificações oficiais do IDSC-BR."
            ),
        },
        {
            "module_id": "ips_published_2024_2026",
            "relative_path": Path("social/ips"),
            "block": "transversal_multitematico",
            "period": "2024|2025|2026",
            "unit": "Pontuação de 0 a 100",
            "limitation": (
                "As edições originalmente publicadas não são estritamente "
                "comparáveis; nenhuma tendência temporal foi calculada."
            ),
        },
    )
    records: list[dict[str, object]] = []
    for specification in specifications:
        path = root / specification["relative_path"]
        if not path.is_dir():
            continue
        files = [item for item in path.rglob("*") if item.is_file()]
        block = str(specification["block"])
        records.append(
            {
                "evidence_id": f"curated:{specification['module_id']}",
                "block": block,
                "block_label": BLOCK_LABELS[block],
                "layer": "curated_local_module",
                "object_name": str(specification["module_id"]),
                "source_reference": str(path),
                "geographic_scope": "São Borja, código IBGE 4318002",
                "period_reference": str(specification["period"]),
                "unit": str(specification["unit"]),
                "observed_rows": 0,
                "source_files": len(files),
                "validation_status": "CURATED_MODULE_VALIDATED",
                "limitation": str(specification["limitation"]),
                "nature": "observed",
            }
        )
    return pd.DataFrame(records, columns=EVIDENCE_COLUMNS)


def build_evidence_register(
    *,
    manifest: pd.DataFrame | None = None,
    dataset_validation: pd.DataFrame | None = None,
    derived_families: pd.DataFrame | None = None,
    local_modules: pd.DataFrame | None = None,
) -> pd.DataFrame:
    """Combina evidências sem duplicar arquivos do inventário."""
    frames = [
        staging_evidence(manifest, dataset_validation),
        derived_product_evidence(derived_families),
        local_modules if local_modules is not None else _empty_evidence(),
    ]
    non_empty = [frame for frame in frames if not frame.empty]
    if not non_empty:
        return _empty_evidence()
    evidence = pd.concat(non_empty, ignore_index=True)
    missing = set(EVIDENCE_COLUMNS).difference(evidence.columns)
    if missing:
        raise ValueError(
            "Registro de evidências sem colunas obrigatórias: "
            f"{sorted(missing)}"
        )
    return evidence[EVIDENCE_COLUMNS].sort_values(
        ["block", "layer", "evidence_id"]
    ).reset_index(drop=True)


def _status_for_block(
    *,
    curated_modules: int,
    validated_staging: int,
    derived_products: int,
    raw_files: int,
    candidate_files: int,
) -> str:
    if curated_modules:
        return "CURATED_VALIDATED_PRESENT"
    if validated_staging:
        return "STAGING_VALIDATED_PRESENT"
    if derived_products:
        return "DERIVED_PRODUCTS_AUDITED_PRESENT"
    if raw_files:
        return "RAW_SOURCES_PRESENT"
    if candidate_files:
        return "METADATA_CANDIDATES_PRESENT"
    return "NO_CANDIDATE_IDENTIFIED"


def _next_action(status: str) -> str:
    return {
        "CURATED_VALIDATED_PRESENT": (
            "Integrar o módulo à síntese comum e avaliar lacunas de cobertura."
        ),
        "STAGING_VALIDATED_PRESENT": (
            "Documentar conceitos, unidade, abrangência e construir camada curada."
        ),
        "DERIVED_PRODUCTS_AUDITED_PRESENT": (
            "Revisar metodologia, fonte, período e atualidade antes da reutilização."
        ),
        "RAW_SOURCES_PRESENT": (
            "Auditar conteúdo e estrutura; construir staging quando aplicável."
        ),
        "METADATA_CANDIDATES_PRESENT": (
            "Confirmar a classificação e a utilidade analítica dos candidatos."
        ),
        "NO_CANDIDATE_IDENTIFIED": (
            "Revisar arquivos não classificados antes de buscar nova fonte externa."
        ),
    }[status]


def build_block_summary(
    files: pd.DataFrame,
    evidence: pd.DataFrame,
) -> pd.DataFrame:
    """Resume cobertura técnica sem tratá-la como validade substantiva."""
    eligible = files.loc[files["analytical_candidate"]]
    records: list[dict[str, object]] = []
    for block in BLOCKS:
        file_group = eligible.loc[eligible["primary_block"].eq(block)]
        evidence_group = evidence.loc[evidence["block"].eq(block)]
        staging = evidence_group.loc[evidence_group["layer"].eq("staging")]
        validated_staging = int(
            staging["validation_status"].eq("STRUCTURAL_VALIDATION_OK").sum()
        )
        curated = int(
            evidence_group["layer"].eq("curated_local_module").sum()
        )
        derived = int(
            evidence_group["layer"].eq("historical_derived_product").sum()
        )
        raw_files = int(file_group["source_stage"].eq("raw").sum())
        candidate_files = len(file_group)
        status = _status_for_block(
            curated_modules=curated,
            validated_staging=validated_staging,
            derived_products=derived,
            raw_files=raw_files,
            candidate_files=candidate_files,
        )
        records.append(
            {
                "block": block,
                "block_label": BLOCK_LABELS[block],
                "candidate_files": candidate_files,
                "known_bytes": int(file_group["size_bytes"].sum()),
                "source_families": int(
                    file_group["source_family"].nunique()
                ),
                "raw_files": raw_files,
                "processed_files": int(
                    file_group["source_stage"].eq("processed").sum()
                ),
                "warehouse_files": int(
                    file_group["source_stage"].eq("warehouse").sum()
                ),
                "export_files": int(
                    file_group["source_stage"].eq("exports").sum()
                ),
                "staging_datasets": len(staging),
                "validated_staging_datasets": validated_staging,
                "curated_modules": curated,
                "audited_derived_families": derived,
                "coverage_status": status,
                "substantive_validation_status": (
                    "PARTIAL" if curated else "PENDING"
                ),
                "next_action": _next_action(status),
                "nature": "calculated_diagnostic",
            }
        )
    return pd.DataFrame(records)


def build_gap_register(block_summary: pd.DataFrame) -> pd.DataFrame:
    """Classifica lacunas sem afirmar ausência definitiva de dados."""
    gap_by_status = {
        "CURATED_VALIDATED_PRESENT": (
            "INTEGRATION_AND_SYNTHESIS_PENDING",
            "A cobertura validada pode não ser exaustiva para o bloco.",
        ),
        "STAGING_VALIDATED_PRESENT": (
            "CURATED_LAYER_PENDING",
            "A validação é estrutural; conceitos e comparabilidade seguem pendentes.",
        ),
        "DERIVED_PRODUCTS_AUDITED_PRESENT": (
            "METHODOLOGICAL_REVIEW_PENDING",
            "A presença de produto não comprova atualidade ou validade metodológica.",
        ),
        "RAW_SOURCES_PRESENT": (
            "STRUCTURAL_AUDIT_OR_STAGING_PENDING",
            "A presença da fonte não comprova legibilidade ou utilidade analítica.",
        ),
        "METADATA_CANDIDATES_PRESENT": (
            "CLASSIFICATION_AND_VALIDATION_PENDING",
            "A classificação decorre de regras de caminho e palavras-chave.",
        ),
        "NO_CANDIDATE_IDENTIFIED": (
            "NO_CANDIDATE_IDENTIFIED_BY_CURRENT_RULES",
            "Não é possível concluir ausência de dados apenas pela heurística.",
        ),
    }
    records = []
    for row in block_summary.itertuples(index=False):
        gap_class, limitation = gap_by_status[row.coverage_status]
        records.append(
            {
                "block": row.block,
                "block_label": row.block_label,
                "coverage_status": row.coverage_status,
                "gap_class": gap_class,
                "what_cannot_be_concluded": limitation,
                "required_next_evidence": row.next_action,
                "nature": "calculated_diagnostic",
            }
        )
    return pd.DataFrame(records)


def build_summary(
    inventory: pd.DataFrame,
    files: pd.DataFrame,
    source_families: pd.DataFrame,
    evidence: pd.DataFrame,
    block_summary: pd.DataFrame,
) -> pd.DataFrame:
    """Produz indicadores e explicita a natureza de cada medida."""
    folder_count = int(_folder_mask(inventory["is_folder"]).sum())
    classified = (
        files["analytical_candidate"]
        & files["primary_block"].ne("nao_classificado")
    )
    unclassified = (
        files["analytical_candidate"]
        & files["primary_block"].eq("nao_classificado")
    )
    indicators = [
        ("inventory_entries", len(inventory), "observed"),
        ("inventory_folders", folder_count, "calculated"),
        ("inventory_files", len(files), "calculated"),
        (
            "analytical_candidate_files",
            int(files["analytical_candidate"].sum()),
            "calculated",
        ),
        ("classified_candidate_files", int(classified.sum()), "calculated"),
        ("unclassified_candidate_files", int(unclassified.sum()), "calculated"),
        ("source_family_rows", len(source_families), "calculated"),
        ("evidence_register_rows", len(evidence), "calculated"),
        (
            "blocks_with_curated_modules",
            int(block_summary["curated_modules"].gt(0).sum()),
            "calculated",
        ),
        (
            "blocks_with_validated_staging",
            int(
                block_summary["validated_staging_datasets"].gt(0).sum()
            ),
            "calculated",
        ),
        (
            "blocks_without_candidates",
            int(
                block_summary["coverage_status"]
                .eq("NO_CANDIDATE_IDENTIFIED")
                .sum()
            ),
            "calculated",
        ),
    ]
    return pd.DataFrame(
        indicators,
        columns=["indicator", "value", "nature"],
    )


def build_coverage_map(
    inventory: pd.DataFrame,
    *,
    manifest: pd.DataFrame | None = None,
    dataset_validation: pd.DataFrame | None = None,
    derived_families: pd.DataFrame | None = None,
    local_modules: pd.DataFrame | None = None,
) -> CoverageMapResult:
    """Constrói o mapa sem modificar fontes ou produtos existentes."""
    files = prepare_inventory(inventory)
    source_families = build_source_family_summary(files)
    evidence = build_evidence_register(
        manifest=manifest,
        dataset_validation=dataset_validation,
        derived_families=derived_families,
        local_modules=local_modules,
    )
    block_summary = build_block_summary(files, evidence)
    gap_register = build_gap_register(block_summary)
    summary = build_summary(
        inventory,
        files,
        source_families,
        evidence,
        block_summary,
    )
    return CoverageMapResult(
        files=files,
        source_families=source_families,
        evidence_register=evidence,
        block_summary=block_summary,
        gap_register=gap_register,
        summary=summary,
    )


def write_coverage_map(
    result: CoverageMapResult,
    output_dir: Path,
    *,
    replace: bool = False,
) -> Path:
    """Publica o mapa localmente de modo atômico."""
    target = output_dir.expanduser().resolve()
    if target.exists():
        if not replace:
            raise FileExistsError(f"Destino do mapa já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    try:
        outputs = {
            "coverage_file_inventory.csv": result.files,
            "coverage_source_family_summary.csv": result.source_families,
            "coverage_evidence_register.csv": result.evidence_register,
            "coverage_block_summary.csv": result.block_summary,
            "coverage_gap_register.csv": result.gap_register,
            "coverage_map_summary.csv": result.summary,
        }
        for file_name, frame in outputs.items():
            frame.to_csv(partial / file_name, index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.rename(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
