"""CLI da captura municipal de PIB e VAB setorial."""

import argparse
from datetime import UTC, datetime
from pathlib import Path

import requests

from sbmi.economy_gdp_series import collect_economy_gdp_series

OLD_URL = "https://ftp.ibge.gov.br/Pib_Municipios/2003_2007/1999-2001_Serie_Revisada.zip"
SIDRA_URL = "https://apisidra.ibge.gov.br/values/t/5938/n6/4318002/p/all/v/37,543,498,513,516,517,520,6575,6574,525,528"


def main() -> None:
    argparse.ArgumentParser(description=__doc__).parse_args()
    execution_id = f"economy-gdp-series-{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}"
    roots = {
        layer: Path(path)
        for layer, path in {
            "raw": ".data/snapshots/web/economy_gdp_series",
            "staging": ".data/staging/base_territorial/economy_gdp_series",
            "curated": ".data/curated/base_territorial/economy_gdp_series",
            "exports": ".data/exports/base_territorial/economy_gdp_series",
            "audit": ".data/audit/base_territorial/economy_gdp_series",
        }.items()
    }
    with requests.Session() as session:
        result = collect_economy_gdp_series(
            session,
            old_url=OLD_URL,
            sidra_url=SIDRA_URL,
            roots=roots,
            execution_id=execution_id,
        )
    print(f"execution_id={execution_id}\nrows={len(result.values)}\naudit={result.paths['audit']}")


if __name__ == "__main__":
    main()
