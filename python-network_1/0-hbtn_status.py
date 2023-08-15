#!/usr/bin/env python3

"""
The module will fetch resources from https://alu-intranet.hbtn.io/status
and will print the body response in a certain format.
"""


import requests

def fetch_status():
    """
    -Fetches the resources from URL specified
    -print (type and content) of the http response
    """

    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    
    print("Body response:")

    print("\t- type:", type(response.text))

    print("\t- content:", response.text)

if __name__ == "__main__":
    fetch_status()
