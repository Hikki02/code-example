# Generated by Django 4.2.2 on 2023-08-08 15:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(max_length=100, verbose_name='Страна')),
                ('city', models.CharField(max_length=225, verbose_name='Город')),
                ('accommodation_address', models.CharField(max_length=225, verbose_name='Место пребывания')),
                ('arrival_date', models.DateField(verbose_name='Дата прибытия')),
                ('arrival_time', models.TimeField(verbose_name='Время прибытия')),
                ('departure_date', models.DateField(verbose_name='Дата отъезда')),
                ('departure_time', models.TimeField(verbose_name='Время отъезда')),
                ('payment_method', models.CharField(choices=[('cash', 'Наличные'), ('credit_card', 'Кредитная карта'), ('bank_transfer', 'Банковский перевод')], max_length=100, verbose_name='Способ оплаты')),
                ('price', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'verbose_name': 'Место пребывания',
                'verbose_name_plural': 'Места пребывания',
            },
        ),
        migrations.CreateModel(
            name='AdvancedCostReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='advanced_cost_reports/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf', 'doc', 'docx', 'heic'])], verbose_name='Авансовый отчет')),
            ],
            options={
                'verbose_name': 'Авансовый отчет',
                'verbose_name_plural': 'Авансовые отчеты',
            },
        ),
        migrations.CreateModel(
            name='BusinessTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_date', models.DateField(verbose_name='Дата отправления')),
                ('return_date', models.DateField(verbose_name='Дата возвращения')),
                ('duration', models.SmallIntegerField(verbose_name='Продолжительность')),
                ('departure_country', models.CharField(max_length=225, verbose_name='Страна отправления')),
                ('departure_city', models.CharField(max_length=225, verbose_name='Город отправления')),
                ('destination_country', models.CharField(max_length=225, verbose_name='Страна назначения')),
                ('destination_city', models.CharField(max_length=225, verbose_name='Город назначения')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=25, verbose_name='Общая стоимость')),
                ('goal', models.TextField(verbose_name='Цель командировки')),
                ('debts', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Долги')),
                ('status', models.CharField(choices=[('soon', 'Скоро командировка'), ('in_trip', 'В командировке'), ('submitting_documents', 'Сдаю документы'), ('awaiting_check', 'На проверке'), ('need_fix', 'Нужны правки'), ('awaiting_advance_report', 'Ожидается авансовый отчет'), ('all_submitted', 'Все сдано'), ('cancel', 'Отмена командировки')], default='soon', max_length=25, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заявка на командировку',
                'verbose_name_plural': 'Заявки на командировку',
            },
        ),
        migrations.CreateModel(
            name='TransportationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportation_type', models.CharField(choices=[('airplane', 'Самолет'), ('train', 'Поезд'), ('bus', 'Автобус'), ('car', 'Автомобиль'), ('other', 'Другое')], max_length=100, verbose_name='Тип транспорта')),
                ('transportation_icon', models.ImageField(upload_to='', verbose_name='Иконка транспорта')),
            ],
            options={
                'verbose_name': 'Тип транспорта',
                'verbose_name_plural': 'Типы транспорта',
            },
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('departure_city', models.CharField(max_length=225, verbose_name='Город отправления')),
                ('departure_country', models.CharField(max_length=225, verbose_name='Страна отправления')),
                ('arrival_city', models.CharField(max_length=225, verbose_name='Город прибытия')),
                ('arrival_country', models.CharField(max_length=225, verbose_name='Страна прибытия')),
                ('departure_date', models.DateField(verbose_name='Дата отправления')),
                ('departure_time', models.TimeField(verbose_name='Время отправления')),
                ('return_date', models.DateField(verbose_name='Дата возвращения')),
                ('return_time', models.TimeField(verbose_name='Время возвращения')),
                ('payment_method', models.CharField(choices=[('cash', 'Наличные'), ('credit_card', 'Кредитная карта'), ('bank_transfer', 'Банковский перевод')], max_length=100, verbose_name='Способ оплаты')),
                ('price', models.DecimalField(decimal_places=2, max_digits=25, verbose_name='Цена')),
                ('business_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transportations', to='business_trips.businesstrip', verbose_name='Заявка на командировку')),
                ('transportation_type', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='business_trips.transportationtype')),
            ],
            options={
                'verbose_name': 'Транспорт',
                'verbose_name_plural': 'Транспорт',
            },
        ),
        migrations.CreateModel(
            name='PrimarySourceDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='primary_source_documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf', 'doc', 'docx', 'heic'])], verbose_name='Документ первички')),
                ('business_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_source_documents', to='business_trips.businesstrip', verbose_name='Заявка на командировку')),
            ],
            options={
                'verbose_name': 'Первичка',
                'verbose_name_plural': 'Документы первички',
            },
        ),
        migrations.CreateModel(
            name='DailyAllowance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('accrued', 'Начислено'), ('awaited', 'Ожидается')], default='awaited', max_length=20, verbose_name='Статус')),
                ('country_total_days', models.PositiveSmallIntegerField(verbose_name='Количество дней в стране')),
                ('abroad_total_days', models.PositiveSmallIntegerField(verbose_name='Количество дней за границей')),
                ('total_days', models.PositiveSmallIntegerField(verbose_name='Общее количество дней')),
                ('mrp', models.DecimalField(decimal_places=2, max_digits=25, verbose_name='МРП')),
                ('country_mrp', models.DecimalField(decimal_places=2, max_digits=25, verbose_name='МРП в стране')),
                ('abroad_mrp', models.DecimalField(decimal_places=2, max_digits=25, verbose_name='МРП за границей')),
                ('country_total_cost', models.DecimalField(decimal_places=2, max_digits=25, verbose_name='Итого в стране')),
                ('abroad_total_cost', models.DecimalField(decimal_places=2, max_digits=25, verbose_name='Итого за границей')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=25, verbose_name='Общая сумма')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=25, verbose_name='Долги')),
                ('business_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_allowance', to='business_trips.businesstrip', verbose_name='Заявка на командировку')),
            ],
            options={
                'verbose_name': 'Суточные',
                'verbose_name_plural': 'Суточные',
            },
        ),
        migrations.CreateModel(
            name='BusinessTripReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='business_trip_reports/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf', 'doc', 'docx', 'heic'])], verbose_name='Отчет о командировке')),
                ('business_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_trip_reports', to='business_trips.businesstrip', verbose_name='Заявка на командировку')),
            ],
            options={
                'verbose_name': 'Отчет о командировке',
                'verbose_name_plural': 'Отчеты о командировке',
            },
        ),
        migrations.CreateModel(
            name='BusinessTripCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='business_trip_certificates/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf', 'doc', 'docx', 'heic'])], verbose_name='Командировочное удостоверение')),
                ('business_trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_trip_certificates', to='business_trips.businesstrip', verbose_name='Заявка на командировку')),
            ],
            options={
                'verbose_name': 'Командировочное удостоверение',
                'verbose_name_plural': 'Командировочные удостоверения',
            },
        ),
    ]
