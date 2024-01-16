from django.urls import path
from payments.views import (PaymentListAPIView, PaymentCourseCreateAPIView, PaymentLessonCreateAPIView,
                            PaymentRetrieveAPIView)

app_name = 'payments'
urlpatterns = [
    path('view/', PaymentListAPIView.as_view(), name='view_payment'),
    path('course/<int:pk>/create/', PaymentCourseCreateAPIView.as_view(), name='course_payment'),
    path('lesson/<int:pk>/create/', PaymentLessonCreateAPIView.as_view(), name='lesson_payment'),
    path('course/<int:pk>/retrieve/', PaymentRetrieveAPIView.as_view(), name='course_retrieve'),
    path('lesson/<int:pk>/retrieve/', PaymentRetrieveAPIView.as_view(), name='course_retrieve'),
]
