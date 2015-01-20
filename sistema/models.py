from django.db import models	
from django.contrib.auth.models import User
import os
from django.db.models.signals import post_save

# Create your models here.

class Pessoa(models.Model):
	nome_pessoa = models.CharField("Nome e sobrenome", max_length = 64)
	idade = models.IntegerField("Idade", max_length = 16)
	genero = models.CharField("Genero", max_length = 64)
	cpf = models.CharField("CPF", max_length = 64)
	empresa = models.CharField("Empresa", max_length = 64)
	cargo = models.CharField("Cargo ocupado", max_length = 64)
	#Completar com mais atributos mais tarde

class Projeto(models.Model):
	nome_projeto = models.CharField("Nome do projeto", max_length = 64)
	data_inicio = models.DateField("Inicio do projeto")
	data_fim = models.DateField("Fim do projeto")
	categoria = models.CharField("Categoria", max_length = 64)
	descricao = models.TextField("Descricao do projeto")