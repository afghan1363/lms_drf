# Generated by Django 5.0 on 2024-01-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0003_subscribe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='is_subscribe',
            field=models.BooleanField(default=False, verbose_name='Подписка'),
        ),
    ]