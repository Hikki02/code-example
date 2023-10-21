from django.db import models

from utils.base.base_model import BaseModel
from django.core.validators import FileExtensionValidator

DAY_ALLOWANCE_STATUSES = [
    ('accrued', 'Начислено'),
    ('awaited', 'Ожидается')
]

SUPPORTED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'pdf', 'doc', 'docx', 'heic']


class DailyAllowance(BaseModel):
    business_trip = models.ForeignKey('BusinessTrip', on_delete=models.CASCADE,
                                               related_name='daily_allowance', verbose_name='Заявка на командировку')
    status = models.CharField(max_length=20, choices=DAY_ALLOWANCE_STATUSES, default='awaited', verbose_name='Статус')
    country_total_days = models.PositiveSmallIntegerField(verbose_name='Количество дней в стране')
    abroad_total_days = models.PositiveSmallIntegerField(verbose_name='Количество дней за границей')
    total_days = models.PositiveSmallIntegerField(verbose_name='Общее количество дней')
    mrp = models.DecimalField(max_digits=25, decimal_places=2, verbose_name='МРП')
    country_mrp = models.DecimalField(max_digits=25, decimal_places=2, verbose_name='МРП в стране')
    abroad_mrp = models.DecimalField(max_digits=25, decimal_places=2, verbose_name='МРП за границей')
    country_total_cost = models.DecimalField(max_digits=25, decimal_places=2, verbose_name='Итого в стране')
    abroad_total_cost = models.DecimalField(max_digits=25, decimal_places=2, verbose_name='Итого за границей')
    total_cost = models.DecimalField(max_digits=25, decimal_places=2, verbose_name='Общая сумма')
    debt = models.DecimalField(max_digits=25, decimal_places=2, verbose_name='Долги')

    class Meta:
        verbose_name = 'Суточные'
        verbose_name_plural = 'Суточные'

    def __str__(self):
        return f'Cуточные для командировки #{self.business_trip_id}'


class PrimarySourceDocument(BaseModel):
    business_trip = models.ForeignKey(
        'BusinessTrip', on_delete=models.CASCADE, related_name='primary_source_documents',
        verbose_name='Заявка на командировку'
    )
    file = models.FileField(
        upload_to='primary_source_documents/', null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=SUPPORTED_EXTENSIONS)],
        verbose_name='Документ первички'
    )

    class Meta:
        verbose_name = 'Первичка'
        verbose_name_plural = 'Документы первички'

    def __str__(self):
        return f'Первичка #{self.id} к командировке #{self.business_trip_id}'
