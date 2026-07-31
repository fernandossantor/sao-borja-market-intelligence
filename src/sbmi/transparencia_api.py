"""Cliente mínimo e seguro para a API do Portal da Transparência."""

from __future__ import annotations

import os
from collections.abc import Mapping
from typing import Any
from urllib.parse import urljoin, urlparse

import requests

API_BASE_URL = "https://api.portaldatransparencia.gov.br/api-de-dados/"
API_KEY_ENV = "TRANSPARENCIA_API_KEY"


def transparencia_api_headers(api_key: str | None = None) -> dict[str, str]:
    """Retorna os cabeçalhos oficiais sem expor a chave em mensagens."""
    key = api_key if api_key is not None else os.getenv(API_KEY_ENV)
    if not key or not key.strip():
        raise RuntimeError(
            f"{API_KEY_ENV} não está configurada; a API do Portal exige uma chave"
        )
    return {"Accept": "application/json", "chave-api-dados": key.strip()}


def fetch_transparencia_api_json(
    endpoint: str,
    *,
    params: Mapping[str, Any] | None = None,
    timeout: float = 30,
    session: requests.Session | None = None,
    api_key: str | None = None,
) -> Any:
    """Consulta um endpoint relativo e devolve o JSON decodificado."""
    if not endpoint or endpoint.startswith(("http://", "https://")):
        raise ValueError("endpoint deve ser relativo à API oficial")
    url = urljoin(API_BASE_URL, endpoint.lstrip("/"))
    if urlparse(url).netloc != urlparse(API_BASE_URL).netloc:
        raise ValueError("endpoint fora do host oficial")
    if timeout <= 0:
        raise ValueError("timeout deve ser positivo")
    client = session or requests.Session()
    response = client.get(
        url,
        params=params,
        headers=transparencia_api_headers(api_key),
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()
