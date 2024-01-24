from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from lms_app.models import Course, Lesson, Subscribe
from lms_app.serializers import CourseSerializer, LessonSerializer, SubscribeSerializer
from lms_app.permissions import Author, Moderator
from rest_framework.permissions import IsAuthenticated
from lms_app.paginators import CoursesPaginator, LessonsPaginator
from lms_app.tasks import send_updates


# Create your views here.
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursesPaginator

    # permission_classes = (IsAuthenticated,)

    def get_permissions(self):
        permission_classes = (IsAuthenticated, Author)
        if self.action == 'create':
            permission_classes = (IsAuthenticated, ~Moderator)
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = (IsAuthenticated, Moderator | Author)
        elif self.action == 'update' or self.action == 'destroy':
            permission_classes = (IsAuthenticated, Author | Moderator)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.author = self.request.user
        new_course.save()

    def perform_update(self, serializer):
        course = serializer.save()
        send_updates.delay(course.pk)


class LessonCreateView(CreateAPIView):
    """Создание урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, ~Moderator,)

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.author = self.request.user
        new_lesson.save()
        send_updates.delay(new_lesson.course.pk)


class LessonListView(ListAPIView):
    """Просмотр всех уроков"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LessonsPaginator


class LessonRetrieveView(RetrieveAPIView):
    """Просмотр одного урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, Author | Moderator,)


class LessonUpdateView(UpdateAPIView):
    """Редактирование урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, Author | Moderator,)

    def perform_update(self, serializer):
        lesson = serializer.save()
        send_updates.delay(lesson.course.pk)


class LessonDestroyView(DestroyAPIView):
    """Удаление урока"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, Author,)


class SubscribeCreateAPIView(CreateAPIView):
    """Создание подписки на курс"""
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        new_subscribe = serializer.save()
        new_subscribe.user = self.request.user
        new_subscribe.course = Course.objects.get(pk=self.kwargs.get('pk'))
        new_subscribe.is_subscribe = True
        new_subscribe.save()


class SubscribeUpdateAPIView(UpdateAPIView):
    """Редактирование подписки на курс"""
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = (IsAuthenticated, Author | Moderator,)


class SubscribeDeleteAPIView(DestroyAPIView):
    """Удаление подписки на курс"""
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = (IsAuthenticated,)
