from django.forms import DateInput, ModelForm, TimeInput
from django import forms
from Salaoapp.models import Usuario, Endereco, Agendamento

# Create the form class.
class UsersForm(ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        widgets = {'password': forms.PasswordInput(),}
        fields = ['usuario', 'senha', 'nome', 'ultimo_nome', 'celular']

class EnderecoForm(ModelForm):
    cep = forms.CharField(max_length=8)
    class Meta:
        model = Endereco
        fields = ['logradouro', 'cep']

class AgendamentoForm(ModelForm):
    data = forms.DateField(widget=DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = Agendamento
        fields = ['data', 'hora']
