#!/usr/bin/env python3
"""
-A Module taking in a URL,
sending a request to the URL and 
displaying the body of the response

-If the HTTP status code is greater than or equal to 400, 
print: Error code: followed by the value of the HTTP status code
"""

import requests
import sys

def fetch_url(url):
    """
    -Taking in a URL,
    sending a request to the URL and 
    displaying the body of the response
    
    -If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code
    
    Args:
        url (str): The URL
    """
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
