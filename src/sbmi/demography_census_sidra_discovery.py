"""Descoberta verificável de tabelas, descritores e consultas planejadas SIDRA."""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd

API_HELP_URL = "https://apisidra.ibge.gov.br/home/ajuda"
COMPOSITION_CATALOG_URL = "https://sidra.ibge.gov.br/pesquisa/censo-demografico/demografico-2022/universo-composicao-domiciliar-e-obitos-informados"
POPULATION_CATALOG_URL = "https://sidra.ibge.gov.br/pesquisa/censo-demografico/demografico-2022/primeiros-resultados-populacao-e-domicilios"
DESCRIPTOR_URLS = {
    "4714": "https://sidra.ibge.gov.br/ajax/tabela/descricao/1/4714",
    "9879": "https://sidra.ibge.gov.br/ajax/tabela/descricao/1/9879",
}
PAGE_SPECS = (
    ("api_help", "Ajuda oficial da API SIDRA", API_HELP_URL, "html"),
    ("composition_catalog", "Composição domiciliar e óbitos", COMPOSITION_CATALOG_URL, "html"),
    ("population_catalog", "População e domicílios", POPULATION_CATALOG_URL, "html"),
    ("descriptor_4714", "Descritor da tabela 4714", DESCRIPTOR_URLS["4714"], "json"),
    ("descriptor_9879", "Descritor da tabela 9879", DESCRIPTOR_URLS["9879"], "json"),
)
ALLOWED_HOSTS = {"apisidra.ibge.gov.br", "sidra.ibge.gov.br"}


@dataclass(frozen=True)
class Page:
    page_id: str
    title: str
    requested_url: str
    final_url: str
    content: bytes
    status_code: int
    content_type: str
    file_type: str
    sha256: str


@dataclass(frozen=True)
class Result:
    pages: pd.DataFrame
    tables: pd.DataFrame
    variables: pd.DataFrame
    classifications: pd.DataFrame
    categories: pd.DataFrame
    concepts: pd.DataFrame
    queries: pd.DataFrame
    summary: pd.DataFrame
    snapshot_path: Path
    output_path: Path


class _Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.inrow = False
        self.incell = False
        self.cells = []
        self.buf = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "tr":
            self.inrow = True
            self.cells = []
        elif self.inrow and tag.lower() in {"td", "th"}:
            self.incell = True
            self.buf = []

    def handle_data(self, data):
        if self.incell:
            self.buf.append(data)

    def handle_endtag(self, tag):
        if tag.lower() in {"td", "th"} and self.incell:
            self.cells.append(" ".join("".join(self.buf).split()))
            self.incell = False
        elif tag.lower() == "tr" and self.inrow:
            if self.cells:
                self.rows.append(self.cells)
            self.inrow = False


def _validate_identifier(identifier, field):
    if not isinstance(identifier, str) or not identifier.strip():
        raise ValueError(f"{field} deve ser um identificador não vazio")
    if Path(identifier).name != identifier or identifier in {".", ".."}:
        raise ValueError(f"{field} deve ser um nome simples")


def _ensure_output_available(root, identifier):
    target = root.expanduser().resolve() / identifier
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")


def _validate(url, allow_values=False):
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS:
        raise ValueError(f"URL fora da lista oficial SIDRA: {url}")
    if not allow_values and "/values" in parsed.path.lower():
        raise ValueError("A descoberta não pode consultar /values")


def _fetch(session, pid, title, url, file_type, timeout, limit):
    _validate(url)
    response = session.get(
        url, timeout=timeout, headers={"User-Agent": "sbmi-sidra-metadata-discovery/1.0"}
    )
    response.raise_for_status()
    content = bytes(response.content)
    if not content or len(content) > limit:
        raise ValueError(f"Conteúdo vazio ou acima do limite: {url}")
    ctype = str(response.headers.get("Content-Type", ""))
    expected = "json" if file_type == "json" else "html"
    if expected not in ctype.lower():
        raise ValueError(f"Tipo inesperado em {url}: {ctype}")
    final = str(getattr(response, "url", url))
    _validate(final)
    return Page(
        pid,
        title,
        url,
        final,
        content,
        int(response.status_code),
        ctype,
        file_type,
        hashlib.sha256(content).hexdigest(),
    )


