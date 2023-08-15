#!/usr/bin/env python3
"""
my_module

This module is used to fetch the content from the specified URL (https://alu-intranet.hbtn.io/status)
and display the body of the response with proper tabulation.
"""

import requests

def fetch_url_content():
    """
    Fetches the content from the specified URL and prints the response body.

    The function uses the requests package to make a GET request to the URL and then prints
    the content of the response, preceded by a tabulation.
    """
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    print('\t- {}'.format(response.text))

if __name__ == "__main__":
    fetch_url_content()
