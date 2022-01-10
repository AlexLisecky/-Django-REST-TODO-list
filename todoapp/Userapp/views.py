from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import User
from .serializer import UserModelSerializer, UserModelSerializerV2


class UserViewCustomSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserModelSerializerV2
        return UserModelSerializer

# class UserViewSet(ViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#
#     def list(self, request):
#         users = User.objects.all()
#         serializer = UserModelSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserModelSerializer(user)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserModelSerializer(request.data)
#         user.username = serializer.data['username']
#         user.last_name = serializer.data['last_name']
#         user.email = serializer.data['email']
#         user.first_name = serializer.data['first_name']
#         user.save()
#         return Response(serializer.data)
#
#     def partial_update(self, request, pk=None):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserModelSerializer(request.data)
#         user.username = serializer.data['username']
#         user.last_name = serializer.data['last_name']
#         user.email = serializer.data['email']
#         user.first_name = serializer.data['first_name']
#         user.save()
#
#         return Response(serializer.data)
