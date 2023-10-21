from rest_framework import serializers


class LegsSerializer(serializers.Serializer):
    origin = serializers.CharField()
    destination = serializers.CharField()
    date = serializers.DateField()


class SearchAirFlightsSerializer(serializers.Serializer):
    legs = LegsSerializer(many=True)
    adultCount = serializers.IntegerField(default=1)
    childCount = serializers.IntegerField(default=0)
    infantCount = serializers.IntegerField(default=0)
    cabin = serializers.CharField()


class FareFamiliesSerializer(serializers.Serializer):
    opt = serializers.CharField()


class FareRulesSerializer(serializers.Serializer):
    opt = serializers.CharField()


class BookFlightSerializer(serializers.Serializer):
    optionId = serializers.CharField()
    fareFamilyId = serializers.CharField()
    email = serializers.EmailField()
    countryCode = serializers.CharField()
    phone = serializers.CharField()
    client = serializers.CharField()
    passengers = serializers.ListField()


class IssueTicketsSerializer(serializers.Serializer):
    action = serializers.CharField()
    token = serializers.CharField()


class RefreshBookingStatusSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()


class SearchRailSerializer(serializers.Serializer):
    origin = serializers.CharField()
    destination = serializers.CharField()
    date = serializers.DateField()


class RailOptionDetailsSerializer(serializers.Serializer):
    optionId = serializers.CharField()
    wagonType = serializers.CharField()


class RailPrebookSerializer(serializers.Serializer):
    optionId = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    countryCode = serializers.CharField()
    seats = serializers.CharField()
    number = serializers.CharField()
    fareId = serializers.CharField()
    passengers = serializers.ListField()


class RailBookSerializer(serializers.Serializer):
    orderId = serializers.IntegerField()
