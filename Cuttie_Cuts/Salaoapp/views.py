from http.client import HTTPResponse
from django.shortcuts import render, redirect, HttpResponse
from Salaoapp.forms import UsersForm, AgendamentoForm, ServicosForm
from Salaoapp.models import Usuario, Agendamento, Servicos, Servicos_preenchido


# Create your views here.
def home(request):
    return render(request, 'index.html')

def homepage(request):
    try:
        profile = {}
        profile['uid'] = Usuario.objects.get(id=request.session['uid'])
        return render(request,'homepage.html',profile)
    except:
        return render(request, 'index.html')

def cadastro(request):
    data = {}
    data['userform'] = UsersForm()
    return render(request,'cadastro.html',data)

def docad(request):
    tabela = Usuario.objects.all()
    form = UsersForm(request.POST or None)
    for c in tabela:
        if form['usuario'].data == c.usuario:
            return render(request, 'erro.html')
        if form['celular'].data == c.celular:
            return render(request, 'erro.html')
    if form.is_valid():
            form.save()
    return render(request, 'sucesso.html')

def erro(request):
    return render(request, 'erro.html',)
    
def sucesso(request):
    return render(request, 'sucesso.html',)

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

def profile(request):
    try:
        profile = {}
        profile['perfil'] = UsersForm(instance=Usuario.objects.get(id=request.session['uid']))
        return render(request,'profile.html',profile)
    except:
        return render(request, 'index.html')

def do_update(request):
    form= Usuario.objects.get(id=request.session['uid'])
    form.usuario = request.POST['usuario']
    form.nome = request.POST['nome']
    form.ultimo_nome = request.POST['ultimo_nome']
    form.celular = request.POST['celular']
    form.save()
    return redirect('homepage')
      

def agendamento(request):
    data = {}
    data['servicoform'] = Servicos.objects.all()
    if request.method == 'POST':
        c = Agendamento(usuario=Usuario.objects.get(id=request.session['uid']), nome = request.POST['nome'], ultimo_nome = request.POST['ultimo_nome'], celular = request.POST['celular'], data = request.POST['data'], hora = request.POST['hora'], comentario = request.POST['comentario'])
        c.save()
        for i in request.POST:
            if i.find("-")!=-1:
                print(i)
                sid = i.split("-")
                s = Servicos_preenchido.objects.create(servico=Servicos.objects.get(id=sid[1]), agendamento=c)
                s.save()
        return redirect('agendamento')
    else:
        data['agendform'] = AgendamentoForm()
        data['history'] = Agendamento.objects.filter(usuario=request.session['uid'])
        return render(request,'agend.html',data)



def edit_coment(request, id):
    c = Agendamento.objects.get(id=id)
    if request.method == 'POST':
        f = AgendamentoForm(request.POST, instance=c)
        f.save()
        return redirect('agendamento')
    else:
        f = AgendamentoForm(instance=c)
        return render(request, 'agend.html',{'agendform':f})

def agend_delete(request, id):
    c =Agendamento.objects.get(id=id)
    c.delete()
    return redirect('agendamento')



