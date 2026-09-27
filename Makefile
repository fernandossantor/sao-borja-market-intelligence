.PHONY: bootstrap bootstrap-browser install doctor test lint lint-legacy format verify gdrive-check gdrive-inventory gdrive-audit gdrive-audit-inbox gdrive-snapshot-inbox profile-inbox-snapshot triage-inbox-structure audit-inbox-content review-inbox-anomalies build-inbox-staging validate-inbox-staging map-historical-integration map-base-territorial-coverage audit-base-territorial-demography audit-base-territorial-demography-lineage snapshot-base-territorial-demography-census compare-base-territorial-demography-census review-base-territorial-demography-census-quality audit-base-territorial-demography-census-provenance verify-base-territorial-demography-census-authority discover-base-territorial-demography-census-official-products discover-base-territorial-demography-census-sidra-metadata snapshot-base-territorial-demography-census-sidra-values rebuild-base-territorial-demography-census-products snapshot-derived-products audit-derived-products snapshot-social-idsc-source build-social-idsc snapshot-social-ips-published build-social-ips-published build-canonical-territorial-model drive-check drive-size drive-snapshot
.PHONY: audit-base-territorial-fiscal-semantics
.PHONY: audit-base-territorial-rais-semantics
.PHONY: audit-base-territorial-rais-lineage
.PHONY: discover-base-territorial-sidra-historical-metadata
.PHONY: audit-complementary-temporal-matrix
.PHONY: audit-public-funds-temporal-coverage
.PHONY: snapshot-base-territorial-demography-historical-values
.PHONY: snapshot-base-territorial-demography-census-series
.PHONY: snapshot-base-territorial-economy-gdp-series
.PHONY: build-base-territorial-business-employment-series
.PHONY: build-base-territorial-cnpj-control
.PHONY: build-base-territorial-education-series
.PHONY: build-base-territorial-public-finance-series
.PHONY: snapshot-base-territorial-siconfi-dca
.PHONY: build-base-territorial-siconfi-dca-series
.PHONY: build-canonical-territorial-model-series

DRIVE_REMOTE ?= sbmi-drive
DRIVE_PATH ?= raw
EXECUTION_TIMESTAMP = $(shell date -u +%Y%m%d-%H%M%S)
PUBLIC_FINANCE_SOURCE_DIR ?= .data/snapshots/web/complementary_source_values/complementary-source-values-20260729-220618/sebrae_observatorio_profile
SICONFI_DCA_SNAPSHOT_ID ?= siconfi-dca-4318002-2019-2025-$(EXECUTION_TIMESTAMP)
SICONFI_DCA_SNAPSHOT_DIR ?=
CNPJ_ESTABLISHMENTS_DIR ?=
CNPJ_COMPANIES_DIR ?=
CNPJ_MUNICIPALITIES_ZIP ?=
CNPJ_EXECUTION_ID ?= cnpj-territorial-control-$(EXECUTION_TIMESTAMP)
CANONICAL_SERIES_BASE_ROOT ?=
CANONICAL_DEMOGRAPHY_HISTORICAL_PATH ?=
CANONICAL_DEMOGRAPHY_CENSUS_PATH ?=
CANONICAL_ECONOMY_GDP_PATH ?=
CANONICAL_BUSINESS_EMPLOYMENT_PATH ?=
CANONICAL_EDUCATION_PATH ?=
CANONICAL_PUBLIC_FINANCE_PATH ?=
CANONICAL_SICONFI_DCA_PATH ?=

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

snapshot-base-territorial-demography-historical-values:
	python -m sbmi.demography_historical_values_cli

snapshot-base-territorial-demography-census-series:
	python -m sbmi.demography_census_series_cli

snapshot-base-territorial-economy-gdp-series:
	python -m sbmi.economy_gdp_series_cli

build-base-territorial-business-employment-series:
	python -m sbmi.business_employment_series_cli

