from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('agendamento/', views.agendamento, name='a'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.login, name='cadatro')
]

