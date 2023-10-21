from rest_framework import serializers
from .models import BusinessTrip, Accommodation, DailyAllowance, Transportation, BusinessTripCertificate, \
    BusinessTripReport, PrimarySourceDocument, AdvancedCostReport


class DailyAllowanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyAllowance
        fields = ('id', 'business_trip', 'status', 'country_total_days', 'abroad_total_days', 'total_days', 'mrp',
                  'country_mrp', 'abroad_mrp', 'country_total_cost', 'abroad_total_cost', 'total_cost', 'debt')


# -------------


class AccommodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accommodation
        fields = ('id', 'business_trip', 'country', 'city', 'accommodation_address', 'arrival_date',
                  'arrival_time', 'departure_date', 'departure_time', 'payment_method', 'price')


# --------------


class TransportationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportation
        fields = ('id', 'business_trip', 'departure_city', 'departure_country', 'arrival_city',
                  'arrival_country', 'transportation_type', 'departure_date', 'departure_time', 'return_date',
                  'return_time', 'payment_method', 'price')


# ----------

class PrimarySourceDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimarySourceDocument
        fields = ('id', 'business_trip', 'file')

# ----------


class BusinessTripCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessTripCertificate
        fields = ('id', 'business_trip', 'file')


# ----------

class BusinessTripReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessTripReport
        fields = ('id', 'business_trip', 'file')


# ----------

class AdvancedCostReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvancedCostReport
        fields = ('id', 'business_trip', 'file')


# ----------

class BusinessTripIncompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessTrip
        fields = ('id', 'status', 'departure_date', 'return_date', 'departure_country', 'departure_city',
                  'destination_country', 'destination_city', 'total_cost', 'goal')


# ----------

class BusinessTripCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessTrip
        fields = ('id', 'status', 'departure_date', 'return_date', 'departure_city', 'destination_city', 'total_cost', 'goal')


# ----------

class BusinessTripCompleteSerializer(serializers.ModelSerializer):
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


# ----------

class UpdateStatusSerializer(serializers.Serializer):
    id = serializers.IntegerField()
