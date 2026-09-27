from sbmi.ipm_definitive_sources import (
    IPM_DEFINITIVE_ARCHIVE_URLS,
    IPM_DEFINITIVE_PAGE,
    validate_source_registry,
)


def test_ipm_definitive_source_registry_is_complete() -> None:
    validate_source_registry()
    assert sorted(IPM_DEFINITIVE_ARCHIVE_URLS) == list(range(2003, 2027))
    assert IPM_DEFINITIVE_PAGE.endswith("/ipm-definitivos")
