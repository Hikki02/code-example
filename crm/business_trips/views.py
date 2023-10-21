from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.business_trips.models import BusinessTrip
from apps.business_trips.models.business_trip_model import BUSINESS_TRIP_STATUSES, DAILY_ALLOWANCE_STATUSES
from .filters import BusinessTripFilter
from .serializers import CRMBusinessTripAdminListSerializer, BusinessTripSerializer, StatusSerializer, \
    BusinessTripListPagination, CRMBusinessTripDetailSerializer
from .services import CrmBusinessTripService

from utils.swagger.parameters import is_approved, employee_name, destination_place, \
    departure_place, business_trip_status, daily_allowance_status, start_date, end_date


class CRMBusinessTripViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """
    Returns a list of all company business trips in the form of incomplete cards.
    Returns a list of all company business trips as an array of objects, with 10 items per page.

    Parameters:
    - `status` (string, optional): Filter by status (possible values: 'approved', 'unapproved').

    If parameters are not specified, all company business trips will be returned.
    """
    serializer_class = CRMBusinessTripAdminListSerializer
    service = CrmBusinessTripService()
    filterset_class = BusinessTripFilter
    pagination_class = BusinessTripListPagination
    queryset = BusinessTrip.objects.all()
    swagger_tags = ['CRM Business Trips']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CRMBusinessTripDetailSerializer
        return self.serializer_class

    def get_queryset(self):
        user = self.request.user
        queryset = self.service.get_all_by_user_company(user)
        queryset = self.filterset_class(self.request.query_params, queryset=queryset).qs
        return queryset

    @swagger_auto_schema(manual_parameters=[is_approved, employee_name, destination_place, departure_place, business_trip_status, daily_allowance_status, start_date, end_date])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def statuses(self, request):
        """
        Returns a list of business trip statuses.
        Returns a list of business trip statuses as an array of objects with the following fields:
        - `value` (string): Status value (e.g., 'awaiting_review').
        - `label` (string): Status name in Russian (e.g., 'Заявка на проверке').
        """
        return Response([{'value': key, 'label': value} for key, value in BUSINESS_TRIP_STATUSES])

    @action(detail=False, methods=['get'])
    def daily_allowance_status(self, request):
        """
        Returns a list of daily allowance statuses.
        Returns a list of daily allowance statuses as an array of objects with the following fields:
        - `value` (string): Status value (e.g., 'not_accrued').
        - `label` (string): Status name in Russian (e.g., 'Не начислены').
        """
        return Response([{'value': key, 'label': value} for key, value in DAILY_ALLOWANCE_STATUSES])

