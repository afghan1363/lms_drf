from rest_framework.routers import DefaultRouter
from lms_app.views import (CourseViewSet, LessonCreateView, LessonListView, LessonRetrieveView, LessonUpdateView,
                           LessonDestroyView, SubscribeCreateAPIView, SubscribeUpdateAPIView, SubscribeDeleteAPIView)
from django.urls import path
from lms_app.apps import LmsAppConfig

app_name = LmsAppConfig.name

router = DefaultRouter()
router.register(prefix=r'courses', viewset=CourseViewSet, basename='courses')
urlpatterns = [
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lessons/', LessonListView.as_view(), name='lessons'),
    path('lesson/<int:pk>/', LessonRetrieveView.as_view(), name='lesson_detail'),
    path('lesson/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', LessonDestroyView.as_view(), name='lesson_delete'),
    path('course/<int:pk>/subscribe/', SubscribeCreateAPIView.as_view(), name='subscribe_create'),
    path('course/subscribe/update/<int:pk>/', SubscribeUpdateAPIView.as_view(), name='subscribe_update'),
    path('course/subscribe/delete/<int:pk>/', SubscribeDeleteAPIView.as_view(), name='subscribe_delete'),
] + router.urls
