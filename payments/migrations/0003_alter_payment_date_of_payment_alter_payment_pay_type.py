# Generated by Django 5.0 on 2024-01-06 01:40

import payments.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date_of_payment',
            field=models.DateField(default=payments.models.get_date_now, verbose_name='Дата оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pay_type',
            field=models.CharField(choices=[('trans', 'Перевод'), ('cash', 'Наличные')], default='trans', max_length=5, verbose_name='способ оплаты'),
        ),
    ]