from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from apps.business_trips.models import BusinessTrip
from apps.business_trips.serializers import AccommodationSerializer, TransportationSerializer, DailyAllowanceSerializer, \
    PrimarySourceDocumentSerializer, BusinessTripCertificateSerializer, BusinessTripReportSerializer, \
    AdvancedCostReportSerializer
from apps.users.models import User


class BusinessTripListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CRMBusinessTripEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class CRMBusinessTripAdminListSerializer(serializers.ModelSerializer):
    user = CRMBusinessTripEmployeeSerializer(many=False, read_only=True)

    class Meta:
        model = BusinessTrip
        fields = ('id', 'user', 'status', 'departure_date', 'return_date', 'total_cost', 'departure_country',
                  'departure_city', 'destination_country', 'destination_city', 'daily_allowance_status')


class BusinessTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessTrip
        fields = '__all__'


class CRMBusinessTripDetailSerializer(serializers.ModelSerializer):
    accommodations = AccommodationSerializer(many=True, read_only=True)
    transportations = TransportationSerializer(many=True, read_only=True)
    daily_allowance = DailyAllowanceSerializer(many=True, read_only=True)
    primary_source_documents = PrimarySourceDocumentSerializer(many=True, read_only=True)
    business_trip_certificates = BusinessTripCertificateSerializer(many=True, read_only=True)
    business_trip_reports = BusinessTripReportSerializer(many=True, read_only=True)
    advanced_cost_reports = AdvancedCostReportSerializer(many=True, read_only=True)

    class Meta:
        model = BusinessTrip
        fields = ('id', 'user', 'status', 'departure_date', 'return_date', 'duration', 'departure_country',
                  'departure_city', 'destination_country', 'destination_city', 'total_cost', 'supervisor', 'assistant',
                  'goal', 'accommodations', 'transportations', 'daily_allowance', 'business_trip_reports',
                  'primary_source_documents', 'advanced_cost_reports', 'business_trip_certificates')


class StatusSerializer(serializers.Serializer):
    value = serializers.CharField()
    label = serializers.CharField()

