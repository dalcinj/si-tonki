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
        cliente = request.user.get_profile()
        cliente_form = EditaClienteForm(instance=cliente)
        endereco_form = EnderecoClienteForm()
        lista_enderecos = cliente.endereco.all()
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

@login_required
def edita_cliente(request):
    cliente = request.user.get_profile()
    endereco_form = EnderecoClienteForm()
    lista_enderecos = cliente.endereco.all()
    if request.method == 'GET':
        cliente_form = EditaClienteForm(instance=cliente)
    else:
        cliente_form = EditaClienteForm(request.POST, instance=cliente)
        if cliente_form.is_valid():
            cliente = cliente_form.save()
            url = reverse('minha_conta')
            request.user.message_set.create(message='Modificações salvas com sucesso!')
            return HttpResponseRedirect(url)
        else:
            cliente_form = EditaClienteForm(request.POST)
            request.user.message_set.create(message='Preencha o formulário corretamente.')
    return render_to_response('edita_cliente.html', locals(), context_instance=RequestContext(request))
    
@login_required
def add_endereco_cliente(request):
    cliente = request.user.get_profile()
    lista_enderecos = cliente.endereco.all()
    if request.method == 'GET':
        endereco_form = EnderecoClienteForm()
    else:
        endereco_form = EnderecoClienteForm(request.POST)
        if endereco_form.is_valid():
            endereco = endereco_form.save()
            cliente.endereco.add(endereco)
            request.user.message_set.create(message='Endereço adicionado com sucesso!')
            url = reverse('minha_conta')
            return HttpResponseRedirect(url)
        else:
            endereco_form = EnderecoClienteForm(request.POST)
            request.user.message_set.create(message='Preencha o formulário corretamente.')
    return render_to_response('add_endereco.html', locals(), context_instance=RequestContext(request))
    
@login_required
def edita_endereco_cliente(request, id_endereco):
    cliente = request.user.get_profile()
    endereco = Endereco.pega_endereco_id(id_endereco)
    if request.method == 'GET':
        endereco_form = EnderecoClienteForm(instance=endereco)
    else:
        endereco_form = EnderecoClienteForm(request.POST, instance=endereco)
        if endereco_form.is_valid():
            endereco = endereco_form.save()
            request.user.message_set.create(message='Endereço modificado com sucesso!')
            url = reverse('minha_conta')
            return HttpResponseRedirect(url)
        else:
            endereco_form = EnderecoClienteForm(request.POST)
            request.user.message_set.create(message='Preencha o formulário corretamente.')
    return render_to_response('edita_endereco_cliente.html', locals(), context_instance=RequestContext(request))
    
@login_required
def remove_endereco_cliente(request, id_endereco):
    cliente = request.user.get_profile()
    endereco = Endereco.pega_endereco_id(id_endereco)
    cliente.endereco.remove(endereco)
    endereco.delete()
    request.user.message_set.create(message='Endereço removido com sucesso!')
    url = reverse('minha_conta')
    return HttpResponseRedirect(url)
    

    