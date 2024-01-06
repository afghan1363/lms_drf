from rest_framework.serializers import ModelSerializer
from payments.serializers import PaymentSerializer
from users.models import User


class UserSerializer(ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'payments')
