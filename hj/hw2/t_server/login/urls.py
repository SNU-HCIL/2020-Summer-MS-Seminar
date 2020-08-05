from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="csrf"),
    path('signup/', views.signUp, name='signUp'),
    path('signin/', views.signIn, name="signIn"),
    path('status/<slug:user_id>/', views.status, name="status"),
    path('gameResult/', views.gameResult, name="gameResult"),
]