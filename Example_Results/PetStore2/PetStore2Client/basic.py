"""Shared configuration for the API client.

BASE_URL and SESSION are set by the client __init__ before any module is used.
All modules import this module and read BASE_URL and SESSION at call time.
"""

import requests

BASE_URL: str = "https://petstore.swagger.io/v2"
SESSION: requests.Session = requests.Session()
