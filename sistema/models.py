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
	pergunta_enquete = models.CharField("Digite a pergunta da sua enquete", max_length = 128)
	num_alternativas = models.IntegerField("Quantas alternativas sua pergunta tera?", max_length = 128)
	
class Opcao(models.Model):
	opcao=models.CharField("Alternativa", max_length = 64)
	
