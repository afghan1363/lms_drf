from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=500, verbose_name='Название курса')
    preview = models.ImageField(verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание', **NULLABLE)


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    title = models.CharField(max_length=250, verbose_name='Тема урока')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    preview = models.ImageField(verbose_name='Превью', **NULLABLE)
    video = models.CharField(max_length=550, verbose_name='Ссылка на видео', **NULLABLE)
