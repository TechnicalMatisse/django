from tkinter.tix import MAX
from django.db import models

# Create your models here.

class Usuario (models.Model):
    usuario = models.CharField(max_length=25)     
    senha = models.CharField(max_length=16)           
    nome = models.CharField(max_length=16)
    ultimo_nome = models.CharField(max_length=16)
    celular = models.IntegerField(max_length=9)

class Endereco (models.Model):
    logradouro = models.CharField(max_length=45)
    cep = models.IntegerField(max_length=8)

class Agendamento (models.Model):
    data = models.DateField()
    hora = models.TimeField()


