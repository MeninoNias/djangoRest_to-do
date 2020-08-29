from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('', views.apiOverview.as_view(), name='api-overview'),
    path('tasks/', views.TaskList.as_view(), name='task-list'),

]
