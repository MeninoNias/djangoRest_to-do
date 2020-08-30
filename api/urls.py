from django.contrib import admin
from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from api.views import TaskViewSet, UserViewSet, api_root
from rest_framework import renderers

task_list = TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
task_detail = TaskViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
task_highlight = TaskViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', api_root),
    path('tasks/', task_list, name='tasks-list'),
    path('tasks/<str:pk>/', task_detail, name='task-detail'),
    path('tasks/<str:pk>/highlight/', task_highlight, name='task-highlight'),
    path('users/', user_list, name='users-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]