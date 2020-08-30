from django.shortcuts import render
from django.http import Http404

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from core.models import Task
from core.modulos.task.serializers import TaskSerializer
from core.modulos.user.serializers import UserSerializer

from core.modulos.task.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

#API ROOT
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-list', request=request, format=format),
        'tasks': reverse('tasks-list', request=request, format=format)
    })

# class TaskList(APIView):

#     def get(self, request, format=None):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskList(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class TaskDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         task = self.get_object(pk)
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class TaskDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

class TaskHighlight(GenericAPIView):
    queryset = Task.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        return Response(task.highlighted)


#USER
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer