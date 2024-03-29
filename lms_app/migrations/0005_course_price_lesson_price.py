# Generated by Django 5.0 on 2024-01-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0004_alter_subscribe_is_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100000.0, max_digits=9, verbose_name=' Стоимость курса'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5000.0, max_digits=9, verbose_name=' Стоимость урока'),
        ),
    ]
