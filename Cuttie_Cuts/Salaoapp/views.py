from django.shortcuts import render
from Salaoapp.forms import UsersForm

# Create your views here.

def index(request):
    return render(request,'index.html',{})

def cadastro(request):
	data = {}
	data['form'] = UsersForm()
	return render(request,'cadastro.html',data)

def agendamento(request):
    return render(request, 'a.html',)
    
def login(request):
    return render(request, 'login.html',)

