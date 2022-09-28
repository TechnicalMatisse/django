from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('docad/',views.docad, name='docad'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('contagendamento/', views.contagendamento, name='contagendamento'),
    path('login/', views.login, name='login'),
    path('',views.dologin, name='dologin'),
    path('cadastro/', views.login, name='cadastro'),
    path('home/', views.login, name='home')
]
