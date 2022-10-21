from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from Salaoapp.forms import UsersForm, EnderecoForm, AgendamentoForm
from Salaoapp.forms import Usuario


# Create your views here.
def home(request):
    try:
        profile = {}
        profile['uid'] = Usuario.objects.get(id=request.session['uid'])
    except:
        return render(request, 'index.html')
    return render(request,'index.html',profile)

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
    if request.method == "POST":
        tabela = Usuario.objects.all()
        form = UsersForm(request.POST or None)
        try:
            u = Usuario.objects.get(usuario=request.POST['usuario'])
        except:
            return render(request, 'errorlog.html')

        if u.senha == request.POST['senha']:
            request.session['uid'] = u.id
            return redirect('sucessolog')
        else:
            return render(request,'errorlog.html')
    else:
        redirect('login')


def logout(request):
    try:
        del request.session['uid']
        return redirect('sucessologout')
    except:
        pass
        return redirect('errorlogout')
        
def sucessolog(request):
    return render(request, 'sucessolog.html',)

def sucessologout(request):
    return render(request, 'sucessologout.html',)

def errorlog(request):
    return render(request, 'errorlog.html',)

def errorlogout(request):
    return render(request, 'errorlogout.html',)
    