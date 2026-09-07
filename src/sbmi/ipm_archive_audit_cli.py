"""CLI para auditoria de layout dos arquivos definitivos de IPM."""

from __future__ import annotations

import argparse
from pathlib import Path

from sbmi.ipm_archive_audit import audit_ipm_archive, audit_results_table


def _archive_spec(value: str) -> tuple[int, Path]:
    try:
        year_text, path_text = value.split("=", 1)
        year = int(year_text)
    except (ValueError, TypeError) as exc:
        raise argparse.ArgumentTypeError("Use ANO=CAMINHO.zip") from exc
    return year, Path(path_text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--archive",
        action="append",
        required=True,
        type=_archive_spec,
        help="Arquivo oficial no formato ANO=CAMINHO.zip; pode ser repetido.",
    )
    parser.add_argument("--municipality", default="São Borja")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("artifacts/ipm_definitive_layout_audit.csv"),
    )
    args = parser.parse_args()

    results = [
        audit_ipm_archive(path, distribution_year=year, municipality=args.municipality)
        for year, path in args.archive
    ]
    table = audit_results_table(results)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(args.output, index=False)

    print(f"archives={len(results)}")
    print(f"rows={len(table)}")
    print(f"output={args.output}")
    for result in results:
        print(
            "year="
            f"{result.distribution_year} member={result.import_member} "
            f"matches={len(result.matched_lines)} sha256={result.archive_sha256}"
        )
    print("STATUS=IPM_DEFINITIVE_LAYOUT_AUDIT_OK")


if __name__ == "__main__":
    main()
