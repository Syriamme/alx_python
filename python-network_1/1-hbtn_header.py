#!/usr/bin/env python3

"""
The module will send a request to a specific URL
and print value of the variable in the response header.
"""


import requests

import sys

def fetch_request_id(url):
    """
    Sending a request to the given URL and printing the value
    of X-Request-Id
    Args:
        url: The URL
    """
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    print(request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_request_id(url)
