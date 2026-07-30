.PHONY: bootstrap bootstrap-browser install doctor test lint lint-legacy format verify gdrive-check gdrive-inventory gdrive-audit gdrive-audit-inbox gdrive-snapshot-inbox profile-inbox-snapshot triage-inbox-structure audit-inbox-content review-inbox-anomalies build-inbox-staging validate-inbox-staging map-historical-integration map-base-territorial-coverage audit-base-territorial-demography audit-base-territorial-demography-lineage snapshot-base-territorial-demography-census compare-base-territorial-demography-census review-base-territorial-demography-census-quality audit-base-territorial-demography-census-provenance verify-base-territorial-demography-census-authority discover-base-territorial-demography-census-official-products discover-base-territorial-demography-census-sidra-metadata snapshot-base-territorial-demography-census-sidra-values rebuild-base-territorial-demography-census-products snapshot-derived-products audit-derived-products snapshot-social-idsc-source build-social-idsc snapshot-social-ips-published build-social-ips-published build-canonical-territorial-model drive-check drive-size drive-snapshot
.PHONY: audit-base-territorial-fiscal-semantics
.PHONY: audit-base-territorial-rais-semantics
.PHONY: audit-base-territorial-rais-lineage
.PHONY: discover-base-territorial-sidra-historical-metadata
.PHONY: audit-complementary-temporal-matrix
.PHONY: audit-public-funds-temporal-coverage

DRIVE_REMOTE ?= sbmi-drive
DRIVE_PATH ?= raw

bootstrap:
	python -m pip install --upgrade pip setuptools wheel
	python -m pip install -e '.[dev]'
	mkdir -p .data/raw .data/staging .data/curated .data/snapshots .data/manifests .data/audit artifacts manifests reports/generated

bootstrap-browser:
	python -m pip install -e '.[dev,browser]'
	bash scripts/install_playwright_chromium.sh

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

audit-inbox-content:
	python -m sbmi.inbox_content_audit_cli

review-inbox-anomalies:
	python -m sbmi.inbox_anomaly_review_cli

build-inbox-staging:
	python -m sbmi.inbox_staging_cli

validate-inbox-staging:
	python -m sbmi.inbox_staging_validation_cli

map-historical-integration:
	python -m sbmi.historical_integration_map_cli

map-base-territorial-coverage:
	python -m sbmi.base_territorial_coverage_cli

audit-base-territorial-fiscal-semantics:
	python -m sbmi.fiscal_semantic_audit_cli

audit-base-territorial-rais-semantics:
	python -m sbmi.rais_semantic_audit_cli

audit-base-territorial-rais-lineage:
	python -m sbmi.rais_lineage_audit_cli

audit-base-territorial-demography:
	python -m sbmi.demography_audit_cli

audit-base-territorial-demography-lineage:
	python -m sbmi.demography_lineage_cli

snapshot-base-territorial-demography-census:
	python -m sbmi.demography_census_snapshot_cli

compare-base-territorial-demography-census:
	python -m sbmi.demography_census_comparison_cli

review-base-territorial-demography-census-quality:
	python -m sbmi.demography_census_quality_review_cli

audit-base-territorial-demography-census-provenance:
	python -m sbmi.demography_census_provenance_cli

verify-base-territorial-demography-census-authority:
	python -m sbmi.demography_census_authority_cli

discover-base-territorial-demography-census-official-products:
	python -m sbmi.demography_census_official_discovery_cli

discover-base-territorial-demography-census-sidra-metadata:
	python -m sbmi.demography_census_sidra_discovery_cli

discover-base-territorial-sidra-historical-metadata:
	python -m sbmi.sidra_historical_discovery_cli

audit-complementary-temporal-matrix:
	python -m sbmi.complementary_temporal_matrix_cli

snapshot-base-territorial-demography-census-sidra-values:
	python -m sbmi.demography_census_sidra_values_cli

rebuild-base-territorial-demography-census-products:
	python -m sbmi.demography_census_rebuild_cli

snapshot-derived-products:
	python -m sbmi.derived_products_snapshot_cli

audit-derived-products:
	python -m sbmi.derived_products_audit_cli

snapshot-social-idsc-source:
	python -m sbmi.social_idsc_snapshot_cli

build-social-idsc:
	python -m sbmi.social_idsc_cli

snapshot-social-ips-published:
	python -m sbmi.social_ips_snapshot_cli

build-social-ips-published:
	python -m sbmi.social_ips_cli

build-canonical-territorial-model:
	python -m sbmi.canonical_territorial_model_cli

drive-check:
	python -m sbmi.cli drive-check --remote $(DRIVE_REMOTE) --path $(DRIVE_PATH)

drive-size:
	python -m sbmi.cli drive-size --remote $(DRIVE_REMOTE) --path $(DRIVE_PATH)

drive-snapshot:
	python -m sbmi.cli drive-snapshot --remote $(DRIVE_REMOTE) --path $(DRIVE_PATH)
