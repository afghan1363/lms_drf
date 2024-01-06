from django.urls import path
from payments.views import PaymentListAPIView

app_name = 'payments'
urlpatterns = [
    path('view/', PaymentListAPIView.as_view(), name='view_payment'),
]
