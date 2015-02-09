from django.forms import ModelForm, TextInput, Select, PasswordInput, Textarea, CharField
from django import forms
from sistema.models import *
from django.contrib.auth.forms import PasswordChangeForm

class PessoaForm(forms.ModelForm):
	class Meta:
		model = Pessoa
		fields = ('nome_pessoa', 'idade', 'genero', 'cpf', 'empresa', 'cargo')

class ProjetoForm(forms.ModelForm):
	class Meta:
		model = Projeto
		fields = ('nome_projeto', 'data_inicio', 'data_fim', 'categoria', 'descricao')

class EnqueteForm(forms.ModelForm):
	class Meta:
		model=Enquete
		fields=('pergunta_enquete', 'num_alternativas')

class OpcaoForm(forms.ModelForm):
	class Meta:
		model=Opcao


