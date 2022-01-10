from django_filters.rest_framework import FilterSet
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as filters
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.serializers import StringRelatedField
from rest_framework.response import Response
from rest_framework import mixins, viewsets, permissions

from .models import Project, Todo
from .serializer import ProjectSerializer, TodoSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectFilter(filters.FilterSet):
    # обязательно указывать имя как в модели title = models.CharField(max_length=64, verbose_name='Проект')
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['title']


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter
    #permission_classes = [permissions.IsAuthenticated]


class TodoFilters(filters.FilterSet):
    project_name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Todo
        fields = ['project_name']


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoModelCustomSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                         mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_class = TodoFilters
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
