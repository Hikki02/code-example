from django.core.validators import FileExtensionValidator
from django.db import models
from utils.base.base_model import BaseModel

BUSINESS_TRIP_STATUSES = [
    ('awaiting_review', 'Заявка на проверке'),
    ('fix_required', 'Нужны правки по заявке'),
    ('soon', 'Скоро командировка'),
    ('in_trip', 'В командировке'),
    ('submitting_docs', 'Сдаю документы'),
    ('awaiting_docs_check', 'На проверке / доки'),
    ('need_docs_fix', 'Нужны правки / доки'),
    ('awaiting_advance_report', 'Ожидается авансовый отчет'),
    ('awaiting_ao_check', 'На проверке / АО'),
    ('need_ao_fix', 'Нужны правки / АО'),
    ('all_submitted', 'Все сдано'),
    ('cancellation', 'Отмена командировки')
]

DAILY_ALLOWANCE_STATUSES = [
    ('accrued', 'Начислены'),
    ('not_accrued', 'Не начислены')
]

SUPPORTED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'pdf', 'doc', 'docx', 'heic']


class BusinessTrip(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='business_trip', verbose_name='Пользователь', blank=True, null=True)
    departure_date = models.DateField(verbose_name='Дата отправления', null=True, blank=True)
    return_date = models.DateField(verbose_name='Дата возвращения', null=True, blank=True)
    duration = models.SmallIntegerField(verbose_name='Продолжительность', null=True, blank=True)
    departure_country = models.CharField(max_length=225, verbose_name='Страна отправления', null=True, blank=True)
    departure_city = models.CharField(max_length=225, verbose_name='Город отправления', null=True, blank=True)
    destination_country = models.CharField(max_length=225, verbose_name='Страна назначения', null=True, blank=True)
    destination_city = models.CharField(max_length=225, verbose_name='Город назначения', null=True, blank=True)
    total_cost = models.DecimalField(max_digits=25, decimal_places=2, verbose_name='Общая стоимость', blank=True, null=True)
    supervisor = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='supervised_business_trip', verbose_name='Руководитель', default=None, null=True, blank=True)
    assistant = models.ForeignKey('users.User', on_delete=models.PROTECT, related_name='assisted_business_trip', verbose_name='Ассистент', default=None, null=True)
    goal = models.TextField(verbose_name='Цель командировки', null=True, blank=True)
    debts = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Долги', null=True, blank=True, default=0)
    status = models.CharField(max_length=25, choices=BUSINESS_TRIP_STATUSES, verbose_name='Статус', default='awaiting_review', null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    daily_allowance_status = models.CharField(choices=DAILY_ALLOWANCE_STATUSES, verbose_name='Статус суточных', default='not_accrued', max_length=25, null=True, blank=True)

    class Meta:
        verbose_name = 'Заявка на командировку'
        verbose_name_plural = 'Заявки на командировку'

    def __str__(self):
        return f'Командировка #{self.id}'


class BusinessTripCertificate(BaseModel):
    business_trip = models.ForeignKey(
        'BusinessTrip', on_delete=models.CASCADE, related_name='business_trip_certificates',
        verbose_name='Заявка на командировку'
    )
    file = models.FileField(
        upload_to='business_trip_certificates/', null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=SUPPORTED_EXTENSIONS)],
        verbose_name='Командировочное удостоверение'
    )

    class Meta:
        verbose_name = 'Командировочное удостоверение'
        verbose_name_plural = 'Командировочные удостоверения'

    def __str__(self):
        return f'Командировочное удостоверение #{self.id} к командировке #{self.business_trip_id}'


class BusinessTripReport(BaseModel):
    business_trip = models.ForeignKey('BusinessTrip', on_delete=models.CASCADE,
                                      related_name='business_trip_reports', verbose_name='Заявка на командировку')
    file = models.FileField(
        upload_to='business_trip_reports/', null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=SUPPORTED_EXTENSIONS)],
        verbose_name='Отчет о командировке'
    )

    class Meta:
        verbose_name = 'Отчет о командировке'
        verbose_name_plural = 'Отчеты о командировке'

    def __str__(self):
        return f'Отчет о командировке #{self.id} к командировке #{self.business_trip_id}'


class AdvancedCostReport(BaseModel):
    business_trip = models.ForeignKey(
        'BusinessTrip', on_delete=models.CASCADE, related_name='advanced_cost_reports',
        verbose_name='Заявка на командировку', null=True
    )
    file = models.FileField(
        upload_to='advanced_cost_reports/', null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=SUPPORTED_EXTENSIONS)],
        verbose_name='Авансовый отчет'
    )

    class Meta:
        verbose_name = 'Авансовый отчет'
        verbose_name_plural = 'Авансовые отчеты'

    def __str__(self):
        return f'Авансовый отчет #{self.id} к командировке #{self.business_trip_id}'
