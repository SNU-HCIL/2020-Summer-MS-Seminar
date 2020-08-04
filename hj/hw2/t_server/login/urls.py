from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="csrf"),
    path('signup/', views.signUp, name='signUp'),
    path('signin/', views.signIn, name="signIn"),
]