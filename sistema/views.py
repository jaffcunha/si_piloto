from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from sistema.forms import *
from sistema.models import *
from django.core.exceptions import PermissionDenied

# Create your views here.

def cadastro_pessoa(request):
	if request.method == 'GET':
		pessoa_form = PessoaForm()
	if request.method == 'POST':
		pessoa_form = PessoaForm(request.POST)
		if pessoa_form.is_valid():
			pessoa_form.save()
		else:
			dados_incorretos = True
			return render_to_response('cadastro_pessoa.html', locals(), context_instance=RequestContext(request))
	return render_to_response('cadastro_pessoa.html', locals(), context_instance=RequestContext(request))

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


