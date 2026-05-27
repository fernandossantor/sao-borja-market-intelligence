# =========================================
# BRAZILIAN DATA RULES
# =========================================

SUPPORTED_ENCODINGS = [
    "utf-8",
    "latin1",
    "cp1252",
    "iso-8859-1"
]

SUPPORTED_DELIMITERS = [
    ";",
    ",",
    "\t"
]

BRAZILIAN_DATE_PATTERNS = [
    "%Y",
    "%Y%m",
    "%m/%Y",
    "%d/%m/%Y"
]

IBGE_CODE_LENGTH = 7

KNOWN_IDENTIFIER_COLUMNS = [
    "ibge",
    "codigo_ibge",
    "cod_ibge",
    "cnae",
    "cbo",
    "id_municipio",
    "municipio_id"
]

BRAZILIAN_NUMERIC_TYPES = {
    "currency": {
        "decimal": ",",
        "thousands": "."
    },

    "percentage": {
        "range_min": 0,
        "range_max": 100
    }
}

AGRO_UNITS = [
    "ha",
    "hectare",
    "ton",
    "kg",
    "sacas",
    "cabecas"
]

PEOPLE_UNITS = [
    "habitantes",
    "beneficiarios",
    "empregados",
    "vinculos",
    "servidores"
]
