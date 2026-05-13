"""Store module for PetStore2Client API."""

from pydantic import validate_call
from robot.api.deco import keyword

from .. import basic


class Store:
    """Access to Petstore orders."""

    ROBOT_LIBRARY_SCOPE = "SUITE"

    @property
    def _base_url(self) -> str:
        return basic.BASE_URL

    @property
    def _session(self):
        return basic.SESSION

    @keyword("Get Inventory")
    @validate_call
    def get_inventory(self) -> dict:
        """Returns pet inventories by status.

        Returns:
            dict: Map of status codes to quantities.
        """
        url = f"{self._base_url}/store/inventory"
        response = self._session.get(url)
        response.raise_for_status()
        return response.json()

    @keyword("Post Place Order")
    @validate_call
    def post_place_order(self, body: dict) -> dict:
        """Place an order for a pet.

        Args:
            body (dict): Order placed for purchasing the pet.

        Returns:
            dict: Order object.
        """
        url = f"{self._base_url}/store/order"
        response = self._session.post(url, json=body)
        response.raise_for_status()
        return response.json()

    @keyword("Get Order By Id")
    @validate_call
    def get_order_by_id(self, order_id: int) -> dict:
        """Find purchase order by ID.

        Args:
            order_id (int): ID of the order that needs to be fetched.

        Returns:
            dict: Order object.
        """
        url = f"{self._base_url}/store/order/{order_id}"
        response = self._session.get(url)
        response.raise_for_status()
        return response.json()

    @keyword("Delete Order")
    @validate_call
    def delete_order(self, order_id: int) -> None:
        """Delete purchase order by ID.

        Args:
            order_id (int): ID of the order that needs to be deleted.

        Returns:
            None: No content returned on success.
        """
        url = f"{self._base_url}/store/order/{order_id}"
        response = self._session.delete(url)
        response.raise_for_status()
