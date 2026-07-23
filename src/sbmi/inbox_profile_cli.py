"""Comando para gerar o perfil estrutural local da captura de ``raw/new_files``."""

from __future__ import annotations

import argparse
from pathlib import Path

from sbmi.inbox_profile import profile_snapshot


def latest_snapshot(snapshots_root: Path) -> Path:
    """Seleciona a captura não oculta mais recente pelo nome do diretório."""
    root = snapshots_root.expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Diretório de capturas não encontrado: {root}")
    candidates = sorted(
        path for path in root.iterdir() if path.is_dir() and not path.name.startswith(".")
    )
    if not candidates:
        raise FileNotFoundError(f"Nenhuma captura encontrada em: {root}")
    return candidates[-1]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Gera perfil estrutural de planilhas e arquivos delimitados da captura local, "
            "sem alterar os conteúdos."
        )
    )
    parser.add_argument("--snapshot-path", type=Path)
    parser.add_argument(
        "--snapshots-root",
        type=Path,
        default=Path(".data/snapshots/new_files"),
    )
    parser.add_argument("--output-dir", type=Path)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    snapshot_path = (
        args.snapshot_path.expanduser().resolve()
        if args.snapshot_path is not None
        else latest_snapshot(args.snapshots_root)
    )
    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/audit/new_files/content_profile") / snapshot_path.name
    )

    result = profile_snapshot(snapshot_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    result.files.to_csv(output_dir / "file_profile.csv", index=False)
    result.sheets.to_csv(output_dir / "sheet_profile.csv", index=False)
    result.columns.to_csv(output_dir / "column_profile.csv", index=False)
    result.schema_groups.to_csv(output_dir / "exact_schema_groups.csv", index=False)

    files_profiled = int(result.files["profile_status"].eq("PROFILED").sum())
    unsupported = int(result.files["profile_status"].eq("UNSUPPORTED_FORMAT").sum())
    errors = int(result.files["profile_status"].eq("ERROR").sum())
    low_confidence = (
        int(result.sheets["header_confidence_estimate"].eq("LOW").sum())
        if not result.sheets.empty
        else 0
    )
    schema_group_count = (
        int(result.schema_groups["schema_signature_sha256"].nunique())
        if not result.schema_groups.empty
        else 0
    )

    print(f"snapshot_path={snapshot_path}")
    print(f"files_discovered={len(result.files)}")
    print(f"files_profiled={files_profiled}")
    print(f"files_unsupported={unsupported}")
    print(f"files_error={errors}")
    print(f"tables_profiled={len(result.sheets)}")
    print(f"columns_profiled={len(result.columns)}")
    print(f"header_low_confidence_tables={low_confidence}")
    print(f"exact_schema_groups={schema_group_count}")
    print(f"exact_schema_group_rows={len(result.schema_groups)}")
    print(f"output_dir={output_dir.resolve()}")
    print("status=ok" if errors == 0 else "status=completed_with_errors")


if __name__ == "__main__":
    main()
