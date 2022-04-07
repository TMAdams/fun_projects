#!/usr/bin/python

# I am a magical 8 ball, query my wisdom

# Import python modules

import requests
import json

# Prepare function to get a random number from RANDOM.org


def fetch_random_number():
    query_data = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": "1luVRBATYPwOuTGR5W1iGhY39sMv8BTLQs1cqP4dnuEN1qJrEoZRBVdOlkveBQrIEsMhIVKV1F+GyvwGVX1Svw==",
            "n": 1,
            "min": 1,
            "max": 20,
            "replacement": True
        },
        'id': 1
    }
    headers = {
        'Content-type': 'application/json',
        'Content-Length': '200',
        'Accept': 'application/json'
    }
    data = json.dumps(query_data)
    response = requests.post(
        url='https://api.random.org/json-rpc/2/invoke',
        data=data,
        headers=headers
    )
    return(print(response.text))
