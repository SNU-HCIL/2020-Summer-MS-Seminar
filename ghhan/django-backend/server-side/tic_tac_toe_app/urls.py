from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log_in/', views.logIn, name='log-in'),
    path('log_out/', views.logOut, name='log-out'),
    path('save/', views.SaveGameResult, name='save'),
    path('ai_action/', views.RetrieveAIAction, name='ai-action')
]