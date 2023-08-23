#!/usr/bin/python3
"""
Module to send a POST request with a letter parameter to http://0.0.0.0:5000/search_user and process the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {'q': letter}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

