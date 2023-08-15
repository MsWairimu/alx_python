#!/usr/bin/python3
"""
Module to fetch and display the status of https://alu-intranet.hbtn.io
"""

import requests

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)

