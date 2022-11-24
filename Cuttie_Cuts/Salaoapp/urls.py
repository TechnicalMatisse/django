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
    path('agend_delete/<int:id>/deletar',views.agend_delete, name='agend_delete'),
]



""" 

def agendamento(request):
    data = {}
    data['servicoform'] = Servicos.objects.all()
    if request.method == 'POST':
        c = Agendamento(usuario=Usuario.objects.get(id=request.session['uid']), nome = request.POST['nome'], ultimo_nome = request.POST['ultimo_nome'], celular = request.POST['celular'], data = request.POST['data'], hora = request.POST['hora'], comentario = request.POST['comentario'])
        c.save()
        for i in request.POST:
            if i.find('_')!=-1:
                
            
                s = Servicos_preenchido(agendamento=c.id, servico=int(sid[1]))
                s.save()
        return redirect('agendamento')
    else:
        data['agendform'] = AgendamentoForm()
        data['history'] = Agendamento.objects.filter(usuario=request.session['uid'])
        return render(request,'agend.html',data)
 """