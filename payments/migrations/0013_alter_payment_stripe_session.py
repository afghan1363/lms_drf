# Generated by Django 5.0 on 2024-01-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0012_alter_payment_stripe_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='stripe_session',
            field=models.TextField(blank=True, null=True, verbose_name='Session_ID in Stripe'),
        ),
    ]
