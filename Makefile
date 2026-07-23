.PHONY: install doctor test lint format

install:
	python -m pip install -e '.[dev]'

doctor:
	sbmi doctor

test:
	pytest

lint:
	ruff check src tests

format:
	ruff format src tests
	ruff check --fix src tests
