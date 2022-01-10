from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, StringRelatedField
from .models import Project, Todo
from Userapp.serializer import UserModelSerializer


class ProjectSerializer(ModelSerializer):
    #users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoSerializer(ModelSerializer):
    #project_name = ProjectSerializer()
    #user = StringRelatedField()

    class Meta:
        model = Todo
        fields = '__all__'
