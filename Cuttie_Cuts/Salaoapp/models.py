from tkinter.tix import MAX
from django.db import models

# Create your models here.

class Usuario (models.Model):
    usuario = models.CharField(max_length=25)
    senha = models.CharField(max_length=16)
    nome = models.CharField(max_length=25)
    ultimo_nome = models.CharField(max_length=25)
    celular = models.CharField(max_length=14)

class Endereco (models.Model):
    logradouro = models.CharField(max_length=45)
    cep = models.CharField(max_length=9)

class Agendamento (models.Model):
    data = models.DateField()
    hora = models.TimeField()


