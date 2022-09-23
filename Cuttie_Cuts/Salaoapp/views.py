from django.shortcuts import render, redirect
from Salaoapp.forms import UsersForm
from Salaoapp.forms import Usuario

# Create your views here.

def index(request):
    return render(request,'index.html',{})

def cadastro(request):
	data = {}
	data['form'] = UsersForm()
	return render(request,'cadastro.html',data)


def docad(request):
    tabela = Usuario.objects.all()
    form = UsersForm(request.POST or None)
    erro = ''
    for c in tabela:
        if form['usuario'].data == c.usuario :
            erro = "Mensagem de erro"
    if form.is_valid() and erro == '':
            form.save()
    return redirect('cadastro')

def agendamento(request):
    return render(request, 'agend.html',)

def agendamento(request):
    return render(request, 'a.html',)

def login(request):
    return render(request, 'login.html',)
