from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    @classmethod
    def _validate(cls, **kwargs) -> None:
        for k, v in kwargs.items():
            if not k:
                raise ValueError('You have not entered %s' % v)

    def _create(self, email: str, password: str, **extra) -> None:
        self._validate(email=email, password=password)
        user = self.model(email=self.normalize_email(email), **extra)
        user.set_password(raw_password=password)
        user.save()
        return user

    def create_user(self,
                    email: str,
                    password: str,) -> None:
        user = self._create(email, password)
        return user

    def create_superuser(self,
                         email: str,
                         password: str) -> None:
        self._create(email, password, is_superuser=True, is_staff=True, is_active=True)
