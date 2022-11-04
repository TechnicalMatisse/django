from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name ='home'),
    path('homepage/', views.homepage, name ='homepage'),
    path('cadastro/', views.cadastro, name ='cadastro'),
    path('docad/', views.docad, name ='docad'),
    path('agendamento/', views.agendamento, name ='agendamento'),
    path('login/', views.login, name ='login'),
    path('dologin/',views.dologin, name ='dologin'),
    path('cadastro/', views.login, name ='cadastro'),
    path('erro/', views.erro, name ='erro'),
    path('errorlog/', views.errorlog, name ='errorlog' ),
    path('errorlogout/', views.errorlogout, name ='errorlogout' ),
    path('sucesso/', views.sucesso, name ='sucesso'),
    path('sucessolog/', views.sucessolog, name ='sucessolog'),
    path('sucessologout/', views.sucessologout, name ='sucessologout'),
    path('logout/', views.logout, name ='logout'),
    path('perfil/', views.profile, name ='perfil'),
    path('doupdate/', views.do_update, name ='doupdate'),
    path('agendamento/<int:id>/editar',views.edit_coment, name='edit_coment'),
]
