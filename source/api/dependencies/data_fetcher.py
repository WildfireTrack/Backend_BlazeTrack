from source.config.settings import settings
import pandas as pd



def fetch_global_widfire_data():
    """
    Fetches global wildfire data from the specified URL and returns it as a pandas DataFrame.
    
    Returns:
        pd.DataFrame: A DataFrame containing the global wildfire data.
    """
    url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{settings.MAP_KEY}/VIIRS_NOAA20_NRT/world/1"
    try:
        data = pd.read_csv(url)
        return data.to_json(orient="records")  # Convert DataFrame to JSON format
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error