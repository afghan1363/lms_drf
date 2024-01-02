from rest_framework.generics import CreateAPIView
from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
