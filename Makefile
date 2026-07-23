.PHONY: bootstrap install doctor test lint lint-legacy format verify

bootstrap:
	python -m pip install --upgrade pip setuptools wheel
	python -m pip install -e '.[dev]'
	mkdir -p .data/raw .data/staging .data/curated artifacts manifests reports/generated

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
