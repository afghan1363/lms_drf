from rest_framework.routers import DefaultRouter
from lms_app.views import (CourseViewSet, LessonCreateView, LessonListView, LessonRetrieveView, LessonUpdateView,
                           LessonDestroyView)
from django.urls import path
from lms_app.apps import LmsAppConfig

app_name = LmsAppConfig.name

router = DefaultRouter()
router.register(prefix=r'course', viewset=CourseViewSet, basename='course')
urlpatterns = [
    path('lesson/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/', LessonListView.as_view(), name='lessons'),
    path('lesson/<int:pk>/', LessonRetrieveView.as_view(), name='lesson_detail'),
    path('lesson/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete', LessonDestroyView.as_view(), name='lesson_delete'),
] + router.urls
