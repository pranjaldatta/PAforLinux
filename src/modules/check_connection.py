import requests


def check_connection():
    """
    A simple function to check connection.
    Returns:
    True if internet is available.
    False if internet is unavailable.

    """
    url = "https://www.google.com"
    timeout = 5
    try:
        _ = requests.get(url=url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

