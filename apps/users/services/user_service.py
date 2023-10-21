from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from utils.base.base_service import BaseService

User = get_user_model()


class UserService(BaseService):
    @staticmethod
    def register_user(email, password):
        try:
            user = User.objects.create_user(email=email, password=password)
            return user
        except IntegrityError:
            return None

    @staticmethod
    def generate_uidb64_and_token(user: User):
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        return uidb64, token

    @staticmethod
    def _validate_token(uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

            if default_token_generator.check_token(user, token):
                return user

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            pass

        return None

    @staticmethod
    def confirm_email(uidb64, token):
        user = UserService._validate_token(uidb64, token)

        if user:
            user.status = User.VERIFIED
            user.save()
        return user

    @staticmethod
    def reset_password(uidb64, token, new_password):
        user = UserService._validate_token(uidb64, token)

        if user:
            user.set_password(new_password)
            user.save()
        return user
