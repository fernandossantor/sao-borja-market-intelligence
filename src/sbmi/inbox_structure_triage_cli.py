"""Comando para resumir grupos e similaridades estruturais da captura."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from sbmi.inbox_structure_triage import triage_structure


def latest_profile_dir(root: Path) -> Path:
    """Seleciona o diretório de perfil mais recente pelo nome."""
    resolved = root.expanduser().resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Diretório de perfis não encontrado: {resolved}")
    candidates = sorted(
        path for path in resolved.iterdir() if path.is_dir() and not path.name.startswith(".")
    )
    if not candidates:
        raise FileNotFoundError(f"Nenhum perfil encontrado em: {resolved}")
    return candidates[-1]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Resume assinaturas exatas e candidatos de similaridade parcial entre "
            "as tabelas perfiladas de raw/new_files."
        )
    )
    parser.add_argument("--profile-dir", type=Path)
    parser.add_argument(
        "--profiles-root",
        type=Path,
        default=Path(".data/audit/new_files/content_profile"),
    )
    parser.add_argument("--output-dir", type=Path)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    profile_dir = (
        args.profile_dir.expanduser().resolve()
        if args.profile_dir is not None
        else latest_profile_dir(args.profiles_root)
    )
    sheet_path = profile_dir / "sheet_profile.csv"
    column_path = profile_dir / "column_profile.csv"
    if not sheet_path.is_file() or not column_path.is_file():
        raise FileNotFoundError(
            "O perfil precisa conter sheet_profile.csv e column_profile.csv."
        )

    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/audit/new_files/structure_triage") / profile_dir.name
    )
    result = triage_structure(pd.read_csv(sheet_path), pd.read_csv(column_path))
    output_dir.mkdir(parents=True, exist_ok=True)
    result.table_registry.to_csv(output_dir / "table_registry.csv", index=False)
    result.schema_summary.to_csv(output_dir / "schema_summary.csv", index=False)
    result.source_summary.to_csv(output_dir / "source_summary.csv", index=False)
    result.similarity_candidates.to_csv(
        output_dir / "header_similarity_candidates.csv", index=False
    )

    repeated = result.schema_summary.loc[result.schema_summary["group_size"].gt(1)]
    singleton = result.schema_summary.loc[result.schema_summary["group_size"].eq(1)]
    largest_size = int(result.schema_summary["group_size"].max())
    largest = result.schema_summary.loc[
        result.schema_summary["group_size"].eq(largest_size)
    ].iloc[0]

    print(f"profile_dir={profile_dir}")
    print(f"tables_total={len(result.table_registry)}")
    print(f"sources_total={len(result.source_summary)}")
    print(f"schema_signatures_total={len(result.schema_summary)}")
    print(f"repeated_exact_schema_groups={len(repeated)}")
    print(f"tables_in_repeated_exact_groups={int(repeated['group_size'].sum())}")
    print(f"singleton_schema_tables={len(singleton)}")
    print(f"largest_exact_group_size={largest_size}")
    print(f"largest_exact_group_sources={largest.sources}")
    print(f"similarity_candidate_pairs={len(result.similarity_candidates)}")
    for row in result.source_summary.itertuples(index=False):
        print(
            "source="
            f"{row.source_declared}\ttables={row.tables}"
            f"\tfiles={row.files}"
            f"\tschemas={row.exact_schema_signatures}"
            f"\trepeated={row.repeated_exact_tables}"
            f"\tsingleton={row.singleton_tables}"
        )
    print(f"output_dir={output_dir.resolve()}")
    print("status=ok")


if __name__ == "__main__":
    main()
