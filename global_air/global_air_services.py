import requests
from .global_air_serializers import (
    SearchAirFlightsSerializer,
    FareFamiliesSerializer,
    FareRulesSerializer,
    BookFlightSerializer,
    IssueTicketsSerializer,
    RefreshBookingStatusSerializer,
    SearchRailSerializer,
    RailOptionDetailsSerializer,
    RailPrebookSerializer,
    RailBookSerializer
)
from typing import List


class GlobalAirServices:
    def __init__(self, api_key: str):
        """
        Initialize the GlobalAirServices class with an API key.
        """
        self.api_key = api_key
        self.base_url = ""  # TODO: Add the base URL

    def _make_request(self, url: str, method: str, payload=None) -> dict:
        """
        Make a request to the GlobalAir API.
        """
        headers = {
            "X-API-Key": self.api_key,
            "Authorization": "Bearer <JWT token>"
        }
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=payload)
        else:
            raise ValueError("Unsupported HTTP method")

        return response.json()

    def _serialize(self, serializer_class, payload) -> dict:
        """
        Validate and serialize the payload using the provided serializer class.
        """
        serializer = serializer_class(data=payload)
        serializer.is_valid(raise_exception=True)
        serialized_payload = serializer.validated_data

        return serialized_payload

    def search_air_flights(
            self,
            origin: str, destination: str,
            date: str, cabin: str,
            adult_count: int = 1, child_count: int = 0, infant_count: int = 0
    ):
        """
        Search for flights based on the provided parameters.
        """
        url = self.base_url + "air/search"
        payload = {
            "legs": [
                {
                    "origin": origin,
                    "destination": destination,
                    "date": date
                }
            ],
            "adultCount": adult_count,
            "childCount": child_count,
            "infantCount": infant_count,
            "cabin": cabin
        }
        serialized_payload = self._serialize(SearchAirFlightsSerializer, payload)
        return self._make_request(url, "POST", serialized_payload)

    def get_fare_families(self, opt: str):
        """
        Get fare families for the provided option ID.
        """
        url = self.base_url + "air/fare-families"
        payload = {
            "opt": opt
        }
        serialized_payload = self._serialize(FareFamiliesSerializer, payload)
        return self._make_request(url, "POST", serialized_payload)

    def get_fare_rules(self, opt: str):
        """
        Get fare rules for the provided option ID.
        """
        url = self.base_url + "air/rules"
        payload = {
            "opt": opt
        }
        serialized_payload = self._serialize(FareRulesSerializer, payload)
        return self._make_request(url, "POST", serialized_payload)

    def book_flight(
            self,
            option_id: str, ff_id: str,
            email: str, phone: str,
            client: dict, passengers: List[dict]
    ):
        """
        Book a flight based on the provided parameters.
        ff_id is the fare family ID.
        passengers is a list of dictionaries, each dictionary representing a passenger.
        """
        url = self.base_url + "air/book"
        payload = {
            "optionId": option_id,
            "fareFamilyId": ff_id,
            "email": email,
            "countryCode": "7",
            "phone": phone,
            "client": client,
            "passengers": passengers
        }
        serialized_payload = self._serialize(BookFlightSerializer, payload)
        return self._make_request(url, "POST", serialized_payload)

    def get_countries_list(self):
        """
        Get a list of countries supported by GlobalAir.
        """
        url = self.base_url + "countries/list"
        return self._make_request(url, "GET")

    def issue_tickets(self, action: str, token: str):
        """
        Issue tickets for the provided action and token.
        Action example: "confirm", etc
        """
        url = self.base_url + "orders/auth"
        payload = {
            "action": action,
            "token": token
        }
        serialized_payload = self._serialize(IssueTicketsSerializer, payload)
        return self._make_request(url, "POST", serialized_payload)

    def refresh_booking_status(self, order_id: int):
        """
        Refresh the booking status for the provided order ID.
        """
        url = self.base_url + f"orders/refresh?id={order_id}"
        payload = {
            "orderId": order_id
        }
        serialized_payload = self._serialize(RefreshBookingStatusSerializer, payload)
        return self._make_request(url, "POST", serialized_payload)

    def search_rail(self, origin: str, destination: str, date: str):
        """
        Search for rail options based on the provided parameters.
        """
        url = self.base_url + "rail/search"
        payload = {
            "origin": origin,
            "destination": destination,
            "date": date
        }
        serialized_payload = self._serialize(SearchRailSerializer, payload)
        return self._make_request(url, "POST", serialized_payload)

    def get_rail_option_details(self, option_id: int, wagon_type: str):
        """
        Get rail option details for the provided option ID and wagon type.
        """
        url = self.base_url + "rail/option-details"
        payload = {
            "optionId": option_id,
            "wagonType": wagon_type
        }
        serialized_payload = self._serialize(RailOptionDetailsSerializer, payload)
        return self._make_request(url, "POST", serialized_payload)

    def rail_prebook(self, option_id: int, email: str, phone: str, country_code: str, seats: list, number: int, fare_id: str, passengers: List[dict]):
        """
        Prebook a rail option based on the provided parameters.
        seats is a list of dictionaries, each dictionary representing a seat.
        passengers is a list of dictionaries, each dictionary representing a passenger.
        """
        url = self.base_url + "rail/prebook"
        payload = {
            "optionId": option_id,
            "email": email,
            "phone": phone,
            "countryCode": country_code,
            "seats": seats,
            "number": number,
            "fareId": fare_id,
            "passengers": passengers
        }
        serialized_payload = self._serialize(RailPrebookSerializer, payload)
        return self._make_request(url, "POST", serialized_payload)

    def rail_book(self, order_id: int):
        """
        Book a rail option based on the provided order ID.
        """
        url = self.base_url + "rail/book"
        payload = {
            "orderId": order_id
        }
        serialized_payload = self._serialize(RailBookSerializer, payload)
        return self._make_request(url, "POST", serialized_payload)
