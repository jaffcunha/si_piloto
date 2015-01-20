from django.conf.urls import patterns, include, url
from django.contrib import admin
from sistema.views import *
from sistema.forms import *	#INCLUIR
from django.contrib.formtools.wizard.views import SessionWizardView	 #INCLUIR

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^cadastro_pessoa/$', 'sistema.views.cadastro_pessoa', name='cadastro_pessoa'),
	url(r'^editar_pessoa/(?P<id_pessoa>[0-9]+)/$', 'sistema.views.editar_pessoa', name='editar_pessoa'),	
	url(r'^excluir_pessoa/(?P<id_pessoa>[0-9]+)/$', 'sistema.views.excluir_pessoa', name='excluir_pessoa'),
	url(r'^visualizar_pessoas/$', 'sistema.views.visualizar_pessoas', name='visualizar_pessoas'),
	url(r'^cadastro_projeto/$', 'sistema.views.cadastro_projeto', name='cadastro_projeto'),
	url(r'^excluir_projeto/(?P<id_projeto>[0-9]+)/$', 'sistema.views.excluir_projeto', name='excluir_projeto'),
	url(r'^editar_projeto/(?P<id_projeto>[0-9]+)/$', 'sistema.views.editar_projeto', name='editar_projeto'),
	url(r'^formwizard/$', SubClassFormWizard.as_view([PessoaForm, ProjetoForm]), name='formwizard'), 		#INCLUIR
	url(r'^formwizard_diferentes/$', SubClassFormWizard.as_view(FORMS), name='formwizard_diferentes'), 		#INCLUIR para usar templates diferentes para cada form
)
