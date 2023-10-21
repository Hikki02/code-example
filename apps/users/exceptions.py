from rest_framework.exceptions import APIException
from rest_framework import status


class BaseCustomException(APIException):
    detail_message = None
    detail_status_code = None

    def __init__(self, detail=None, status_code=None):
        if detail is None:
            detail = self.detail_message
        if status_code is None:
            status_code = self.detail_status_code
        self.detail = {"message": detail, "code": status_code}


class RegistrationFailed(BaseCustomException):
    detail_message = "User registration failed. Username or email already exists."
    detail_status_code = status.HTTP_400_BAD_REQUEST


class UserAlreadyExists(BaseCustomException):
    detail_message = "User with this email already exists."
    detail_status_code = status.HTTP_400_BAD_REQUEST


class UserNotFound(BaseCustomException):
    detail_message = "User with this email does not exist."
    detail_status_code = status.HTTP_404_NOT_FOUND


class WrongPassword(BaseCustomException):
    detail_message = "Incorrect password."
    detail_status_code = status.HTTP_400_BAD_REQUEST


class PasswordsDoNotMatch(BaseCustomException):
    detail_message = "Passwords do not match."
    detail_status_code = status.HTTP_400_BAD_REQUEST


class CustomPasswordResetResponse(BaseCustomException):
    detail_message = "Password reset link sent to your email address."
    detail_status_code = status.HTTP_200_OK

