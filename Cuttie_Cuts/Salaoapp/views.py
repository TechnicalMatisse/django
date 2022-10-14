from django.shortcuts import render, redirect
from Salaoapp.forms import UsersForm, EnderecoForm, AgendamentoForm
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
    for c in tabela:
        if form['usuario'].data == c.usuario:
            return render(request, 'erro.html')
        if form['celular'].data == c.celular:
            return render(request, 'erro.html')
    if form.is_valid() and form_sec.is_valid():
            form.save()
            form_sec.save()
    return render(request, 'sucesso.html')

def erro(request):
    return render(request, 'erro.html',)
    
def sucesso(request):
    return render(request, 'sucesso.html',)

def agendamento(request):
    return render(request, 'agend.html',)

def contagendamento(request):
    data = {}
    data['agendform'] = AgendamentoForm()
    return render(request, 'a.html',data)

def login(request):
    data = {}
    data['userform'] = UsersForm()
    return render(request,'login.html',data)

def dologin(request):
    tabela = Usuario.objects.all()
    form = UsersForm(request.POST or None)
    for c in tabela:
        if form['usuario'].data == c.usuario:
            if form['senha'].data == c.senha:
                return render()
    return redirect('home')