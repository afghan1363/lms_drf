from datetime import date
from django.db import models
from django.conf import settings


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название курса')
    preview = models.ImageField(verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор курса',
                               **NULLABLE)
    price = models.PositiveIntegerField(default=1000000, verbose_name=' Стоимость курса')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Course - {self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='lesson')
    title = models.CharField(max_length=250, verbose_name='Тема урока')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(verbose_name='Превью', **NULLABLE)
    video = models.CharField(max_length=550, verbose_name='Ссылка на видео', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор урока',
                               **NULLABLE)
    price = models.PositiveIntegerField(default=500000, verbose_name=' Стоимость урока')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Lesson - {self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscribe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Подписчик', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE,
                               related_name='subscribe')
    is_subscribe = models.BooleanField(verbose_name='Подписка', default=False)
