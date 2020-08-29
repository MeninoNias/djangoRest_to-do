from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Task
from core.modulos.task.serializers import TaskSerializer


class apiOverview(APIView):

    def get(self, request,  format=None):
        api_urls = {
            'List':'/task-list/',
            'Create': '/task-create/',
            'Detail View': '/task-detail/<str:pk>/',
            'Update': '/task-update/<str:pk>/',
            'Delete': '/task-delete/<str:pk>/',
        }

        return Response(api_urls)

class TaskList(APIView):

    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)