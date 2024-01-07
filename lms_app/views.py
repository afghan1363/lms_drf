from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from lms_app.models import Course, Lesson
from lms_app.serializers import CourseSerializer, LessonSerializer
from lms_app.permissions import Author, Moderator
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, ~Moderator]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, Moderator | Author]
        elif self.action == 'update' or self.action == 'destroy':
            permission_classes = [IsAuthenticated, Author]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.author = self.request.user
        new_course.save()


class LessonCreateView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~Moderator,)

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.author = self.request.user
        new_lesson.save()


class LessonListView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,)


class LessonRetrieveView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, Author | Moderator,)


class LessonUpdateView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, Author | Moderator,)


class LessonDestroyView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, Author,)
