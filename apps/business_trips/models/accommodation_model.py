from django.db import models

from utils.base.base_model import BaseModel

PAYMENT_METHODS = [
    ('cash', 'Наличные'),
    ('credit_card', 'Кредитная карта'),
    ('bank_transfer', 'Банковский перевод'),  # уточнить какие методы оплаты должны быть доступны пользователю
]


class Accommodation(BaseModel):
    business_trip = models.ForeignKey('BusinessTrip', on_delete=models.CASCADE,
                                      related_name='accommodations', verbose_name='Заявка на командировку', null=True)
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=225, verbose_name='Город')
    accommodation_address = models.CharField(max_length=225, verbose_name='Место пребывания')
    arrival_date = models.DateField(verbose_name='Дата прибытия')
    arrival_time = models.TimeField(verbose_name='Время прибытия')
    departure_date = models.DateField(verbose_name='Дата отъезда')
    departure_time = models.TimeField(verbose_name='Время отъезда')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHODS, verbose_name='Способ оплаты')
    price = models.DecimalField(max_digits=25, decimal_places=2)

    class Meta:
        verbose_name = 'Место пребывания'
        verbose_name_plural = 'Места пребывания'

    def __str__(self):
        return f'Cуточные для командировки #{self.business_trip_id}'
