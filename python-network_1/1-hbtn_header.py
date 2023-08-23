#!/usr/bin/python3
"""
Module to fetch and display the value of the X-Request-Id header from a given URL's response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from the command line argument
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)

