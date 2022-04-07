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
    return(str(print(response.text)))

# Translate your random number to a magic 8 ball response


def get_answer():
    number = fetch_random_number()
    match number:
        case "1":
            answer = "It is certain."
        case "2":
            answer = "It is decidedly so."
        case "3":
            answer = "Without a doubt."
        case "4":
            answer = "Yes definitely."
        case "5":
            answer = "You may rely on it."
        case "6":
            answer = "As I see it, yes."
        case "7":
            answer = "Most likely."
        case "8":
            answer = "Outlook good."
        case "9":
            answer = "Yes."
        case "10":
            answer = "Signs point to yes."
        case "11":
            answer = "Reply hazy, try again."
        case "12":
            answer = "Ask again later."
        case "13":
            answer = "Better not tell you now."
        case "14":
            answer = "Cannot predict now."
        case "15":
            answer = "Concentrate and ask again."
        case "16":
            answer = "Don't count on it."
        case "17":
            answer = "My reply is no."
        case "18":
            answer = "My sources say no."
        case "19":
            answer = "Outlook not so good."
        case "20":
            answer = "Very doubtful."
    return(answer)

# Prepare main function


def main():
    print(get_answer())
