from tkinter import Widget
from django.forms import DateInput, ModelForm, TimeInput
from django import forms
from Salaoapp.models import Usuario, Agendamento

# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'maxlength': '14'}))
    celular = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_cel(event)', 'maxlength': '10'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    ultimo_nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha', 'nome', 'ultimo_nome', 'celular']

class AgendamentoForm(ModelForm):
    data = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))
    celular = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_cel(event)', 'maxlength': '10'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    ultimo_nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    class Meta:
        model = Agendamento
        fields = [ 'nome', 'ultimo_nome', 'celular', 'data', 'hora', 'comentario']

class PacotesForm(ModelForm):
    prata = forms.BooleanField()
    bronze = forms.BooleanField()
    ouro = forms.BooleanField()
    diamante = forms.BooleanField()
    class Meta:
        model = Agendamento
        fields = [ 'prata', 'bronze', 'ouro']
        
class PacotesForm(ModelForm):
    manicure = forms.BooleanField()
    pedicure = forms.BooleanField()
    pentado = forms.BooleanField()
    corte = forms.BooleanField()
    sobrancelha = forms.BooleanField()
    depilacao = forms.BooleanField()
    limpeza = forms.BooleanField()

