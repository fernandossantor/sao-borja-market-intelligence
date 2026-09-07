"""Registro dos anexos oficiais de IPM definitivo publicados pela Receita Estadual/RS."""

from __future__ import annotations

IPM_DEFINITIVE_PAGE = "https://atendimento.receita.rs.gov.br/ipm-definitivos"

IPM_DEFINITIVE_ARCHIVE_URLS: dict[int, str] = {
    2026: "https://atendimento.receita.rs.gov.br/upload/arquivos/202512/17093842-daim545-3.zip",
    2025: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21133005-20241211105501daim545-2025.zip",
    2024: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21133004-20231220101855definitivodoe-20231220-2024.zip",
    2023: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21133003-20221207110353definitivodoe-20221207-2023.zip",
    2022: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21133002-20211216093532definitivodoe-20211215-2022.zip",
    2021: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21133001-20201127100859definitivodoe-20201127-2021.zip",
    2020: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21133000-20191112103752definitivo-doe-12112019-2020.zip",
    2019: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21132959-20181105083634deinitivodoe-20181016-2019.zip",
    2018: "https://admin.atendimento.receita.rs.gov.br/upload/arquivos/202508/21134338-201801050923246-definitivodoe-20180501.zip",
    2017: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134336-20161109154240definitivodoe-2017.zip",
    2016: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134335-20161109154826definitivodoe-2016.zip",
    2015: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134334-20161110084443definitivodoe-2015.zip",
    2014: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134333-20161110084609definitivodoe-2014.zip",
    2013: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134331-20161110084756definitivodoe-2013.zip",
    2012: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134330-20161110084912definitivodoe-2012.zip",
    2011: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134329-20161110085107definitivodoe-2011.zip",
    2010: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134328-20161110085219definitivodoe-2010.zip",
    2009: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134326-20161110085346definitivodoe-2009.zip",
    2008: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134325-20161110090950definitivodoe-2008.zip",
    2007: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134324-20161110091022definitivodoe-2007.zip",
    2006: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134323-20161110091046definitivodoe-2006.zip",
    2005: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134322-20161110091116definitivodoe-2005.zip",
    2004: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134320-20161110091138definitivodoe-2004.zip",
    2003: "https://atendimento.receita.rs.gov.br/upload/arquivos/202508/21134319-20161110091205definitivodoe-2003.zip",
}


def validate_source_registry() -> None:
    """Recusa lacunas, anos extras ou URLs fora dos hosts oficiais registrados."""
    expected = set(range(2003, 2027))
    observed = set(IPM_DEFINITIVE_ARCHIVE_URLS)
    if observed != expected:
        raise ValueError(
            f"Registro IPM incompleto: faltam={sorted(expected-observed)} extras={sorted(observed-expected)}"
        )
    allowed_hosts = (
        "https://atendimento.receita.rs.gov.br/",
        "https://admin.atendimento.receita.rs.gov.br/",
    )
    for year, url in IPM_DEFINITIVE_ARCHIVE_URLS.items():
        if not url.startswith(allowed_hosts) or not url.lower().endswith(".zip"):
            raise ValueError(f"URL oficial inválida para {year}: {url}")
