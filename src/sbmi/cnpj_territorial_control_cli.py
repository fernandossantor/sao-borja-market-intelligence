"""CLI do controle territorial de matriz/filial dos Dados Abertos CNPJ."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

from sbmi.cnpj_territorial_control import curate_cnpj_territorial_control


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--establishments-dir", type=Path, required=True)
    parser.add_argument("--companies-dir", type=Path, required=True)
    parser.add_argument("--municipalities-zip", type=Path, required=True)
    parser.add_argument("--execution-id")
    parser.add_argument("--municipality-tom", default="8863")
    parser.add_argument("--municipality-ibge", type=int, default=4318002)
    parser.add_argument("--active-status-code", default="02")
    parser.add_argument("--chunksize", type=int, default=200_000)
    args = parser.parse_args()

    execution_id = args.execution_id or (
        f"cnpj-territorial-control-{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}"
    )
    roots = {
        layer: Path(f".data/{layer}/base_territorial/cnpj_territorial_control")
        for layer in ("staging", "curated", "exports", "audit")
    }
    result = curate_cnpj_territorial_control(
        establishments=args.establishments_dir,
        companies=args.companies_dir,
        municipalities_zip=args.municipalities_zip,
        roots=roots,
        execution_id=execution_id,
        municipality_tom=args.municipality_tom,
        municipality_ibge=args.municipality_ibge,
        active_status_code=args.active_status_code,
        chunksize=args.chunksize,
    )
    external = int(
        (
            result.establishments["territorial_control_status"]
            == "FILIAL_DE_MATRIZ_EXTERNA"
        ).sum()
    )
    print(
        f"execution_id={execution_id}\n"
        f"rows={len(result.establishments)}\n"
        f"external_matrix_branches={external}\n"
        f"audit={result.paths['audit']}"
    )


if __name__ == "__main__":
    main()
