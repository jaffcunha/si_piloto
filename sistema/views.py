from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sistema.forms import *
from sistema.models import *
from django.core.exceptions import PermissionDenied
from django.conf import settings

# Create your views here.


# Cadastrar, editar e excluir pessoas
def cadastro_pessoa(request):
	if request.method == 'GET':
		pessoa_form = PessoaForm()
	if request.method == 'POST':
		pessoa_form = PessoaForm(request.POST)
		if pessoa_form.is_valid():
			pessoa_form.save()
		else:
			dados_incorretos = True
			return render(request, 'cadastro_pessoa.html', locals())
	return render(request, 'cadastro_pessoa.html', locals())

def editar_pessoa(request, id_pessoa):
	objeto = Pessoa.objects.get(id = id_pessoa)
	if request.method == 'GET':
		pessoa_form = PessoaForm(instance = objeto)
	if request.method == 'POST':
		pessoa_form = PessoaForm(instance = objeto)
		if pessoa_form.is_valid():
			pessoa_form.save()
		else:
			dados_incorretos = True
			return render_to_response('cadastro_pessoa.html', locals(), context_instance=RequestContext(request))
	return render_to_response('cadastro_pessoa.html', locals(), context_instance=RequestContext(request))

def excluir_pessoa(request, id_pessoa):
	objeto = Pessoa.objects.get(id = id_pessoa)
	objeto.delete()


#Cadastrar, editar e excluir projetos
def cadastro_projeto(request):
	if request.method == 'GET':
		projeto_form = ProjetoForm()
	if request.method == 'POST':
		projeto_form = ProjetoForm(request.POST)
		if projeto_form.is_valid():
			projeto_form.save()
		else: 
			dados_incorretos = True
			return render_to_response('cadastro_projeto.html', locals(), context_instance=RequestContext(request))
	return render_to_response('cadastro_projeto.html', locals(), context_instance=RequestContext(request))

def editar_projeto(request, id_projeto):
	objeto = Projeto.objects.get(id = id_projeto)
	if request.method == 'GET':
		projeto_form = ProjetoForm(instance = objeto)
	if request.method == 'POST':
		projeto_form = ProjetoForm(instance = objeto)
		if projeto_form.is_valid():
			projeto_form.save()
		else:
			dados_incorretos = True
			return render_to_response('cadastro_projeto.html', locals(), context_instance=RequestContext(request))
	return render_to_response('cadastro_projeto.html', locals(), context_instance=RequestContext(request))

# def excluir_projeto:
# 	objeto = Projeto.objects.get(id = id_projeto)
# 	objeto.delete()


