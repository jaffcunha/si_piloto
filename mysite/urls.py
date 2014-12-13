from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^cadastro_pessoa/$', 'sistema.views.cadastro_pessoa', name='cadastro_pessoa'),
	url(r'^excluir_pessoa/(?P<id_pessoa>[0-9]+)/$', 'sistema.views.excluir_pessoa', name='excluir_pessoa'),
)
