# Generated by Django 5.0 on 2024-01-06 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_payment_date_of_payment_alter_payment_pay_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Платёж', 'verbose_name_plural': 'Платежи'},
        ),
    ]
