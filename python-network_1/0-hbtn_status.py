#!/usr/bin/env python3
"""
This module fetches the content from https://alu-intranet.hbtn.io/status
and prints the body response in a specific format.
"""

import requests

def fetch_status():
    """
    Fetches the content from the given URL and prints the type and content
    of the response.
    """
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

if __name__ == "__main__":
    fetch_status()
