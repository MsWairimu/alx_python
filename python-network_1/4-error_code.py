#!/usr/bin/python3
"""
Module to fetch and display the body of the response from a given URL.
If the HTTP status code is greater than or equal to 400, display the error code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from the command line argument
    response = requests.get(url)
    
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)

