from rest_framework.serializers import ModelSerializer, IntegerField, CharField, SerializerMethodField
from lms_app.models import Course, Lesson, Subscribe
from lms_app.validators import validate_dogs_data


class SubscribeSerializer(ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ('is_subscribe',)


class LessonSerializer(ModelSerializer):
    title = CharField(validators=(validate_dogs_data,))
    description = CharField(validators=(validate_dogs_data,))
    video = CharField(validators=(validate_dogs_data,))

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    title = CharField(validators=(validate_dogs_data,))
    description = CharField(validators=(validate_dogs_data,))
    count_lessons = IntegerField(source='lesson_set.all.count', read_only=True)  # поле количества уроков курса
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)  # поле вывода уроков
    is_subscribe = SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribe(self, course):
        user = self.context['request'].user
        subscription = Subscribe.objects.filter(course=course.pk, user=user.pk, is_subscribe=True)
        if subscription:
            return True
        return False
