# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 04:10:54 2022

@author: xwtar
"""

import requests
import json

# Set up the API endpoint and API key
API_ENDPOINT = "https://api.openai.com/v1/papers/search"
API_KEY = "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"

# Set up the API parameters
params = {
    "query": "3D Printing",
    "sort": "relevance",
    "page": 1,
    "per_page": 10
}

# Send the API request
response = requests.get(API_ENDPOINT, params=params, headers={"Authorization": f"Bearer {API_KEY}"})

# Check the status code of the response
if response.status_code == 200:
    # Print the response if the request is successful
    print(response.text)
else:
    # Print an error message if the request is not successful
    print("An error occurred:", response.status_code)
    print(response.text)