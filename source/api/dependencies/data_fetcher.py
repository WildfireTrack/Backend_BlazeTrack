import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def fetch_global_widfire_data():
    """
    fetchesthe global data related to wildfires from the NASA FIRMS API and returns it as a pandas DataFrame.
    """
    MAP_KEY = os.getenv('MAP_KEY')
    area_url = f'https://firms.modaps.eosdis.nasa.gov/api/area/csv/{MAP_KEY}/VIIRS_NOAA20_NRT/world/1'
    df_area = pd.read_csv(area_url)

    return df_area.to_json(orient='records')

def fetch_data_by_country_id(country_id : str):
    """
    fetch json data from nasa api by country id
    """
    MAP_KEY = os.getenv('MAP_KEY')
    country_url = f'https://firms.modaps.eosdis.nasa.gov/api/country/csv/{MAP_KEY}/MODIS_NRT/{country_id}/4'
    df_country = pd.read_csv(country_url)

    return df_country.to_json(orient='records')