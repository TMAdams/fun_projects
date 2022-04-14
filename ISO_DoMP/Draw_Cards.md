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
        "n": 39,
        "min": 1,
        "max": 39,
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
            card = "Naxos - Your home is safe, but with a cost"
            img = Image.open("ISO\Naxos.jpg")
            img.show()
        case "2":
            card = "Empire - Blessed by their might, you are inspired"
            img = Image.open("ISO\Empire.jpg")
            img.show()
        case "3":
            card = "The Twin Moons - They dance around you with riches"
            img = Image.open("ISO\The_Twin_Moons.jpg")
            img.show()
        case "4":
            card = "Imperia - Your defences bolster"
            img = Image.open("ISO\Imperia.jpg")
            img.show()
        case "5":
            card = "Sestos - Your property revoked"
            img = Image.open("ISO\Sestos.jpg")
            img.show()
        case "6":
            card = "The Oracle - You see a glimpse of future suffering, now avoid it"
            img = Image.open("ISO\The_Oracle.jpg")
            img.show()
        case "7":
            card = "The Augura - You will be visited"
            img = Image.open("ISO\The_Augura.jpg")
            img.show()
        case "8":
            card = "The Giant - You are mighty"
            img = Image.open("ISO\The_Giant.jpg")
            img.show()
        case "9":
            card = "The Mecha Pyrrhichios - Enhance your form"
            img = Image.open("ISO\The_Mecha_Pyrrhichios.jpg")
            img.show()
        case "10":
            card = "The Dreary - You are drained of function"
            img = Image.open("ISO\The_Dreary.jpg")
            img.show()
        case "11":
            card = "The Lidless Eye - Nothing is hidden"
            img = Image.open("ISO\The_Lidless_Eye.jpg")
            img.show()
        case "12":
            card = "Riot - The chaos of riot envelops you"
            img = Image.open("ISO\Riot.jpg")
            img.show()
        case "13":
            card = "Honour - Act with integrity"
            img = Image.open("ISO\Honour.jpg")
            img.show()
        case "14":
            card = "The Forum - A public spectacle"
            img = Image.open("ISO\The_Forum.jpg")
            img.show()
        case "15":
            card = "Blood - Bleed by your word"
            img = Image.open("ISO\Blood.jpg")
            img.show()
        case "16":
            card = "The Magistrate - Act in shadows"
            img = Image.open("ISO\The_Magistrate.jpg")
            img.show()
        case "17":
            card = "The Cockatrice - A fortuitous sighting"
            img = Image.open("ISO\The_Cockatrice.jpg")
            img.show()
        case "18":
            card = "The Sisyphean Beetle - You're up shit mountain"
            img = Image.open("ISO\The_Sisyphean_Beetle.jpg")
            img.show()
        case "19":
            card = "The General - You lead an army with vigour"
            img = Image.open("ISO\The_General.jpg")
            img.show()
        case "20":
            card = "The Raider - Make your own luck"
            img = Image.open("ISO\The_Raider.jpg")
            img.show()
        case "21":
            card = "The Erased House - Something is misplaced, forgotten"
            img = Image.open("ISO\The_Erased_House.jpg")
            img.show()
        case "22":
            card = "The Commissar - Morale is high"
            img = Image.open("ISO\The_Commissar.jpg")
            img.show()
        case "23":
            card = "The Emerald Library - The stacks remember"
            img = Image.open("ISO\The_Emerald_Library.jpg")
            img.show()
        case "24":
            card = "Victory - Salvage of your enemies"
            img = Image.open("ISO\Victory.jpg")
            img.show()
        case "25":
            card = "The Aether - Go forth and prosper"
            img = Image.open("ISO\The_Aether.jpg")
            img.show()
        case "26":
            card = "The Diplomancer - Your silver tounge wins favour"
            img = Image.open("ISO\The_Diplomancer.jpg")
            img.show()
        case "27":
            card = "Breach - Repair existing damage before all else"
            img = Image.open("ISO\Breach.jpg")
            img.show()
        case "28":
            card = "The Palace Kitchen - Your panty is well-stocked"
            img = Image.open("ISO\The_Palace_Kitchen.jpg")
            img.show()
        case "29":
            card = "The Bazaar - There is strength in exchange"
            img = Image.open("ISO\The_Bazaar.jpg")
            img.show()
        case "30":
            card = "The Exiled Seer - You find answers you did not seek"
            img = Image.open("ISO\The_Exiled_Seer.jpg")
            img.show()
        case "31":
            card = "The Spoiled Noble - Riches for the few"
            img = Image.open("ISO\The_Spoiled_Noble.jpg")
            img.show()
        case "32":
            card = "The Inquisitor - Knowledge is gained through purpose"
            img = Image.open("ISO\The_Inquisitor.jpg")
            img.show()
        case "33":
            card = "The Wound - You were careless"
            img = Image.open("ISO\The_Wound.jpg")
            img.show()
        case "34":
            card = "The Silkworm - Fortune favours the bold"
            img = Image.open("ISO\The_Silkworm.jpg")
            img.show()
        case "35":
            card = "Pandosia - An experiment pays off"
            img = Image.open("ISO\Pandosia.jpg")
            img.show()
        case "36":
            card = "The Kleisoura - So focused outwards, you forgot to look in"
            img = Image.open("ISO\The_Kleisoura.jpg")
            img.show()
        case "37":
            card = "The Sextant - You navigate paths with ease"
            img = Image.open("ISO\The_Sextant.jpg")
            img.show()
        case "38":
            card = "Wartorn Earth - Land lost to battle"
            img = Image.open("ISO\Wartorn_Earth.jpg")
            img.show()
        case "39":
            card = "Dishonour - Watch where you tread"
            img = Image.open("ISO\Dishonour.jpg")
            img.show()
    return(card)

# Simply run this command whenever you need a new card

draw_card()
```
