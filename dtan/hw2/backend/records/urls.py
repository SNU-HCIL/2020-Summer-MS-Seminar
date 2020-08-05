from django.urls import path
from . import views

app_name = 'records'
urlpatterns = [
    path('auth/', views.auth, name='auth'),
]