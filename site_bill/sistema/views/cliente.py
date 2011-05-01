# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

from site_bill.sistema.models import *
from site_bill.sistema.forms import *

# Create your views here.

def minha_conta(request):
    texto = TextoPagina.pega_texto_lugar('minha_conta')
    if request.user.is_authenticated():
        pass
    else:
        login_form = LoginForm()
        user_form = UserCreationForm()
        cliente_form = ClienteForm()
    return render_to_response("minha_conta.html", locals(), context_instance=RequestContext(request))
    

def cadastro_cliente(request):
    erro = False
    cadastrou = False
    if request.method == 'GET':
        user_form = UserCreationForm()
        cliente_form = ClienteForm()
    else:
        user = User()
        user_form = UserCreationForm(request.POST, instance=user)
        if user_form.is_valid():
            user = user_form.save()
            cliente = Cliente()
            cliente.user = user
            cliente_form = ClienteForm(request.POST, instance=cliente)
            if cliente_form.is_valid():
                cliente = cliente_form.save()
                cadastrou = True
                url = reverse('minha_conta')
                return HttpResponseRedirect(url)
            else:
                user.delete()
                user_form = UserCreationForm(request.POST)
                cliente_form = ClienteForm(request.POST)
                erro = True
        else:
            user_form = UserCreationForm(request.POST)
            cliente_form = ClienteForm(request.POST)
            erro = True
    return render_to_response('cadastro_cliente.html', locals(), context_instance=RequestContext(request))

#@login_required
#def edita_cliente(request):
#    cliente = request.user.get_profile()
#    try:
#        lista_enderecos = Endereco.objects.filter()
#    except:
#        lista_enderecos = None
#    if request.method == 'GET':
#        cliente_form = EditaClienteForm()
#        endereco_form = EnderecoClienteForm()
#    else:
#        cliente_form = EditaClienteForm(request.POST, instance=cliente)
#        if cliente_form.is_valid():
#            cliente = cliente_form.save()
#            url = reverse('minha_conta')
#            return HttpResponseRedirect(url)
#        else:
#            user.delete()
#            user_form = UserCreationForm(request.POST)
#            cliente_form = ClienteForm(request.POST)
#            erro = True
#    return render_to_response('cadastro_cliente.html', locals(), context_instance=RequestContext(request))
    