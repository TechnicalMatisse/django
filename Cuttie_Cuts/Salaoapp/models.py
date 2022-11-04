from functools import partial
from tkinter.tix import MAX
from django.db import models

# Create your models here.

class Usuario (models.Model):
    usuario = models.CharField(max_length=25)
    senha = models.CharField(max_length=16)
    nome = models.CharField(max_length=25)
    ultimo_nome = models.CharField(max_length=25)
    celular = models.CharField(max_length=10)

class Agendamento (models.Model):
    data = models.DateField()
    hora = models.TimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=25)
    ultimo_nome = models.CharField(max_length=25)
    celular = models.CharField(max_length=10)
    comentario = models.TextField(max_length=255)

class Pacotes(models.Model):
    prata = models.BooleanField()
    bronze = models.BooleanField()
    ouro = models.BooleanField()
    diamante = models.BooleanField()

class Servicos(models.Model):
    manicure = models.BooleanField()
    pedicure = models.BooleanField()
    pentado = models.BooleanField()
    corte = models.BooleanField()
    sobrancelha = models.BooleanField()
    depilacao = models.BooleanField()
    limpeza = models.BooleanField()