import json
import requests

def retrieve_and_save_latest_data(data_dir='data'):
    filename_to_endpoint_url = {
         'wind_farm_data': 'https://www.thecrownestate.co.uk/api/energy-map/wind-farm-data',
         'wind_graph_data': 'https://www.thecrownestate.co.uk/api/energy-map/wind-graph-all-Data'
    }

    for filename, endpoint_url in filename_to_endpoint_url.items():
        r = requests.get(endpoint_url)

        with open(f'{data_dir}/{filename}.json', 'w') as fp:
            json.dump(r.json(), fp)
            
    return 

retrieve_and_save_latest_data()