# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings
import os

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^site_bill/', include('site_bill.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    #Páginas Básicas
    url(r'^$', 'django.views.generic.simple.redirect_to', {'url': 'vitrini/'}),
    url(r'^vitrini/$', 'site_bill.sistema.views.sistema.vitrini', name='vitrini'),
    url(r'^institucional/$', 'site_bill.sistema.views.sistema.institucional', name='institucional'),
    url(r'^contato/$', 'site_bill.sistema.views.sistema.contato', name='contato'),
    
    #Sistema
    url(r'^login/$', 'site_bill.sistema.views.sistema.login', name='login'),
    url(r'^logout/$', 'site_bill.sistema.views.sistema.logout', name='logout'),
    
    #Cliente
    url(r'^minha_conta/$', 'site_bill.sistema.views.cliente.minha_conta', name='minha_conta'),
    url(r'^carrinho/$', 'site_bill.sistema.views.cliente.carrinho', name='carrinho'),
    url(r'^cadastro_cliente/$', 'site_bill.sistema.views.cliente.cadastro_cliente', name='cadastro_cliente'),
    
    #Produtos
    url(r'^lista_produtos_categoria/(?P<id_categoria>[0-9]+)/$', 'site_bill.sistema.views.produto.lista_produtos_categoria', name='lista_produtos_categoria'),
    url(r'^lista_produtos_marca/(?P<id_marca>[0-9]+)/$', 'site_bill.sistema.views.produto.lista_produtos_marca', name='lista_produtos_marca'),
    url(r'^detalhes_produto/(?P<id_produto>[0-9]+)/$', 'site_bill.sistema.views.produto.detalhes_produto', name='detalhes_produto'),
    
    
    #Localmente
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.getcwd(),'static') }),
    url(r'^arquivos/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.getcwd(),'arquivos') }),
    
)
