# Generated by Django 5.0 on 2024-01-15 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0011_alter_payment_status_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='stripe_session',
            field=models.CharField(blank=True, null=True, verbose_name='Session_ID in Stripe'),
        ),
    ]
