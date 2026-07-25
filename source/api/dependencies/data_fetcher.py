import io
import json

import pandas as pd
import requests
from fastapi import HTTPException

from source.config.settings import settings


def _get_map_key() -> str:
    if not settings.MAP_KEY:
        raise HTTPException(status_code=500, detail="MAP_KEY is not configured — check your .env file")
    return settings.MAP_KEY


def _fetch_csv_as_json(url: str):
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=503, detail=f"NASA FIRMS API unreachable or errored: {e}")

    try:
        df = pd.read_csv(io.StringIO(resp.text))
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"NASA FIRMS API returned unparseable data: {e}")

    # df.to_json() returns a JSON *string* — parse it back into a real
    # list so it isn't double-encoded when FastAPI serializes the response.
    return json.loads(df.to_json(orient='records'))


def fetch_global_widfire_data():
    """
    Fetches the global data related to wildfires from the NASA FIRMS API and returns it as JSON.
    """
    map_key = _get_map_key()
    area_url = f'https://firms.modaps.eosdis.nasa.gov/api/area/csv/{map_key}/VIIRS_NOAA20_NRT/world/1'
    return _fetch_csv_as_json(area_url)


def fetch_data_by_country_id(country_id: str):
    """
    Fetch wildfire data from NASA FIRMS API filtered by country ID.
    """
    map_key = _get_map_key()
    country_url = f'https://firms.modaps.eosdis.nasa.gov/api/country/csv/{map_key}/VIIRS_NOAA20_NRT/{country_id}/4'
    return _fetch_csv_as_json(country_url)