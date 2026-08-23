from source.config.settings import settings
import pandas as pd
import json
import h3


def fetch_global_widfire_data():
    url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{settings.MAP_KEY}/VIIRS_NOAA20_NRT/world/1"
    try:
        df = pd.read_csv(url)
        df['latitude'] = df['latitude'].astype(float)
        df['longitude'] = df['longitude'].astype(float)
        resolution = 8
        df['h3_index'] = [h3.latlng_to_cell(lat, lng, resolution) for lat, lng in zip(df['latitude'], df['longitude'])]
        df = df.drop_duplicates(subset=['h3_index'])
        
        df = df[df['frp'] > 5]
        json_df = df.to_dict(orient="records")
        return json_df
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return pd.DataFrame()  
