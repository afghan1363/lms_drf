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

    def get(self):
        if self.request.method.upper() == 'DELETE':
            self.permission_classes = (IsAuthenticated, Author,)
        elif self.request.method.upper() in ('PUT', 'PATCH', 'HEAD',):
            self.permission_classes = (IsAuthenticated, Moderator, Author,)
        elif self.request.method.upper() == 'POST':
            self.permission_classes = (IsAuthenticated, ~ Moderator,)
        return self.permission_classes

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.author = self.request.user
        new_course.save()



    # def get_permissions(self):
    #     if self.request.method.upper() in ['POST', 'DELETE']:
    #         self.permission_classes = (IsAuthenticated, Author,)
    #     elif self.request.method.upper() == 'CREATE':
    #         self.permission_classes = (IsAuthenticated, ~Moderator)
    #     return self.permission_classes


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
