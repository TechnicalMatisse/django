from django.forms import DateInput, ModelForm, TimeInput
from django import forms
from Salaoapp.models import Usuario, Endereco, Agendamento

# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'maxlength': '14'}))
    celular = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_cel(event)', 'maxlength': '14'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    ultimo_nome = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_nome(event)'}))
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha', 'nome', 'ultimo_nome', 'celular']

class EnderecoForm(ModelForm):
    cep = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'regex_cep(event)', 'maxlength': '9'}))
    class Meta:
        model = Endereco
        fields = ['logradouro', 'cep']

class AgendamentoForm(ModelForm):
    data = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = Agendamento
        fields = ['data', 'hora']
