from django.urls import path
from users.views import UserViewSet

app_name = 'users'

urlpatterns = [
    path('update/<int:pk>/', UserViewSet.as_view(), name='user_update'),
]
