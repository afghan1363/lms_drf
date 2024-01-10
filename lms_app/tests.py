from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lms_app.models import Lesson, Course, Subscribe
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@mail.com', password='Test12345')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='testcourse',
            author=self.user
        )

        self.lesson = Lesson.objects.create(
            title="test",
            description="test description",
            video="https://www.youtube.com/",
            author=self.user,
            course=self.course
        )

    def test_lessons_list(self):
        """
        Тест вывод списка уроков
        """
        response = self.client.get(
            reverse('lms_app:lessons'),
        )
        # print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': self.lesson.pk, 'title': self.lesson.title, 'description': self.lesson.description,
                 'video': self.lesson.video, 'preview': self.lesson.preview, 'course': self.course.pk,
                 'author': self.user.pk}]}


        )

    def test_lesson_create(self):
        """
        Тест создания урока
        """
        data = {
            'course': self.course.pk,
            'title': 'test',
            'description': 'test description',
            'video': 'https://www.youtube.com/'
        }
        response = self.client.post(
            reverse('lms_app:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {'id': 2, 'title': 'test', 'description': 'test description', 'video': 'https://www.youtube.com/',
             'preview': None, 'course': self.course.pk, 'author': self.user.pk}

        )

    def test_lesson_retrieve(self):
        """
        Тест просмотр урока
        """
        response = self.client.get(
            reverse('lms_app:lesson_detail', kwargs={'pk': self.lesson.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': self.lesson.pk, 'title': self.lesson.title, 'description': self.lesson.description,
             'video': self.lesson.video, 'preview': self.lesson.preview, 'course': self.course.pk,
             'author': self.user.pk}

        )

    def test_lesson_update(self):
        """
        Тест редактирования урока
        """
        data = {
            "title": "test_updated",
            "description": "updated description",
            "video_url": "https://www.youtube.com/",
        }
        response = self.client.patch(
            reverse('lms_app:lesson_update', kwargs={'pk': self.lesson.pk}),
            data=data
        )
        print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'id': self.lesson.pk, 'title': 'test_updated',
             'description': 'updated description',
             'preview': None, 'video': 'https://www.youtube.com/', 'course': self.course.pk, 'author': self.user.pk}
        )

    def test_lesson_delete(self):
        """
        Тест удаления урока
        """

        response = self.client.delete(
            reverse('lms_app:lesson_delete', kwargs={'pk': self.lesson.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class SubscriptionTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@mail.com', password='Test12345')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title="test course",
            description="test description",
            author=self.user,
        )

        self.subscription = Subscribe.objects.create(
            course=self.course,
            user=self.user
        )

    def test_create_subscription(self):
        """
        Тест создания подписки
        """
        data = {
            'course': self.course.pk,
            'user': self.user.pk,
            'is_subscribe': True
        }
        response = self.client.post(
            reverse('lms_app:subscribe_create', kwargs={'pk': self.course.pk}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'is_subscribe': True},

        )

    def test_delete_subscription(self):
        """
        Тест удаления подписки
        """

        response = self.client.delete(
            reverse('lms_app:subscribe_delete', kwargs={'pk': self.subscription.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
