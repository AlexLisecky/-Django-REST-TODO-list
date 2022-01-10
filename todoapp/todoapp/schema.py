import graphene
from graphene_django import DjangoObjectType
from todo.models import Project, Todo
from Userapp.models import User


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(graphene.ObjectType):
    all_project = graphene.List(ProjectType)
    all_users = graphene.List(UserType)
    all_todo = graphene.List(TodoType)
    project_by_id = graphene.Field(ProjectType, id=graphene.Int(required=True))
    todo_by_id = graphene.Field(TodoType, id=graphene.Int(required=True))
    user_by_username = graphene.Field(UserType, username=graphene.String(required=True))
    all_data = graphene.List(ProjectType, id=graphene.Int(required=False))

    def resolve_all_project(root, info):
        return Project.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_todo(root, info):
        return Todo.objects.all()

    def resolve_project_by_id(root, info, id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            return None

    def resolve_todo_by_id(root, info, id):
        try:
            return Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return None

    def resolve_user_by_username(root, info, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def resolve_all_data(root, info, id=None):
        if id:
            query = Project.objects.filter(id=id)
        query = Project.objects.all()
        return query

# {
#   allData(id:1){
#     title
#     link
#     users {
#       username
#       lastName
#       firstName
#       todoSet{
#         id
#         text
#         }
#       }
#     }
#   }



schema = graphene.Schema(query=Query)
