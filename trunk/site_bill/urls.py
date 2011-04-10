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

    #Páginas Iniciais 
    url(r'^$', 'django.views.generic.simple.redirect_to', {'url': 'index/'}),
    url(r'^index/$', 'site_bill.sistema.views.sistema.index', name='index'),
    url(r'^login/$', 'site_bill.sistema.views.sistema.login', name='login'),
    url(r'^logout/$', 'site_bill.sistema.views.sistema.logout', name='logout'),
    
    #Cliente
    url(r'^home/$', 'site_bill.sistema.views.cliente.home', name='home'),
    url(r'^cadastro_cliente/$', 'site_bill.sistema.views.cliente.cadastro_cliente', name='cadastro_cliente'),
    
    
    
    
    #Localmente
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.getcwd(),'static') }),
    url(r'^arquivos/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.getcwd(),'arquivos') }),
    
)
