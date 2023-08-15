import requests

def fetch_and_display_status(url):
    """
    Fetches the given URL and displays the response body in a formatted way.
    
    Args:
        url (str): The URL to fetch the status from.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if there's an HTTP error
        data = response.json()
        
        for key, value in data.items():
            print(f"- {key}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    fetch_and_display_status(url)
