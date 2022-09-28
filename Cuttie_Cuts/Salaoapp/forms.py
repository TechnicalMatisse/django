from django.forms import ModelForm
from django import forms
from Salaoapp.models import Usuario, Endereco

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