def _tables(pages):
    rows = []
    for pid in ("composition_catalog", "population_catalog"):
        parser = _Parser()
        parser.feed(pages[pid].content.decode(errors="replace"))
        seen = set()
        for cells in parser.rows:
            if len(cells) < 5 or not cells[1].isdigit() or cells[1] in seen:
                continue
            tid = cells[1]
            seen.add(tid)
            rows.append(
                (
                    pid,
                    tid,
                    cells[2],
                    cells[3],
                    cells[4],
                    f"https://sidra.ibge.gov.br/tabela/{tid}",
                    "DIRECT_CANDIDATE" if tid in {"4714", "9879"} else "CONTEXT_TABLE",
                    "NOT_ASSESSED",
                    "observed",
                    "interpreted",
                )
            )
    return pd.DataFrame(
        rows,
        columns=[
            "source_page_id",
            "table_id",
            "table_title",
            "period",
            "territory_codes",
            "table_url",
            "discovery_relevance",
            "conceptual_equivalence_status",
            "metadata_nature",
            "relevance_nature",
        ],
    )


def _descriptors(pages):
    docs = {tid: json.loads(pages[f"descriptor_{tid}"].content) for tid in DESCRIPTOR_URLS}
    variables = []
    classes = []
    categories = []
    for tid, doc in docs.items():
        if str(doc.get("Id")) != tid:
            raise ValueError(f"ID divergente no descritor {tid}")
        for var in doc.get("Variaveis", []):
            units = var.get("UnidadeDeMedida") or [{}]
            variables.append(
                (
                    tid,
                    str(var["Id"]),
                    var["Nome"],
                    units[0].get("Unidade", ""),
                    var.get("DecimaisArmazenamento"),
                    var.get("DecimaisApresentacao"),
                    False,
                    "observed",
                )
            )
            for derived in var.get("VariaveisDerivadas", []):
                variables.append(
                    (
                        tid,
                        str(derived["Id"]),
                        derived["Nome"],
                        derived.get("UnidadeDeMedida", ""),
                        derived.get("DecimaisArmazenamento"),
                        derived.get("DecimaisApresentacao"),
                        True,
                        "observed",
                    )
                )
        for cls in doc.get("Classificacoes", []):
            classes.append(
                (
                    tid,
                    str(cls["Id"]),
                    cls["Nome"],
                    str(cls["IndiceTotal"]),
                    bool(cls["AdmiteTotal"]),
                    "observed",
                )
            )
            for cat in cls.get("Categorias", []):
                categories.append(
                    (
                        tid,
                        str(cls["Id"]),
                        str(cat["Id"]),
                        cat["Nome"],
                        str(cat["Id"]) == str(cls["IndiceTotal"]),
                        cat.get("Disponibilidade", ""),
                        "observed",
                    )
                )
    return (
        docs,
        pd.DataFrame(
            variables,
            columns=[
                "table_id",
                "variable_id",
                "variable_name",
                "unit",
                "storage_decimals",
                "display_decimals",
                "is_derived",
                "nature",
            ],
        ),
        pd.DataFrame(
            classes,
            columns=[
                "table_id",
                "classification_id",
                "classification_name",
                "total_category_id",
                "allows_total",
                "nature",
            ],
        ),
        pd.DataFrame(
            categories,
            columns=[
                "table_id",
                "classification_id",
                "category_id",
                "category_name",
                "is_total",
                "availability",
                "nature",
            ],
        ),
    )


def _concepts(docs):
    return pd.DataFrame(
        [
            (
                "composition_scope",
                "Composição domiciliar",
                "Relação de parentesco ou convivência com a pessoa responsável pelo domicílio.",
                "composition_catalog",
                "observed",
            ),
            (
                "family_limitation",
                "Famílias",
                "A divulgação não contém os dados completos necessários à análise de famílias.",
                "composition_catalog",
                "observed_limitation",
            ),
            (
                "table_4714_notes",
                "Notas da tabela 4714",
                docs["4714"].get("Notas", ""),
                "descriptor_4714",
                "observed",
            ),
            (
                "table_9879_notes",
                "Notas da tabela 9879",
                docs["9879"].get("Notas", ""),
                "descriptor_9879",
                "observed",
            ),
        ],
        columns=["concept_id", "concept", "statement", "source_page_id", "nature"],
    )


