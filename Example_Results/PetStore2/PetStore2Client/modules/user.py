"""User module for PetStore2Client API."""

from pydantic import validate_call
from robot.api.deco import keyword

from .. import basic


class User:
    """Operations about user."""

    ROBOT_LIBRARY_SCOPE = "SUITE"

    @property
    def _base_url(self) -> str:
        return basic.BASE_URL

    @property
    def _session(self):
        return basic.SESSION

    @keyword("Post Create Users With List Input")
    @validate_call
    def post_create_users_with_list_input(self, body: list) -> None:
        """Creates list of users with given input array.

        Args:
            body (list): List of user objects.

        Returns:
            None: No content returned on success.
        """
        url = f"{self._base_url}/user/createWithList"
        response = self._session.post(url, json=body)
        response.raise_for_status()

    @keyword("Get User By Name")
    @validate_call
    def get_user_by_name(self, username: str) -> dict:
        """Get user by user name.

        Args:
            username (str): The name that needs to be fetched.

        Returns:
            dict: User object.
        """
        url = f"{self._base_url}/user/{username}"
        response = self._session.get(url)
        response.raise_for_status()
        return response.json()

    @keyword("Put Update User")
    @validate_call
    def put_update_user(self, username: str, body: dict) -> None:
        """Updated user.

        Args:
            username (str): Name that needs to be updated.
            body (dict): Updated user object.

        Returns:
            None: No content returned on success.
        """
        url = f"{self._base_url}/user/{username}"
        response = self._session.put(url, json=body)
        response.raise_for_status()

    @keyword("Delete User")
    @validate_call
    def delete_user(self, username: str) -> None:
        """Delete user.

        Args:
            username (str): The name that needs to be deleted.

        Returns:
            None: No content returned on success.
        """
        url = f"{self._base_url}/user/{username}"
        response = self._session.delete(url)
        response.raise_for_status()

    @keyword("Get Login User")
    @validate_call
    def get_login_user(self, username: str, password: str) -> str:
        """Logs user into the system.

        Args:
            username (str): The user name for login.
            password (str): The password for login in clear text.

        Returns:
            str: Login token or session info.
        """
        url = f"{self._base_url}/user/login"
        response = self._session.get(url, params={"username": username, "password": password})
        response.raise_for_status()
        return response.json()

    @keyword("Get Logout User")
    @validate_call
    def get_logout_user(self) -> None:
        """Logs out current logged in user session.

        Returns:
            None: No content returned on success.
        """
        url = f"{self._base_url}/user/logout"
        response = self._session.get(url)
        response.raise_for_status()

    @keyword("Post Create Users With Array Input")
    @validate_call
    def post_create_users_with_array_input(self, body: list) -> None:
        """Creates list of users with given input array.

        Args:
            body (list): List of user objects.

        Returns:
            None: No content returned on success.
        """
        url = f"{self._base_url}/user/createWithArray"
        response = self._session.post(url, json=body)
        response.raise_for_status()

    @keyword("Post Create User")
    @validate_call
    def post_create_user(self, body: dict) -> None:
        """Create user.

        Args:
            body (dict): Created user object.

        Returns:
            None: No content returned on success.
        """
        url = f"{self._base_url}/user"
        response = self._session.post(url, json=body)
        response.raise_for_status()
