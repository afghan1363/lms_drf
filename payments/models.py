from django.db import models
from users.models import User
from lms_app.models import Course, Lesson, NULLABLE


class Payment(models.Model):
    BY_TRANSFER = 'trans'
    BY_CASH = 'cash'
    PAYMENT_METHOD = (
        (BY_TRANSFER, 'Перевод'),
        (BY_CASH, 'Наличные')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Плательщик')
    date_of_payment = models.DateField(verbose_name='Дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    paid_amount = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма оплаты')
    pay_type = models.CharField(choices=PAYMENT_METHOD, default=BY_TRANSFER, max_length=10,
                                verbose_name='способ оплаты')
