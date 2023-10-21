from rest_framework import serializers
from apps.users.models import User


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
        )


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'password2',
        )


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    company_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'user_role', 'company_id')

    def get_company_id(self, obj):
        try:
            company_id = obj.company.id
            return company_id
        except:
            return None

class UserFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['company', 'user_role', 'first_name', 'last_name', 'email', 'phone_number', 'password',
                  'inn', 'is_staff', 'is_superuser']

        read_only_fields = ['is_staff', 'is_superuser']
        extra_kwargs = {
            'password': {'required': True, 'write_only': True},
        }
