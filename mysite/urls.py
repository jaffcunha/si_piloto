from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^cadastro_pessoa/$', 'sistema.views.cadastro_pessoa', name='cadastro_pessoa'),
	url(r'^excluir_pessoa/(?P<id_pessoa>[0-9]+)/$', 'sistema.views.excluir_pessoa', name='excluir_pessoa'),
	url(r'^cadastro_projeto/$', 'sistema.views.cadastro_projeto', name='cadastro_projeto'),
	url(r'^excluir_projeto/(?P<id_projeto>[0-9]+)/$', 'sistema.views.excluir_projeto', name='excluir_projeto'),
	url(r'^editar_projeto/(?P<id_projeto>[0-9]+)/$', 'sistema.views.editar_projeto', name='editar_projeto'),
)
