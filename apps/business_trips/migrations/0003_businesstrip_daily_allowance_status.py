# Generated by Django 4.1.10 on 2023-10-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_trips', '0002_accommodation_business_trip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesstrip',
            name='daily_allowance_status',
            field=models.CharField(blank=True, choices=[('accrued', 'Начислены'), ('not_accrued', 'Не начислены')], default='not_accrued', max_length=25, null=True, verbose_name='Статус суточных'),
        ),
    ]
