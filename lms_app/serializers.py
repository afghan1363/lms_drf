from rest_framework.serializers import ModelSerializer, SerializerMethodField
from lms_app.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    # count_lessons = SerializerMethodField()
    #
    # def get_count_lessons(self, course):
    #     return course.

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
