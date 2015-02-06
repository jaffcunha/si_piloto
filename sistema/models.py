from django.db import models	
from django.contrib.auth.models import User
import os
from django.db.models.signals import post_save

# Create your models here.

class Pessoa(models.Model):
	nome_pessoa = models.CharField("Nome completo", max_length = 64)
	idade = models.IntegerField("Idade", max_length = 16)
	genero = models.CharField("Genero", max_length = 64)
	cpf = models.CharField("CPF", max_length = 64)
	empresa = models.CharField("Empresa", max_length = 64)
	cargo = models.CharField("Cargo ocupado", max_length = 64)

class Produto(models.Model):
	nome_produto = models.CharField("Nome do produto", max_length = 64) 
	valor = models.CharField('Valor do produto', max_length = 64)

class Projeto(models.Model):
	nome_projeto = models.CharField("Nome do projeto", max_length = 64)
	data_inicio = models.DateField("Inicio do projeto (dd/mm/aaaa)")
	data_fim = models.DateField("Fim do projeto (dd/mm/aaaa)")
	categoria = models.CharField("Categoria", max_length = 64)
	descricao = models.TextField("Descricao do projeto")
	
class Enquete(models.Model):
<<<<<<< HEAD
	titulo_enquete = models.CharField("Titulo da enquete", max_length = 128)
	assunto_enquete = models.CharField("Assunto da enquete", max_length = 128)
	
class Opcao(models.Model):
	opcao=models.CharField("Opcao", max_length = 64)
=======
	titulo_enquete = models.CharField("Título da enquete", max_length = 128)
	assunto_enquete = models.CharField("Assunto da enquete", max_length = 128)
	
>>>>>>> c34985415f64a4d4f249ee46e44e80dce88a0d53
