from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'AI'
urlpatterns = [
    path('', csrf_exempt(views.index), name='index'),
]