from django.contrib.auth.models import AbstractUser
from django.db import models
from lms_app.models import NULLABLE


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=30, verbose_name='Телефон', **NULLABLE)
    city = models.CharField(max_length=200, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    is_moderator = models.BooleanField(default=False, verbose_name='Модератор')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
