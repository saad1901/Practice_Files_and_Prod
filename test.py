import requests

def is_internet_available():
    try:
        requests.get("http://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

if is_internet_available():
    print("Internet is available.")
else:
    print("Internet is not available.")
