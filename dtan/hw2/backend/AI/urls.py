from django.urls import path
from . import views

app_name = 'AI'
urlpatterns = [
    path('', views.index, name='index'),
]