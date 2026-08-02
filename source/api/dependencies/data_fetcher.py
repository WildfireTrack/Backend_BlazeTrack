from source.config.settings import settings
import pandas as pd
import json



def fetch_global_widfire_data():
    """
    Fetches global wildfire data from the specified URL and returns it as a pandas DataFrame.
    
    Returns:
        pd.DataFrame: A DataFrame containing the global wildfire data.
    """
    url = f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/{settings.MAP_KEY}/VIIRS_NOAA20_NRT/world/1"
    try:
        data = pd.read_csv(url)
        total_rows= len(data)
        data = data[data['frp'] > 50]
        total_filtered_data = len(data)
        return_dict = {
            "total_rows": total_rows,
            "total_filtered_data": total_filtered_data,
            "data": data.to_dict()  
        }
        return_json = json.dumps(return_dict) 
        return return_json  
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return pd.DataFrame()  
