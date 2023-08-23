#!/usr/bin/python3
"""
Module to send a POST request with an email parameter to a given URL and display the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from the command line argument
    email = sys.argv[2]  # Get the email address from the command line argument

    payload = {'email': email}
    response = requests.post(url, data=payload)
    content = response.text
    print(content)

