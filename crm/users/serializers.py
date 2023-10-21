from rest_framework import serializers
from apps.users.models import User


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'position', 'user_role', 'email', 'phone_number', 'password')


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    position = serializers.CharField(required=False)
    user_role = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'position', 'user_role', 'email', 'phone_number')


class EmployeeListSerializer(serializers.ModelSerializer):
    user_role = serializers.CharField(source='get_user_role_display', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'user_role', 'email')
