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

@login_required
def minha_conta(request):
    texto = TextoPagina.pega_texto_local('carrinho')
    return render_to_response("minha_conta.html", locals(), context_instance=RequestContext(request))
    
def carrinho(request):
    texto = TextoPagina.pega_texto_local('carrinho')
    return render_to_response("carrinho.html", locals(), context_instance=RequestContext(request))

def cadastro_cliente(request):
    erro_usuario = False
    if request.method == 'GET':
        user_form = UserCreationForm(prefix='user')
        cliente_form = ClienteForm(prefix='cliente')
        endereco_form = EnderecoClienteForm(prefix='endereco_cliente')
    else:
        user = User()
        user_form = UserCreationForm(request.POST, instance=user, prefix='usuario')
        if user_form.is_valid():
            user = user_form.save()
            endereco_cliente = Endereco()
            endereco_form = EnderecoClienteForm(request.POST, instance=endereco_cliente, prefix='endereco_cliente')
            if endereco_form.is_valid():
                endereco_cliente = endereco_form.save()
                cliente = Cliente()
                cliente.user = user
                cliente.endereco = endereco_cliente
                cliente_form = ClienteForm(request.POST, instance=cliente, prefix='cliente')
                if cliente_form.is_valid():
                    cliente = cliente_form.save()
                    url = reverse('home')
                    return HttpResponseRedirect(url)
                else:
                    endereco_cliente.delete()
                    user.delete()
                    user_form = UserCreationForm(request.POST, prefix='usuario')
                    cliente_form = ClienteForm(request.POST, prefix='cliente')
                    endereco_form = EnderecoClienteForm(request.POST, prefix='endereco_cliente')
                    erro = True
            else:
                user.delete()
                user_form = UserCreationForm(request.POST, prefix='usuario')
                cliente_form = ClienteForm(request.POST, prefix='cliente')
                endereco_form = EnderecoClienteForm(request.POST, prefix='endereco_cliente')
                erro = True
        else:
            user_form = UserCreationForm(request.POST, prefix='usuario')
            cliente_form = ClienteForm(request.POST, prefix='cliente')
            endereco_form = EnderecoClienteForm(request.POST, prefix='endereco_cliente')
            erro = True
    return render_to_response('cadastro_cliente.html', locals(), context_instance=RequestContext(request))
    