"""Interface de linha de comando do projeto."""

import os
from pathlib import Path
from typing import Annotated

import pandas as pd
import typer

from sbmi.drive import check_remote, remote_size, snapshot_raw
from sbmi.inventory import build_inventory, duplicate_candidates
from sbmi.paths import ProjectPaths

app = typer.Typer(no_args_is_help=True)


def drive_remote_name(remote: str | None) -> str:
    """Resolve o nome do remote sem expor credenciais."""
    return remote or os.getenv("SBMI_DRIVE_REMOTE", "sbmi-drive")


def drive_raw_path(remote_path: str | None) -> str:
    """Resolve o caminho lógico da camada bruta no remote."""
    return remote_path or os.getenv("SBMI_DRIVE_RAW_PATH", "raw")


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


@app.command("drive-check")
def drive_check(
    remote: Annotated[str | None, typer.Option()] = None,
    remote_path: Annotated[str | None, typer.Option("--path")] = None,
) -> None:
    """Valida acesso somente leitura ao primeiro nível da pasta bruta."""
    resolved_remote = drive_remote_name(remote)
    resolved_path = drive_raw_path(remote_path)
    entries = check_remote(resolved_remote, resolved_path)
    typer.echo(f"remote={resolved_remote}")
    typer.echo(f"path={resolved_path}")
    typer.echo(f"entries={len(entries)}")
    for entry in entries[:20]:
        typer.echo(entry)
    typer.echo("status=ok")


@app.command("drive-size")
def drive_size(
    remote: Annotated[str | None, typer.Option()] = None,
    remote_path: Annotated[str | None, typer.Option("--path")] = None,
) -> None:
    """Calcula volume e número de objetos antes de baixar qualquer dado."""
    resolved_remote = drive_remote_name(remote)
    resolved_path = drive_raw_path(remote_path)
    result = remote_size(resolved_remote, resolved_path)
    typer.echo(f"remote={resolved_remote}")
    typer.echo(f"path={resolved_path}")
    typer.echo(f"objects={result.count}")
    typer.echo(f"bytes={result.bytes}")
    typer.echo(f"sizeless={result.sizeless}")


@app.command("drive-snapshot")
def drive_snapshot(
    remote: Annotated[str | None, typer.Option()] = None,
    remote_path: Annotated[str | None, typer.Option("--path")] = None,
    snapshots_root: Annotated[
        Path,
        typer.Option(),
    ] = Path(".data/snapshots"),
    snapshot_id: Annotated[str | None, typer.Option()] = None,
) -> None:
    """Cria captura local nova da camada bruta sem apagar nem sobrescrever o Drive."""
    resolved_remote = drive_remote_name(remote)
    resolved_path = drive_raw_path(remote_path)
    target = snapshot_raw(
        remote=resolved_remote,
        remote_path=resolved_path,
        snapshots_root=snapshots_root,
        snapshot_id=snapshot_id,
    )
    typer.echo(f"snapshot={target}")
    typer.echo("status=ok")


if __name__ == "__main__":
    app()
