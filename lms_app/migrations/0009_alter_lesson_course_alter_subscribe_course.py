# Generated by Django 4.2.9 on 2024-01-24 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0008_alter_course_updated_at_alter_lesson_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='lms_app.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscribe', to='lms_app.course', verbose_name='Курс'),
        ),
    ]
