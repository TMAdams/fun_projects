# Commands to draw cards from the deck of minor prophecies

This deck was designed by Ashley Tuffin

Run this in an interactive session so numbers are all picked beforehand but cards are only revealed when needed

```python
# Import modules

import requests
import json
from PIL import Image

# Generate a list of random numbers to simulate card deck order for drawing

query_data = {
    "jsonrpc": "2.0",
    "method": "generateIntegers",
    "params": {
        "apiKey": "your_api_key",
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

shuffled_deck = result_json["result"]["random"]["data"]

count = 0


def draw_card():
    global shuffled_deck
    global count
    global img
    card_number = str(shuffled_deck[count])
    count += 1
    match card_number:
        case "1":
            card = "Naxos"
            img = Image.open("ISO\Naxos.jpg")
            img.show()
        case "2":
            card = "Empire"
            img = Image.open("ISO\Empire.jpg")
            img.show()
        case "3":
            card = "The Twin Moons"
            img = Image.open("ISO\The_Twin_Moons.jpg")
            img.show()
        case "4":
            card = "Imperia"
            img = Image.open("ISO\Imperia.jpg")
            img.show()
        case "5":
            card = "Sestos"
            img = Image.open("ISO\Sestos.jpg")
            img.show()
        case "6":
            card = "The Oracles"
            img = Image.open("ISO\The_Oracles.jpg")
            img.show()
        case "7":
            card = "The Augura"
            img = Image.open("ISO\The_Augura.jpg")
            img.show()
        case "8":
            card = "The Giant"
            img = Image.open("ISO\The_Giant.jpg")
            img.show()
        case "9":
            card = "The Mech Knight"
            img = Image.open("ISO\The_Mech_Knight.jpg")
            img.show()
        case "10":
            card = "The Dreary"
            img = Image.open("ISO\The_Dreary.jpg")
            img.show()
        case "11":
            card = "The Lidless Eye"
            img = Image.open("ISO\The_Lidless_Eye.jpg")
            img.show()
        case "12":
            card = "Riot"
            img = Image.open("ISO\Riot.jpg")
            img.show()
        case "13":
            card = "Honour"
            img = Image.open("ISO\Honour.jpg")
            img.show()
        case "14":
            card = "The Forum"
            img = Image.open("ISO\The_Forum.jpg")
            img.show()
        case "15":
            card = "Blood"
            img = Image.open("ISO\Blood.jpg")
            img.show()
        case "16":
            card = "The Magistrate"
            img = Image.open("ISO\The_Magistrate.jpg")
            img.show()
        case "17":
            card = "The Cockatrice"
            img = Image.open("ISO\The_Cockatrice.jpg")
            img.show()
        case "18":
            card = "The Sisyphean Beetle"
            img = Image.open("ISO\The_Sisyphean_Beetle.jpg")
            img.show()
        case "19":
            card = "The General"
            img = Image.open("ISO\The_General.jpg")
            img.show()
        case "20":
            card = "The Raider"
            img = Image.open("ISO\The_Raider.jpg")
            img.show()
        case "21":
            card = "The Erased House"
            img = Image.open("ISO\The_Erased_House.jpg")
            img.show()
        case "22":
            card = "The Commissar"
            img = Image.open("ISO\The_Commissar.jpg")
            img.show()
        case "23":
            card = "The Emerald Library"
            img = Image.open("ISO\The_Emerald_Library.jpg")
            img.show()
        case "24":
            card = "Victory"
            img = Image.open("ISO\Victory.jpg")
            img.show()
        case "25":
            card = "The Aether"
            img = Image.open("ISO\The_Aether.jpg")
            img.show()
        case "26":
            card = "The Diplomancer"
            img = Image.open("ISO\The_Diplomancer.jpg")
            img.show()
        case "27":
            card = "The Pit Fighter"
            img = Image.open("ISO\The_Pit_Fighter.jpg")
            img.show()
        case "28":
            card = "The Palace Kitchen"
            img = Image.open("ISO\The_Palace_Kitchen.jpg")
            img.show()
        case "29":
            card = "The Bazaar"
            img = Image.open("ISO\The_Bazaar.jpg")
            img.show()
        case "30":
            card = "The Exiled Seer"
            img = Image.open("ISO\The_Exiled_Seer.jpg")
            img.show()
        case "31":
            card = "The Spoiled Noble"
            img = Image.open("ISO\The_Spoiled_Noble.jpg")
            img.show()
        case "32":
            card = "The Inquisitor"
            img = Image.open("ISO\The_Inquisitor.jpg")
            img.show()
        case "33":
            card = "Wounded"
            img = Image.open("ISO\Wounded.jpg")
            img.show()
        case "34":
            card = "The Silkworm"
            img = Image.open("ISO\The_Silkworm.jpg")
            img.show()
    return(card)

# Simply run this command whenever you need a new card

draw_card()
```
