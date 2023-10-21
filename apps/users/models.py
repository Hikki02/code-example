from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

from apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    EMPLOYEE = 'employee'
    TRAVEL_AGENT = 'travel_agent'
    ACCOUNTANT = 'accountant'
    DEPARTMENT_HEAD = 'department_head'
    ADMIN = 'admin'

    USER_ROLE = (
        (EMPLOYEE, 'Работник'),
        (TRAVEL_AGENT, 'Тревел агент'),
        (ACCOUNTANT, 'Бухгалтер'),
        (DEPARTMENT_HEAD, 'Руководитель отдела'),
        (ADMIN, 'Администратор'),
    )

    username = models.CharField(max_length=225, verbose_name='Имя пользователя')
    company = models.ForeignKey('companies.Company', related_name='user_company', on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name='Компания')
    user_role = models.CharField(max_length=20, choices=USER_ROLE, default=EMPLOYEE, verbose_name='Роль пользователя')
    first_name = models.CharField(max_length=225, verbose_name='Имя')
    last_name = models.CharField(max_length=225, verbose_name='Фамилия')
    position = models.CharField(max_length=100, verbose_name='Должность', null=True)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    inn = models.IntegerField(null=True, verbose_name='ИНН')

    created_at = models.DateTimeField(verbose_name='Дата создания', default=timezone.now)

    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    is_superuser = models.BooleanField(default=False, verbose_name='Суперпользователь')
    is_active = models.BooleanField(default=False, verbose_name='Активен')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ()

    objects = UserManager()

    def __str__(self):
        return f'{self.id} -- {self.email}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
