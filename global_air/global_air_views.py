from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .global_air_services import GlobalAirServices
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


class GlobalAirBaseView(APIView):
    service_class = GlobalAirServices

    def get_instance(self):
        api_key = "api_key"
        return self.service_class(api_key)

    def validate_data(self, serializer_class, payload):
        serializer = serializer_class(data=payload)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return data


class SearchAirFlightsView(GlobalAirBaseView):
    serializer_class = SearchAirFlightsSerializer

    def post(self, request):
        data = self.validate_data(self.serializer_class, request.data)
        global_air = self.get_instance()

        search_results = global_air.search_air_flights(
            origin=data["origin"],
            destination=data["destination"],
            date=data["date"],
            cabin=data["cabin"],
            adult_count=data["adult_count"],
            child_count=data["child_count"],
            infant_count=data["infant_count"],
        )
        return Response(search_results, status=status.HTTP_200_OK)


class FareFamiliesView(GlobalAirBaseView):
    serializer_class = FareFamiliesSerializer

    def post(self, request):
        data = self.validate_data(self.serializer_class, request.data)
        global_air = self.get_instance()

        fare_families = global_air.get_fare_families(opt=data["opt"])
        return Response(fare_families, status=status.HTTP_200_OK)


class FareRulesView(GlobalAirBaseView):
    serializer_class = FareRulesSerializer

    def post(self, request):
        data = self.validate_data(self.serializer_class, request.data)
        global_air = self.get_instance()

        fare_rules = global_air.get_fare_rules(opt=data["opt"])
        return Response(fare_rules, status=status.HTTP_200_OK)


class BookFlightView(GlobalAirBaseView):
    serializer_class = BookFlightSerializer

    def post(self, request):
        data = self.validate_data(self.serializer_class, request.data)
        global_air = self.get_instance()

        booking = global_air.book_flight(
            option_id=data["option_id"],
            ff_id=data["ff_id"],
            email=data["email"],
            phone=data["phone"],
            client=data["client"],
            passengers=data["passengers"]
        )
        return Response(booking, status=status.HTTP_200_OK)


class GetCountriesListView(generics.ListAPIView, GlobalAirBaseView):
    def get(self, request, **kwargs):
        global_air = self.get_instance()

        countries = global_air.get_countries_list()
        return Response(countries, status=status.HTTP_200_OK)


class IssueTicketsView(GlobalAirBaseView):
    serializer_class = IssueTicketsSerializer

    def post(self, request):
        data = self.validate_data(self.serializer_class, request.data)
        global_air = self.get_instance()

        ticket = global_air.issue_tickets(
            action=data["action"],
            token=data["token"],
        )
        return Response(ticket, status=status.HTTP_200_OK)


class RefreshBookingStatusView(GlobalAirBaseView):
    serializer_class = RefreshBookingStatusSerializer

    def post(self, request):
        data = self.validate_data(self.serializer_class, request.data)
        global_air = self.get_instance()

        booking_status = global_air.refresh_booking_status(order_id=data["order_id"],)
        return Response(booking_status, status=status.HTTP_200_OK)


class SearchRailView(GlobalAirBaseView):
    serializer_class = SearchRailSerializer

    def post(self, request):
        data = self.validate_data(self.serializer_class, request.data)
        global_air = self.get_instance()

        search_results = global_air.search_rail(
            origin=data["origin"],
            destination=data["destination"],
            date=data["date"],
        )
        return Response(search_results, status=status.HTTP_200_OK)


class RailOptionDetailsView(GlobalAirBaseView):
    serializer_class = RailOptionDetailsSerializer

    def post(self, request):
        data = self.validate_data(self.serializer_class, request.data)
        global_air = self.get_instance()

        option_details = global_air.get_rail_option_details(
            option_id=data["option_id"],
            wagon_type=data["wagon_type"],
        )
        return Response(option_details, status=status.HTTP_200_OK)


class RailPrebookView(GlobalAirBaseView):
    serializer_class = RailPrebookSerializer

    def post(self, request):
        data = self.validate_data(self.serializer_class, request.data)
        global_air = self.get_instance()

        prebook = global_air.rail_prebook(
            option_id=data["option_id"],
            email=data["email"],
            phone=data["phone"],
            country_code=data["country_code"],
            seats=data["seats"],
            number=data["number"],
            fare_id=data["fare_id"],
            passengers=data["passengers"],
        )
        return Response(prebook, status=status.HTTP_200_OK)


class RailBookView(GlobalAirBaseView):
    serializer_class = RailBookSerializer

    def post(self, request):
        data = self.validate_data(self.serializer_class, request.data)
        global_air = self.get_instance()

        book = global_air.rail_book(order_id=data["order_id"],)
        return Response(book, status=status.HTTP_200_OK)
