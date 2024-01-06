from django.urls import path
from users.views import UserCreateAPIView, UserRetrieveAPIView

app_name = 'users'

urlpatterns = [
    path('detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserCreateAPIView.as_view(), name='user_update'),
]
