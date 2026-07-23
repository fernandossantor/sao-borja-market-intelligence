"""Integração controlada com Google Drive por meio do rclone."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

REMOTE_NAME_PATTERN = re.compile(r"^[A-Za-z0-9._-]+$")
SNAPSHOT_ID_PATTERN = re.compile(r"^[A-Za-z0-9._-]+$")


@dataclass(frozen=True)
class RemoteSize:
    """Resumo do tamanho remoto informado pelo rclone."""

    count: int
    bytes: int
    sizeless: int = 0


def require_rclone() -> str:
    """Retorna o executável do rclone ou interrompe com mensagem objetiva."""
    executable = shutil.which("rclone")
    if executable is None:
        raise RuntimeError(
            "rclone não encontrado. Instale-o no Codespace antes de acessar o Drive."
        )
    return executable


def normalize_remote_name(remote: str) -> str:
    """Valida o nome lógico do remote sem aceitar especificações arbitrárias."""
    normalized = remote.strip().removesuffix(":")
    if not normalized or REMOTE_NAME_PATTERN.fullmatch(normalized) is None:
        raise ValueError(
            "Nome de remote inválido. Use apenas letras, números, ponto, hífen ou sublinhado."
        )
    return normalized


def normalize_remote_path(remote_path: str) -> str:
    """Normaliza um caminho relativo dentro do remote."""
    normalized = remote_path.strip().strip("/")
    parts = Path(normalized).parts if normalized else ()
    if any(part in {".", ".."} for part in parts):
        raise ValueError("O caminho remoto não pode conter '.' ou '..'.")
    return "/".join(parts)


def remote_spec(remote: str, remote_path: str = "") -> str:
    """Monta a especificação `remote:caminho` usada pelo rclone."""
    normalized_remote = normalize_remote_name(remote)
    normalized_path = normalize_remote_path(remote_path)
    return f"{normalized_remote}:{normalized_path}"


def run_rclone(arguments: list[str]) -> subprocess.CompletedProcess[str]:
    """Executa rclone sem shell e propaga falhas com a saída original."""
    command = [require_rclone(), *arguments]
    return subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )


def check_remote(remote: str, remote_path: str = "raw") -> list[str]:
    """Lista o primeiro nível do caminho remoto para validar o acesso."""
    result = run_rclone(
        [
            "lsf",
            remote_spec(remote, remote_path),
            "--max-depth",
            "1",
        ]
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def remote_size(remote: str, remote_path: str = "raw") -> RemoteSize:
    """Obtém quantidade de objetos e volume remoto antes de qualquer cópia."""
    result = run_rclone(["size", remote_spec(remote, remote_path), "--json"])
    payload = json.loads(result.stdout)
    return RemoteSize(
        count=int(payload.get("count", 0)),
        bytes=int(payload.get("bytes", 0)),
        sizeless=int(payload.get("sizeless", 0)),
    )


def default_snapshot_id() -> str:
    """Gera identificador UTC estável para uma nova captura."""
    return datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")


def snapshot_raw(
    remote: str,
    remote_path: str,
    snapshots_root: Path,
    snapshot_id: str | None = None,
) -> Path:
    """Copia o conteúdo remoto para uma captura local nova, sem apagar destinos."""
    resolved_id = snapshot_id or default_snapshot_id()
    if SNAPSHOT_ID_PATTERN.fullmatch(resolved_id) is None:
        raise ValueError("Identificador de snapshot inválido.")

    target = snapshots_root.expanduser().resolve() / resolved_id / "raw"
    if target.exists() and any(target.iterdir()):
        raise FileExistsError(f"O snapshot já contém arquivos: {target}")

    target.mkdir(parents=True, exist_ok=True)
    run_rclone(
        [
            "copy",
            remote_spec(remote, remote_path),
            str(target),
            "--create-empty-src-dirs",
            "--check-first",
            "--transfers",
            "4",
            "--checkers",
            "8",
        ]
    )
    return target
