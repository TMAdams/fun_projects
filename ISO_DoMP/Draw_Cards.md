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

result_json = response.json()

shuffled_deck = result["result"]["random"]["data"]

count = 0


def draw_card():
    global shuffled_deck
    global count
    card_number = str(shuffled_deck[count])
    count += 1
    match card_number:
        case "1":
            card = "Naxos"
        case "2":
            card = "Empire"
        case "3":
            card = "The Twin Moons"
        case "4":
            card = "Imperia"
        case "5":
            card = "Sestos"
        case "6":
            card = "The Oracles"
        case "7":
            card = "The Augura"
        case "8":
            card = "The Giant"
        case "9":
            card = "The Mech Knight"
        case "10":
            card = "The Dreary"
        case "11":
            card = "The Lidless Eye"
        case "12":
            card = "Riot"
        case "13":
            card = "Honour"
        case "14":
            card = "The Forum"
        case "15":
            card = "Blood"
        case "16":
            card = "The Magistrate"
        case "17":
            card = "The Cockatrice"
        case "18":
            card = "The Sisyphean Beetle"
        case "19":
            card = "The General"
        case "20":
            card = "The Raider"
        case "21":
            card = "The Erased House"
        case "22":
            card = "The Commissar"
        case "23":
            card = "The Emerald Library"
        case "24":
            card = "Victory"
        case "25":
            card = "The Aether"
        case "26":
            card = "The Diplomancer"
        case "27":
            card = "The Pit Fighter"
        case "28":
            card = "The Palace Kitchen"
        case "29":
            card = "The Bazaar"
        case "30":
            card = "The Exiled Seer"
        case "31":
            card = "The Spoiled Noble"
        case "32":
            card = "The Inquisitor"
        case "33":
            card = "Wounded"
        case "34":
            card = "The Silkworm"
    return(card)

# Simply run this command whenever you need a new card

draw_card()
```
