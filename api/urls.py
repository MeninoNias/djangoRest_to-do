from django.contrib import admin
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('', views.apiOverview.as_view(), name='api-overview'),
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<str:pk>/', views.TaskDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)