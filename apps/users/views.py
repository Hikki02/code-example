import logging

from drf_yasg.utils import swagger_auto_schema

from utils.swagger.parameters import token, uidb64

logger = logging.getLogger(__name__)

from django.contrib.auth.hashers import check_password
from rest_framework import permissions, status, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from apps.users.models import User
from apps.users.serializers import (
    UserLoginSerializer,
    UserRegistrationSerializer,
    UserEmailSerializer,
    UserFullSerializer,
)
from apps.users.utils import generateAuthInfo
from apps.users.exceptions import (
    RegistrationFailed,
    UserNotFound,
    WrongPassword,
    UserAlreadyExists,
)
from apps.users.services.email_service import EmailService
from apps.users.services.user_service import UserService


class UserViewSet(
    GenericViewSet
):
    user_service = UserService
    email_service = EmailService
    swagger_tags = ['User']

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.action == 'registration':
            return UserRegistrationSerializer
        if self.action == 'login':
            return UserLoginSerializer
        # Выдает странные ошибки
        # if self.action in ['check_user_email', 'password_reset_request']:
        #     return UserEmailSerializer
        return UserFullSerializer

    @action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny])
    def registration(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.user_service.register_user(
            email=serializer.validated_data.get('email'),
            password=serializer.validated_data.get('password')
        )
        if user:
            uidb64, token = self.user_service.generate_uidb64_and_token(user)
            self.email_service.send_registration_confirmation_email(user, uidb64, token)
            return Response({"message": "Email activation link sent successfully", "status": status.HTTP_200_OK})
        raise RegistrationFailed()

    @action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny])
    def login(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()
        if not user:
            raise AuthenticationFailed()
        elif not check_password(password, user.password):
            raise WrongPassword()

        serializer = UserLoginSerializer(user, context={'request': request})
        return Response({"status": status.HTTP_200_OK, "message": "Login successful",
                         "data": generateAuthInfo(user, serializer.data)})

    @action(methods=['get'], detail=False, permission_classes=[permissions.AllowAny])
    def check_user_email(self, request, *args, **kwargs):
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            raise UserAlreadyExists()
        return Response({"status": status.HTTP_200_OK, "message": "Email is available"})

    @action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny])
    def password_reset_request(self, request, *args, **kwargs):
        user_service = self.user_service
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()

        if not user:
            raise UserNotFound()

        uidb64, token = user_service.generate_uidb64_and_token(user)
        EmailService.send_password_reset_email(user=user, uidb64=uidb64, token=token)

        return Response({"message": "Password reset link sent to your email address.", "status": status.HTTP_200_OK})

    @swagger_auto_schema(manual_parameters=[token, uidb64])
    @action(methods=['get'], detail=False, permission_classes=[permissions.AllowAny])
    def confirm_email(self, request, *args, **kwargs):
        user_service = self.user_service
        uidb64 = request.data.get('uidb64')
        token = request.data.get('token')
        user = user_service.confirm_email(uidb64, token)

        if user:
            return Response({"status": status.HTTP_200_OK, "message": "Email confirmed successfully"})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Email confirmation failed"})

    @action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny])
    def password_reset(self, request, *args, **kwargs):
        user_service = self.user_service
        uidb64 = request.query_params.get('uidb64')
        token = request.query_params.get('token')
        new_password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if new_password != confirm_password:
            return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Passwords do not match"})

        user = user_service.reset_password(uidb64, token, new_password)

        if user:
            return Response({"status": status.HTTP_200_OK, "message": "Password reset successfully"})
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Password reset failed"})

    @action(methods=['get'], detail=True, permission_classes=[permissions.IsAuthenticated])
    def get_user_profile(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True, permission_classes=[permissions.IsAuthenticated])
    def update_profile(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)

        if serializer.is_valid() and user.status == User.VERIFIED:
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "message": "Profile updated successfully",
                             "user_profile": self.get_user_profile(request, *args, **kwargs).data})

        print(serializer.errors)
        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": "Profile update failed"})

