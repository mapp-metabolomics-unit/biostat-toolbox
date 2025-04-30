"""Submodule to fetch in different ways the species."""

from io import StringIO
from typing import Dict

import pandas as pd
from cache_decorator import Cache
from requests import request

QLEVER_URL = "https://qlever.cs.uni-freiburg.de/api/wikidata"


@Cache(
    validity_duration="8w",
    use_approximated_hash=True,
)
def sparql_to_text(query: str, url: str = QLEVER_URL, as_post: bool = False) -> str:
    """TODO: Add docstring."""

    method = "POST" if as_post else "GET"
    return request(
        method,
        url,
        params={"query": query},
        headers={
            "Accept": "text/csv",
            "Accept-Encoding": "gzip,deflate",
            "User-Agent": "LOTUS project database dumper",
        },
        timeout=70,
    ).text


@Cache(
    "{cache_dir}/{function_name}/{_hash}.csv.gz",
    use_approximated_hash=True,
)
def text_to_csv(text_from_query: str) -> pd.DataFrame:
    """Function that converts a text from a SPARQL query to a DataFrame."""
    df = pd.read_csv(StringIO(text_from_query))
    return df


def get_taxon_qids(taxon_name: str) -> str:
    """TODO: Add docstring."""
    query = f"""PREFIX wdt: <http://www.wikidata.org/prop/direct/>
            SELECT ?taxon WHERE {{
                ?taxon wdt:P225 {taxon_name} .
            }}"""
