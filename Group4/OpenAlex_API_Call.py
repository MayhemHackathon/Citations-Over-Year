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

# Print the response
print(response.text)
