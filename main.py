import json
import requests

def run():
    with open("apis.json", 'r') as apis:
        apis_data = json.load(apis)
        for api in apis_data:
            api_response = requests.get(api)
            if api_response.ok:
                # More customisation e.g checks of the response can be done here e.g
                # api_response.json()['success'] == 'True'
                # Ping Healthchecks
                requests.get(apis_data[api])