def _queries():
    base = "https://apisidra.ibge.gov.br/values"
    rows = [
        (
            "territory_4714",
            "4714",
            "4318002",
            "2022",
            "93,6318,614",
            "",
            f"{base}/t/4714/n6/4318002/p/2022/v/93,6318,614",
        ),
        (
            "composition_9879",
            "9879",
            "4318002",
            "2022",
            "800,1000800",
            "c460=12076,12077,12078,12079;c68=9902;c11561=100679;c12237=104570;c11562=72593",
            f"{base}/t/9879/n6/4318002/p/2022/v/800,1000800/c460/12076,12077,12078,12079/c68/9902/c11561/100679/c12237/104570/c11562/72593",
        ),
    ]
    for row in rows:
        _validate(row[-1], allow_values=True)
    return pd.DataFrame(
        [(*row, "PREPARED_NOT_EXECUTED", "recommended") for row in rows],
        columns=[
            "query_id",
            "table_id",
            "municipality_code",
            "period",
            "variable_ids",
            "classification_filters",
            "url",
            "execution_status",
            "nature",
        ],
    )


def _atomic(root, ident):
    target = root.expanduser().resolve() / ident
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    partial.mkdir(parents=True)
    return target, partial


def discover_sidra_metadata(
    session,
    *,
    snapshots_root,
    audit_root,
    snapshot_id,
    run_id,
    timeout_seconds=30.0,
    max_page_bytes=1_000_000,
):
    if timeout_seconds <= 0 or max_page_bytes <= 0:
        raise ValueError("Timeout e limite devem ser positivos")
    _validate_identifier(snapshot_id, "snapshot_id")
    _validate_identifier(run_id, "run_id")
    _ensure_output_available(snapshots_root, snapshot_id)
    _ensure_output_available(audit_root, run_id)
    pages = {
        pid: _fetch(session, pid, title, url, kind, timeout_seconds, max_page_bytes)
        for pid, title, url, kind in PAGE_SPECS
    }
    tables = _tables(pages)
    docs, variables, classes, categories = _descriptors(pages)
    concepts = _concepts(docs)
    queries = _queries()
    if not {"4714", "9879"}.issubset(set(tables.table_id)):
        raise ValueError("Tabelas candidatas esperadas ausentes")
    sp, partial = _atomic(snapshots_root, snapshot_id)
    manifest = []
    try:
        for pid, page in sorted(pages.items()):
            name = f"{pid}.{page.file_type}"
            (partial / name).write_bytes(page.content)
            manifest.append(
                {
                    "page_id": pid,
                    "title": page.title,
                    "requested_url": page.requested_url,
                    "final_url": page.final_url,
                    "status_code": page.status_code,
                    "content_type": page.content_type,
                    "bytes": len(page.content),
                    "sha256": page.sha256,
                    "local_file": name,
                    "nature": "observed",
                }
            )
        manifest = pd.DataFrame(manifest)
        manifest.to_csv(partial / "sidra_page_manifest.csv", index=False)
        sp.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(sp)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    summary = pd.DataFrame(
        [
            ("pages_captured", len(manifest), "observed"),
            ("tables_identified", len(tables), "calculated"),
            ("variables_identified", len(variables), "calculated"),
            ("classifications_identified", len(classes), "calculated"),
            ("categories_identified", len(categories), "calculated"),
            ("queries_prepared", len(queries), "calculated"),
            ("values_requests", 0, "observed"),
            ("conceptually_validated_tables", 0, "observed"),
        ],
        columns=["indicator", "value", "nature"],
    )
    op, partial = _atomic(audit_root, run_id)
    try:
        for name, frame in (
            ("sidra_table_register", tables),
            ("sidra_variable_register", variables),
            ("sidra_classification_register", classes),
            ("sidra_category_register", categories),
            ("sidra_concept_register", concepts),
            ("sidra_query_plan", queries),
            ("sidra_discovery_summary", summary),
        ):
            frame.to_csv(partial / f"{name}.csv", index=False)
        op.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(op)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return Result(
        manifest, tables, variables, classes, categories, concepts, queries, summary, sp, op
    )
