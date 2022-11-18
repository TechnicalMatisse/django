from tkinter import Widget
from django.forms import DateInput, ModelForm, TimeInput
from django import forms
from Salaoapp.models import Usuario, Agendamento, Servicos

TIME_CHOICES = [
    ("08:00 às 09:00", "08:00 às 09:00"),
    ("09:00 às 10:00", "09:00 às 10:00"),
    ("10:00 às 11:00", "10:00 às 11:00"),
    ("11:00 às 12:00", "11:00 às 12:00"),
    ("13:00 às 14:00", "13:00 às 14:00"),
    ("14:00 às 15:00", "14:00 às 15:00"),
    ("15:00 às 16:00", "15:00 às 16:00"),
    ("16:00 às 17:00", "16:00 às 17:00"),
    ("17:00 às 18:00", "17:00 às 18:00"),
    ("18:00 às 19:00", "18:00 às 19:00"),
]

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
    hora = forms.ChoiceField(choices = TIME_CHOICES,)
    celular = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_cel(event)', 'maxlength': '10'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    ultimo_nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    class Meta:
        model = Agendamento
        fields = [ 'nome', 'ultimo_nome', 'celular', 'data', 'hora', 'comentario']


class ServicosForm(ModelForm):
    manicure = forms.BooleanField()
    pedicure = forms.BooleanField()
    penteado = forms.BooleanField()
    corte = forms.BooleanField()
    sobrancelha = forms.BooleanField()
    depilacao = forms.BooleanField()
    limpeza = forms.BooleanField()
    class Meta:
        model = Servicos
        fields = [ 'manicure', 'pedicure', 'penteado', 'corte', 'sobrancelha', 'depilacao', 'limpeza']






""" class PacotesForm(ModelForm):
    prata = forms.BooleanField()
    bronze = forms.BooleanField()
    ouro = forms.BooleanField()
    diamante = forms.BooleanField()
    class Meta:
        model = Agendamento
        fields = [ 'prata', 'bronze', 'ouro'] """