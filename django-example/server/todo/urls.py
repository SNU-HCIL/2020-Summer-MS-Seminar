from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks', views.Tasks.as_view(), name='todo-tasks'),
]

