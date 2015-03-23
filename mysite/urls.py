from django.conf.urls import patterns, include, url
from django.contrib import admin
from sistema.views import *
from sistema.forms import *	#INCLUIR
from django.contrib.formtools.wizard.views import SessionWizardView	 #INCLUIR
from django_pagseguro.urls import pagseguro_urlpatterns #INCLUIR para uso de PagSeguro

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
	url(r'^visualizar_projetos/$', 'sistema.views.visualizar_projetos', name='visualizar_projetos'),
	url(r'^excluir_projeto/(?P<id_projeto>[0-9]+)/$', 'sistema.views.excluir_projeto', name='excluir_projeto'),
	url(r'^editar_projeto/(?P<id_projeto>[0-9]+)/$', 'sistema.views.editar_projeto', name='editar_projeto'),
	url(r'^criar_enquete/$', 'sistema.views.criar_enquete', name='criar_enquete'),
	url(r'^editar_enquete/(?P<id_enquete>[0-9]+)/$', 'sistema.views.editar_enquete', name='editar_enquete'),	
	url(r'^excluir_enquete/(?P<id_enquete>[0-9]+)/$', 'sistema.views.excluir_enquete', name='excluir_enquete'),
	url(r'^visualizar_enquete/$', 'sistema.views.visualizar_enquete', name='visualizar_enquete'),
	url(r'^formwizard/$', SubClassFormWizard.as_view([PessoaForm, ProjetoForm]), name='formwizard'), 		#INCLUIR
	url(r'^formwizard_diferentes/$', SubClassFormWizard.as_view(FORMS), name='formwizard_diferentes'), 		#INCLUIR para usar templates diferentes para cada form
	url(r'^login/$', 'sistema.views.login', name='login'),
    url(r'^logout/$', 'sistema.views.logout', name='logout'),
	url(r'^home/$', 'sistema.views.home', name='home'),
	url(r'^pagamento_botao/$', 'sistema.views.pagamento_botao', name='pagamento_botao'),
	url(r'^cadastro_opcao/(?P<numero_enquete>[0-9]+)/$', 'sistema.views.cadastro_opcao', name='cadastro_opcao'),
)

urlpatterns += pagseguro_urlpatterns()
