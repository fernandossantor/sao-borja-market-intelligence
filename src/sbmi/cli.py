"""Interface de linha de comando do projeto."""

from pathlib import Path
from typing import Annotated

import pandas as pd
import typer

from sbmi.inventory import build_inventory, duplicate_candidates
from sbmi.paths import ProjectPaths

app = typer.Typer(no_args_is_help=True)


@app.command()
def doctor() -> None:
    """Verifica e prepara os diretórios locais do ambiente."""
    paths = ProjectPaths.from_environment()
    paths.ensure_local_directories()
    typer.echo(f"project_root={paths.project_root}")
    typer.echo(f"data_root={paths.data_root}")
    typer.echo("status=ok")


@app.command()
def inventory(
    root: Annotated[
        Path,
        typer.Option(exists=True, file_okay=False, readable=True),
    ],
    output: Annotated[
        Path,
        typer.Option(),
    ] = Path("manifests/local_inventory.csv"),
) -> None:
    """Gera inventário recursivo com hashes SHA-256."""
    result = build_inventory(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output, index=False)
    typer.echo(f"files={len(result)}")
    typer.echo(f"output={output.resolve()}")


@app.command("find-exact-duplicates")
def find_exact_duplicates(
    inventory_csv: Annotated[
        Path,
        typer.Option(exists=True, dir_okay=False, readable=True),
    ],
    output: Annotated[
        Path,
        typer.Option(),
    ] = Path("reports/generated/exact_duplicates.csv"),
) -> None:
    """Identifica arquivos fisicamente idênticos pelo SHA-256."""
    inventory_df = pd.read_csv(inventory_csv)
    result = duplicate_candidates(inventory_df)
    output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output, index=False)
    typer.echo(f"duplicate_rows={len(result)}")
    typer.echo(f"output={output.resolve()}")


if __name__ == "__main__":
    app()
