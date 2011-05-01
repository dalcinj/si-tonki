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
    url(r'^cadastro_cliente/$', 'site_bill.sistema.views.cliente.cadastro_cliente', name='cadastro_cliente'),
    url(r'^edita_cliente/$', 'site_bill.sistema.views.cliente.edita_cliente', name='edita_cliente'),
    url(r'^add_endereco_cliente/$', 'site_bill.sistema.views.cliente.add_endereco_cliente', name='add_endereco_cliente'),
    url(r'^edita_endereco_cliente/(?P<id_endereco>[0-9]+)/$', 'site_bill.sistema.views.cliente.edita_endereco_cliente', name='edita_endereco_cliente'),
    url(r'^remove_endereco_cliente/(?P<id_endereco>[0-9]+)/$', 'site_bill.sistema.views.cliente.remove_endereco_cliente', name='remove_endereco_cliente'),
    
    #Produtos
    url(r'^lista_produtos_categoria/(?P<id_categoria>[0-9]+)/$', 'site_bill.sistema.views.produto.lista_produtos_categoria', name='lista_produtos_categoria'),
    url(r'^lista_produtos_marca/(?P<id_marca>[0-9]+)/$', 'site_bill.sistema.views.produto.lista_produtos_marca', name='lista_produtos_marca'),
    url(r'^detalhes_produto/(?P<id_produto>[0-9]+)/$', 'site_bill.sistema.views.produto.detalhes_produto', name='detalhes_produto'),
    url(r'^adiciona_comentario/(?P<id_produto>[0-9]+)/$', 'site_bill.sistema.views.produto.adiciona_comentario', name='adiciona_comentario'),
    url(r'^busca_produtos/$', 'site_bill.sistema.views.produto.busca_produtos', name='busca_produtos'),
    
    
    #Carrinho
    url(r'^carrinho/$', 'site_bill.sistema.views.produto.carrinho', name='carrinho'),
    url(r'^add_carrinho/(?P<id_produto>[0-9]+)/$', 'site_bill.sistema.views.produto.add_carrinho', name='add_carrinho'),
    url(r'^remove_carrinho/(?P<id_produto_carrinho>[0-9]+)/$', 'site_bill.sistema.views.produto.remove_carrinho', name='remove_carrinho'),
    url(r'^atualiza_carrinho/$', 'site_bill.sistema.views.produto.atualiza_carrinho', name='atualiza_carrinho'),
    
    #Finalização da Compra
    url(r'^verificar_compra/$', 'site_bill.sistema.views.produto.verificar_compra', name='verificar_compra'),
    
    
    #Localmente
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.getcwd(),'static') }),
    url(r'^arquivos/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.getcwd(),'arquivos') }),
    
)
