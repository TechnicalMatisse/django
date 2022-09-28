from django.shortcuts import render, redirect
from Salaoapp.forms import UsersForm, EnderecoForm
from Salaoapp.forms import Usuario

# Create your views here.

def home(request):
    return render(request,'index.html',{})

def cadastro(request):
    data = {}
    data['userform'] = UsersForm()
    data['endereco'] = EnderecoForm()
    return render(request,'cadastro.html',data)


def docad(request):
    tabela = Usuario.objects.all()
    form = UsersForm(request.POST or None)
    form_sec = EnderecoForm(request.POST or None)
    erro = ''
    for c in tabela:
        if form['usuario'].data == c.usuario:
            erro = "Mensagem de erro"
    if form.is_valid() and erro == '':
            form.save()
            form_sec.save()
    return redirect('cadastro')

def agendamento(request):
    return render(request, 'agend.html',)

def contagendamento(request):
    return render(request, 'a.html',)

def login(request):
    data = {}
    data['userform'] = UsersForm()
    return render(request,'login.html',data)

def dologin(request):
    tabela = Usuario.objects.all()
    form = UsersForm(request.POST or None)
    usuario = ''
    for c in tabela:
        if form['usuario'].data == c.usuario:
            if form['senha'].data == c.senha:
                return render('')
    return redirect('home')
