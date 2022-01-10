import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ProjectModelViewSet, TodoModelCustomSet
from .models import Project, Todo
from Userapp.models import User


class TestProjectViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/project/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.get('/api/todo/')
        view = TodoModelCustomSet.as_view({'get': 'list'})
        response = view(request)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/project/', {"count": 1, "next": None, "previous": None,
                                                 "results": [
                                                     {
                                                         "id": 4,
                                                         "text": "brief",
                                                         "created": "2021-11-18T20:48:20.622450Z",
                                                         "updated": "2021-11-18T20:48:20.622450Z",
                                                         "is_active": True,
                                                         "project_name": 1,
                                                         "user": 8
                                                     }
                                                 ]}, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestProjectApiClient(APIClient):

    def test_get_detail(self):
        project = Project.objects.create({
            "count": 6,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "title": "web-site",
                    "link": "link",
                    "users": []
                }]})
        client = APIClient()
        response = client.get(f'/api/project/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        author = Project.objects.create({
            "count": 6,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "title": "web-site",
                    "link": "link",
                    "users": []
                }]})
        client = APIClient()
        response = client.put(f'/api/project/{author.id}/', {
            "count": 6,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "title": "web-site",
                    "link": "link",
                    "users": []
                }]})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestBookViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        todo = Todo.objects.create({
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 4,
                    "text": "brief",
                    "created": "2021-11-18T20:48:20.622450Z",
                    "updated": "2021-11-18T20:48:20.622450Z",
                    "is_active": True,
                    "project_name": 1,
                    "user": 8
                }
            ]
        })
        project = Project.objects.create({
            "count": 6,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "title": "web-site",
                    "link": "link",
                    "users": []
                }]}, todo=todo)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/project/{project.id}/',
                                   {
                                       "count": 6,
                                       "next": None,
                                       "previous": None,
                                       "results": [
                                           {
                                               "id": 1,
                                               "title": "web-site",
                                               "link": "link",
                                               "users": []
                                           }],'author': project.todo.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book = project.objects.get(id=project.id)
        self.assertEqual(book.name, 'Руслан и Людмила')

# модуль json нужен для чтения содержимого ответа от сервера;
# TestCase — базовый класс для создания Django-теста;
# status содержит константы для ответов сервера;
# APIRequestFactory — фабрика для создания запросов;
# force_authenticate — функция для авторизации пользователя;
# APIClient — клиент для удобной отправки REST-запросов;
# APISimpleTestCase — класс для создания простых test cases;
# APIITestCase — класс для создания test cases для REST API;
# Mixer — библиотека для генерации тестовых данных;
# User — модель пользователя;
# AuthorViewSet — view set для работы с моделью Author;
# Author, Book — модели автора и книги.
