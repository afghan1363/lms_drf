from rest_framework.serializers import ModelSerializer, SerializerMethodField, IntegerField
from lms_app.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    count_lessons = IntegerField(source='lesson_set.all.count')  # поле количества уроков курса

    class Meta:
        model = Course
        fields = '__all__'
