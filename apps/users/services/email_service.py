import os
from django.core.mail import send_mail
from utils.base.base_service import BaseService


class EmailService(BaseService):
    BASE_URL = os.getenv('BASE_URL')

    @staticmethod
    def send_email(subject, user, email_data, from_email=None):
        """
        Send an email to a user.

        Args:
            subject (str): The email subject.
            user (User): The user to whom the email will be sent.
            email_data (dict): A dictionary containing email content.
            from_email (str, optional): The sender's email address. Defaults to None.
        """
        if not from_email:
            from_email = os.getenv('EMAIL_FROM')

        recipient_list = [user.email]

        try:
            send_mail(
                subject,
                email_data,
                from_email,
                recipient_list,
                fail_silently=False,
            )
            print(f"Email sent successfully to {user.email}: {subject}")
        except Exception as e:
            print(f"Email sending failed to {user.email}: {subject}. Error: {str(e)}")

    @staticmethod
    def send_registration_confirmation_email(user, uidb64, token):
        subject = "Подтверждение почты"
        email_data = f'Для подтверждения почты перейдите по ссылке:\n{EmailService.BASE_URL}registration/confirm?uidb64={uidb64}&token={token}'
        EmailService.send_email(subject, user, email_data)

    @staticmethod
    def send_password_reset_email(user, uidb64, token):
        subject = "Сброс пароля"
        email_data = f"Для сброса пароля перейдите по ссылке: \n{EmailService.BASE_URL}reset_password_request/new?uidb64={uidb64}&token={token}"
        EmailService.send_email(subject, user, email_data)
