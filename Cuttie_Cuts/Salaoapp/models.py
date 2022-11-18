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
    hora = models.CharField(max_length=120)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=25)
    ultimo_nome = models.CharField(max_length=25)
    celular = models.CharField(max_length=10)
    comentario = models.TextField(max_length=255, blank=True)

class Servicos(models.Model):
    preenchido = models.ManyToManyField(Agendamento, through='Servicos_preenchido')

class Servicos_preenchido(models.Model):
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    
