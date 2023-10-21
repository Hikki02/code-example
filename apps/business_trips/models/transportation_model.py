from django.db import models

from utils.base.base_model import BaseModel

TRANSPORT_TYPES = [
    ('airplane', 'Самолет'),
    ('train', 'Поезд'),
    ('bus', 'Автобус'),
    ('car', 'Автомобиль'),
    ('other', 'Другое'),
]

PAYMENT_METHODS = [
    ('cash', 'Наличные'),
    ('credit_card', 'Кредитная карта'),
    ('bank_transfer', 'Банковский перевод'),  # уточнить какие методы оплаты должны быть доступны пользователю
]


class Transportation(BaseModel):
    business_trip = models.ForeignKey('BusinessTrip', on_delete=models.CASCADE, related_name='transportations',
                                      verbose_name='Заявка на командировку')
    departure_city = models.CharField(max_length=225, verbose_name='Город отправления')
    departure_country = models.CharField(max_length=225, verbose_name='Страна отправления')
    arrival_city = models.CharField(max_length=225, verbose_name='Город прибытия')
    arrival_country = models.CharField(max_length=225, verbose_name='Страна прибытия')
    transportation_type = models.CharField(max_length=100, verbose_name='Тип транспорта', choices=TRANSPORT_TYPES)
    departure_date = models.DateField(verbose_name='Дата отправления')
    departure_time = models.TimeField(verbose_name='Время отправления')
    return_date = models.DateField(verbose_name='Дата возвращения')
    return_time = models.TimeField(verbose_name='Время возвращения')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHODS, verbose_name='Способ оплаты')
    price = models.DecimalField(max_digits=25, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспорт'

    def __str__(self):
        return f'Транспорт для командировки #{self.business_trip_id}'
