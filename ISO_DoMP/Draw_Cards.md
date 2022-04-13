# Commands to draw cards from the deck of minor prophecies

This deck was designed by Ashley Tuffin

Run this in an interactive session so numbers are all picked beforehand but cards are only revealed when needed

```python
# Import modules

import requests
import json

# Generate a list of random numbers to simulate card deck order for drawing

query_data = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": your_api_key,
        "n": 34,
        "min": 1,
        "max": 34,
        "replacement": False
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
```
