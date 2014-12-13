from django.db import models
from django.contrib.auth.models import User
import os
from django.db.models.signals import post_save

# Create your models here.

class Pessoa(models.Model):
	nome_pessoa = models.CharField("Nome.Sobrenome", max_Length = 64)
	idade = models.NumberField("Idade", max_Length = 16)
	genero = models.CharField("Genero", max_Length = 64)
	cpf = models.CharField("CPF", max_Length = 64)
	empresa = models.CharField("Empresa", max_Length = 64)
	cargo = models.CharField("Cargo ocupado", max_Length = 64)
	#Completar com mais atributos mais tarde