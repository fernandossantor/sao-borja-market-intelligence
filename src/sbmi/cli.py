"""Interface de linha de comando do projeto."""

import os
from pathlib import Path
from typing import Annotated

import pandas as pd
import typer

from sbmi.drive import check_remote, remote_size, snapshot_raw
from sbmi.google_drive import (
    build_authorized_session,
    build_drive_inventory,
    check_root_folder,
    service_account_info_from_environment,
)
from sbmi.inventory import build_inventory, duplicate_candidates
from sbmi.paths import ProjectPaths

app = typer.Typer(no_args_is_help=True)


def drive_remote_name(remote: str | None) -> str:
    """Resolve o nome do remote sem expor credenciais."""
    return remote or os.getenv("SBMI_DRIVE_REMOTE", "sbmi-drive")


def drive_raw_path(remote_path: str | None) -> str:
    """Resolve o caminho lógico da camada bruta no remote."""
    return remote_path or os.getenv("SBMI_DRIVE_RAW_PATH", "raw")


def drive_root_folder_id(root_folder_id: str | None) -> str:
    """Resolve o ID da pasta raiz sem incorporá-lo ao código."""
    resolved = root_folder_id or os.getenv("SBMI_DRIVE_ROOT_FOLDER_ID")
    if not resolved:
        raise typer.BadParameter(
            "Informe --root-folder-id ou defina SBMI_DRIVE_ROOT_FOLDER_ID."
        )
    return resolved.strip()


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


@app.command("gdrive-check")
def gdrive_check(
    root_folder_id: Annotated[str | None, typer.Option()] = None,
    secret_env: Annotated[str, typer.Option()] = "SBMI_GDRIVE_SA_B64",
) -> None:
    """Valida a conta de serviço e a pasta raiz sem baixar arquivos."""
    resolved_root = drive_root_folder_id(root_folder_id)
    info = service_account_info_from_environment(secret_env)
    session = build_authorized_session(info)
    root, entries = check_root_folder(session, resolved_root)

    typer.echo(f"root_name={root.get('name', '')}")
    typer.echo(f"root_mime_type={root.get('mimeType', '')}")
    typer.echo(f"first_level_entries={len(entries)}")
    for entry in sorted(entries, key=lambda item: str(item.get("name", "")))[:20]:
        typer.echo(f"{entry.get('name', '')}\t{entry.get('mimeType', '')}")
    typer.echo("scope=drive.readonly")
    typer.echo("status=ok")


@app.command("gdrive-inventory")
def gdrive_inventory(
    root_folder_id: Annotated[str | None, typer.Option()] = None,
    secret_env: Annotated[str, typer.Option()] = "SBMI_GDRIVE_SA_B64",
    output: Annotated[Path, typer.Option()] = Path(
        ".data/manifests/google_drive_inventory.csv"
    ),
) -> None:
    """Gera inventário recursivo de metadados sem copiar os conteúdos."""
    resolved_root = drive_root_folder_id(root_folder_id)
    info = service_account_info_from_environment(secret_env)
    session = build_authorized_session(info)
    result = build_drive_inventory(session, resolved_root)

    output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output, index=False)

    folders = int(result["is_folder"].sum()) if not result.empty else 0
    files = int((~result["is_folder"]).sum()) if not result.empty else 0
    known_bytes = int(result["size_bytes"].fillna(0).sum()) if not result.empty else 0
    missing_size = int(result["size_bytes"].isna().sum()) if not result.empty else 0
    sha256_available = (
        int(result["sha256_checksum"].notna().sum()) if not result.empty else 0
    )

    typer.echo(f"entries={len(result)}")
    typer.echo(f"folders={folders}")
    typer.echo(f"files={files}")
    typer.echo(f"known_bytes={known_bytes}")
    typer.echo(f"missing_size={missing_size}")
    typer.echo(f"sha256_available={sha256_available}")
    typer.echo(f"output={output.resolve()}")
    typer.echo("status=ok")


@app.command("drive-check")
def drive_check(
    remote: Annotated[str | None, typer.Option()] = None,
    remote_path: Annotated[str | None, typer.Option("--path")] = None,
) -> None:
    """Valida acesso pelo rclone ao primeiro nível da pasta bruta."""
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
    """Calcula volume pelo rclone antes de baixar qualquer dado."""
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
    """Cria captura local nova pelo rclone, sem apagar nem sobrescrever o Drive."""
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
