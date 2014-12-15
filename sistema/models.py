from django.db import models
from django.contrib.auth.models import User
import os
from django.db.models.signals import post_save

# Create your models here.

class Pessoa(models.Model):
	nome_pessoa = models.CharField("Nome.Sobrenome", max_length = 64)
	idade = models.CharField("Idade", max_length = 16)
	genero = models.CharField("Genero", max_length = 64)
	cpf = models.CharField("CPF", max_length = 64)
	empresa = models.CharField("Empresa", max_length = 64)
	cargo = models.CharField("Cargo ocupado", max_length = 64)
	#Completar com mais atributos mais tarde