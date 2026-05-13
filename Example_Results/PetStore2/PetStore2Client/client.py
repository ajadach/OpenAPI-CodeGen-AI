"""Main client for PetStore2Client API."""

import requests

__all__ = ["PetStore2Client"]

from . import basic
from .modules import Pet, Store, User


class PetStore2Client:
    """Main API client for Swagger Petstore."""

    def __init__(self, base_url: str = "https://petstore.swagger.io/v2") -> None:
        """Initialize the PetStore2Client.

        Args:
            base_url (str): The base URL for the API. Defaults to 'https://petstore.swagger.io/v2'.
        """
        if not base_url.startswith(("http://", "https://")):
            base_url = f"https://{base_url}"
        basic.BASE_URL = base_url
        basic.SESSION = requests.Session()
        self.pet = Pet()
        self.store = Store()
        self.user = User()
