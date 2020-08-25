import json
import requests

session = requests.Session()
session.headers.update({'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"})

def run():
    with open("apis.json", 'r') as apis:
        apis_data = json.load(apis)
        for api in apis_data:
            api_response = session.get(api)
            if api_response.ok:
                # More customisation e.g checks of the response can be done here e.g
                # api_response.json()['success'] == 'True'
                # Ping Healthchecks
                requests.get(apis_data[api])
