from rest_framework.generics import ListAPIView
from payments.serializers import PaymentSerializer
from payments.models import Payment
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter


class PaymentListAPIView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('paid_course', 'paid_lesson', 'pay_type')
    ordering_fields = ('date_of_payment',)
