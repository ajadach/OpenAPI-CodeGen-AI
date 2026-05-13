"""Pet module for PetStore2Client API."""

from typing import Any, Optional

from pydantic import validate_call
from robot.api.deco import keyword

from .. import basic


class Pet:
    """Everything about your Pets."""

    ROBOT_LIBRARY_SCOPE = "SUITE"

    @property
    def _base_url(self) -> str:
        return basic.BASE_URL

    @property
    def _session(self):
        return basic.SESSION

    @keyword("Post Upload File")
    @validate_call
    def post_upload_file(
        self,
        pet_id: int,
        additional_metadata: Optional[str] = None,
        file: Optional[Any] = None,
    ) -> dict:
        """Uploads an image.

        Args:
            pet_id (int): ID of pet to update.
            additional_metadata (Optional[str]): Additional data to pass to server.
            file (Optional[Any]): File to upload.

        Returns:
            dict: ApiResponse object with code, type, and message.
        """
        url = f"{self._base_url}/pet/{pet_id}/uploadImage"
        data = {}
        if additional_metadata is not None:
            data["additionalMetadata"] = additional_metadata
        files = {}
        if file is not None:
            files["file"] = file
        response = self._session.post(url, data=data or None, files=files or None)
        response.raise_for_status()
        return response.json()

    @keyword("Post Add Pet")
    @validate_call
    def post_add_pet(self, body: dict) -> None:
        """Add a new pet to the store.

        Args:
            body (dict): Pet object that needs to be added to the store.

        Returns:
            None: No content returned on success.
        """
        url = f"{self._base_url}/pet"
        response = self._session.post(url, json=body)
        response.raise_for_status()

    @keyword("Put Update Pet")
    @validate_call
    def put_update_pet(self, body: dict) -> None:
        """Update an existing pet.

        Args:
            body (dict): Pet object that needs to be added to the store.

        Returns:
            None: No content returned on success.
        """
        url = f"{self._base_url}/pet"
        response = self._session.put(url, json=body)
        response.raise_for_status()

    @keyword("Get Find Pets By Status")
    @validate_call
    def get_find_pets_by_status(self, status: list) -> list:
        """Finds Pets by status.

        Args:
            status (list): Status values that need to be considered for filter.

        Returns:
            list: List of Pet objects matching the status filter.
        """
        url = f"{self._base_url}/pet/findByStatus"
        response = self._session.get(url, params=[("status", s) for s in status])
        response.raise_for_status()
        return response.json()

    @keyword("Get Find Pets By Tags")
    @validate_call
    def get_find_pets_by_tags(self, tags: list) -> list:
        """Finds Pets by tags.

        Args:
            tags (list): Tags to filter by.

        Returns:
            list: List of Pet objects matching the tag filter.
        """
        url = f"{self._base_url}/pet/findByTags"
        response = self._session.get(url, params=[("tags", t) for t in tags])
        response.raise_for_status()
        return response.json()

    @keyword("Get Pet By Id")
    @validate_call
    def get_pet_by_id(self, pet_id: int) -> dict:
        """Find pet by ID.

        Args:
            pet_id (int): ID of pet to return.

        Returns:
            dict: Pet object.
        """
        url = f"{self._base_url}/pet/{pet_id}"
        response = self._session.get(url)
        response.raise_for_status()
        return response.json()

    @keyword("Post Update Pet With Form")
    @validate_call
    def post_update_pet_with_form(
        self,
        pet_id: int,
        name: Optional[str] = None,
        status: Optional[str] = None,
    ) -> None:
        """Updates a pet in the store with form data.

        Args:
            pet_id (int): ID of pet that needs to be updated.
            name (Optional[str]): Updated name of the pet.
            status (Optional[str]): Updated status of the pet.

        Returns:
            None: No content returned on success.
        """
        url = f"{self._base_url}/pet/{pet_id}"
        data = {}
        if name is not None:
            data["name"] = name
        if status is not None:
            data["status"] = status
        response = self._session.post(url, data=data)
        response.raise_for_status()

    @keyword("Delete Pet")
    @validate_call
    def delete_pet(self, pet_id: int, api_key: Optional[str] = None) -> None:
        """Deletes a pet.

        Args:
            pet_id (int): Pet id to delete.
            api_key (Optional[str]): API key header.

        Returns:
            None: No content returned on success.
        """
        url = f"{self._base_url}/pet/{pet_id}"
        headers = {}
        if api_key is not None:
            headers["api_key"] = api_key
        response = self._session.delete(url, headers=headers or None)
        response.raise_for_status()
