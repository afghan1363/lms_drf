from django.db import models
from users.models import User
from lms_app.models import Course, Lesson, NULLABLE
from datetime import date


def get_date_now():
    """Получение текущей даты"""
    return date.today()


class Payment(models.Model):
    BY_TRANSFER = 'trans'
    BY_CASH = 'cash'
    PAYMENT_METHOD = (
        (BY_TRANSFER, 'Перевод'),
        (BY_CASH, 'Наличные')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Плательщик', **NULLABLE)
    date_of_payment = models.DateField(verbose_name='Дата оплаты', default=get_date_now)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    paid_amount = models.IntegerField(verbose_name='Сумма оплаты', **NULLABLE)
    pay_type = models.CharField(choices=PAYMENT_METHOD, default=BY_TRANSFER, max_length=5,
                                verbose_name='способ оплаты')
    stripe_session = models.CharField(max_length=500, **NULLABLE, verbose_name='Session_ID in Stripe')
    status_paid = models.CharField(max_length=100, **NULLABLE, verbose_name='Статус оплаты')
    url = models.URLField(verbose_name='Ссылка для оплаты', **NULLABLE, max_length=500)

    def __str__(self):
        return f'{self.user}: {self.date_of_payment}'

    class Meta:
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'
