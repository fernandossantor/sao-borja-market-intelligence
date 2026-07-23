.PHONY: bootstrap install doctor test lint lint-legacy format verify gdrive-check gdrive-inventory gdrive-audit gdrive-audit-inbox gdrive-snapshot-inbox profile-inbox-snapshot triage-inbox-structure drive-check drive-size drive-snapshot

DRIVE_REMOTE ?= sbmi-drive
DRIVE_PATH ?= raw

bootstrap:
	python -m pip install --upgrade pip setuptools wheel
	python -m pip install -e '.[dev]'
	mkdir -p .data/raw .data/staging .data/curated .data/snapshots .data/manifests .data/audit artifacts manifests reports/generated

install: bootstrap

doctor:
	python -m sbmi.cli doctor

test:
	python -m pytest

lint:
	python -m ruff check src/sbmi tests

lint-legacy:
	python -m ruff check src --exclude sbmi

format:
	python -m ruff format src/sbmi tests
	python -m ruff check --fix src/sbmi tests

verify: doctor test lint

gdrive-check:
	python -m sbmi.cli gdrive-check

gdrive-inventory:
	python -m sbmi.cli gdrive-inventory

gdrive-audit:
	python -m sbmi.cli gdrive-audit

gdrive-audit-inbox:
	python -m sbmi.inbox_cli

gdrive-snapshot-inbox:
	python -m sbmi.inbox_snapshot_cli

profile-inbox-snapshot:
	python -m sbmi.inbox_profile_cli

triage-inbox-structure:
	python -m sbmi.inbox_structure_triage_cli

drive-check:
	python -m sbmi.cli drive-check --remote $(DRIVE_REMOTE) --path $(DRIVE_PATH)

drive-size:
	python -m sbmi.cli drive-size --remote $(DRIVE_REMOTE) --path $(DRIVE_PATH)

drive-snapshot:
	python -m sbmi.cli drive-snapshot --remote $(DRIVE_REMOTE) --path $(DRIVE_PATH)
