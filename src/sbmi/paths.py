"""Resolução centralizada e portável de caminhos do projeto."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProjectPaths:
    project_root: Path
    data_root: Path
    raw: Path
    staging: Path
    curated: Path
    artifacts: Path
    manifests: Path
    reports: Path

    @classmethod
    def from_environment(cls) -> "ProjectPaths":
        project_root = Path(
            os.getenv("SBMI_PROJECT_ROOT", Path.cwd())
        ).expanduser().resolve()
        data_root = Path(
            os.getenv("SBMI_DATA_ROOT", project_root / ".data")
        ).expanduser().resolve()

        return cls(
            project_root=project_root,
            data_root=data_root,
            raw=data_root / "raw",
            staging=data_root / "staging",
            curated=data_root / "curated",
            artifacts=project_root / "artifacts",
            manifests=project_root / "manifests",
            reports=project_root / "reports" / "generated",
        )

    def ensure_local_directories(self) -> None:
        for path in (
            self.raw,
            self.staging,
            self.curated,
            self.artifacts,
            self.manifests,
            self.reports,
        ):
            path.mkdir(parents=True, exist_ok=True)
