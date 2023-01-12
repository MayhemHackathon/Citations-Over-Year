from __future__ import print_function
import os
import json
import pretty_json

PYOACORE_KEY = "RDGVzeO2d6jgNHFyaoXfupK9WSI5Bh4k"
os.environ["CORE_API_KEY"] = PYOACORE_KEY
import time
import requests
import swagger_client
import pyoacore
from pyoacore.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = pyoacore.ArticlesApi()
core_id = '42' # str | The id of the article

# try:
#     # Get articles by ID
#     api_instance.articles_get_core_id_get(core_id)
# except ApiException as e:
#     print("Exception when calling ArticlesApi->articles_get_core_id_get: %s\n" % e)


api_key = "RDGVzeO2d6jgNHFyaoXfupK9WSI5Bh4k"
# with open ("apikey.txt", "r") as apikey_file:
#     api_key=apikey_file.readlines()[0].strip()
api_endpoint = "https://api.core.ac.uk/v3/"


def get_entity(url_fragment):
    headers={"Authorization":"Bearer "+api_key}
    response = requests.get(api_endpoint + url_fragment, headers=headers)
    if response.status_code == 200:
        return response.json(), response.elapsed.total_seconds()
    else:
        print(f"Error code {response.status_code}, {response.content}")

data_provider, elapsed = get_entity("data-providers/1")
# pretty_json(data_provider)
json_formatted_str = json.dumps(data_provider, indent=2)

print(json_formatted_str)