build-base-territorial-cnpj-control:
	test -n "$(CNPJ_ESTABLISHMENTS_DIR)" || \
		(printf '%s\n' 'CNPJ_ESTABLISHMENTS_DIR is required' >&2; exit 2)
	test -n "$(CNPJ_COMPANIES_DIR)" || \
		(printf '%s\n' 'CNPJ_COMPANIES_DIR is required' >&2; exit 2)
	test -n "$(CNPJ_MUNICIPALITIES_ZIP)" || \
		(printf '%s\n' 'CNPJ_MUNICIPALITIES_ZIP is required' >&2; exit 2)
	python -m sbmi.cnpj_territorial_control_cli \
		--establishments-dir $(CNPJ_ESTABLISHMENTS_DIR) \
		--companies-dir $(CNPJ_COMPANIES_DIR) \
		--municipalities-zip $(CNPJ_MUNICIPALITIES_ZIP) \
		--execution-id $(CNPJ_EXECUTION_ID)

build-base-territorial-education-series:
	python -m sbmi.education_series_cli

build-base-territorial-public-finance-series:
	python -m sbmi.public_finance_series_cli \
		--execution-id public-finance-series-$(EXECUTION_TIMESTAMP) \
		--source-dir $(PUBLIC_FINANCE_SOURCE_DIR)

snapshot-base-territorial-siconfi-dca:
	python -m sbmi.siconfi_dca_snapshot_cli --snapshot-id $(SICONFI_DCA_SNAPSHOT_ID)

build-base-territorial-siconfi-dca-series:
	test -n "$(SICONFI_DCA_SNAPSHOT_DIR)" || \
		(printf '%s\n' 'SICONFI_DCA_SNAPSHOT_DIR is required' >&2; exit 2)
	python -m sbmi.siconfi_dca_series_cli \
		--execution-id siconfi-dca-series-$(EXECUTION_TIMESTAMP) \
		--snapshot-dir $(SICONFI_DCA_SNAPSHOT_DIR)

build-canonical-territorial-model-series:
	test -n "$(CANONICAL_SERIES_BASE_ROOT)" || (printf '%s\n' 'CANONICAL_SERIES_BASE_ROOT is required' >&2; exit 2)
	test -n "$(CANONICAL_DEMOGRAPHY_HISTORICAL_PATH)" || (printf '%s\n' 'CANONICAL_DEMOGRAPHY_HISTORICAL_PATH is required' >&2; exit 2)
	test -n "$(CANONICAL_DEMOGRAPHY_CENSUS_PATH)" || (printf '%s\n' 'CANONICAL_DEMOGRAPHY_CENSUS_PATH is required' >&2; exit 2)
	test -n "$(CANONICAL_ECONOMY_GDP_PATH)" || (printf '%s\n' 'CANONICAL_ECONOMY_GDP_PATH is required' >&2; exit 2)
	test -n "$(CANONICAL_BUSINESS_EMPLOYMENT_PATH)" || (printf '%s\n' 'CANONICAL_BUSINESS_EMPLOYMENT_PATH is required' >&2; exit 2)
	test -n "$(CANONICAL_EDUCATION_PATH)" || (printf '%s\n' 'CANONICAL_EDUCATION_PATH is required' >&2; exit 2)
	test -n "$(CANONICAL_PUBLIC_FINANCE_PATH)" || (printf '%s\n' 'CANONICAL_PUBLIC_FINANCE_PATH is required' >&2; exit 2)
	test -n "$(CANONICAL_SICONFI_DCA_PATH)" || (printf '%s\n' 'CANONICAL_SICONFI_DCA_PATH is required' >&2; exit 2)
	python -m sbmi.canonical_territorial_model_series_cli \
		--base-root $(CANONICAL_SERIES_BASE_ROOT) \
		--demography-historical-path $(CANONICAL_DEMOGRAPHY_HISTORICAL_PATH) \
		--demography-census-path $(CANONICAL_DEMOGRAPHY_CENSUS_PATH) \
		--economy-gdp-path $(CANONICAL_ECONOMY_GDP_PATH) \
		--business-employment-path $(CANONICAL_BUSINESS_EMPLOYMENT_PATH) \
		--education-path $(CANONICAL_EDUCATION_PATH) \
		--public-finance-path $(CANONICAL_PUBLIC_FINANCE_PATH) \
		--siconfi-dca-path $(CANONICAL_SICONFI_DCA_PATH)

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
