#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from django.contrib.localflavor.br.forms import *

from site_bill.sistema.models import *

# SISTEMA
class LoginForm(forms.Form):
    username = forms.CharField(max_length=128, label='Usuário')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput,label= 'Senha')
# /SISTEMA


# CLIENTE
class ClienteForm(forms.ModelForm):
    telefone = BRPhoneNumberField(label='Telefone Residencial')
    celular = BRPhoneNumberField()
    cpf = BRCPFField(label='CPF')
    
    class Meta:
        model = Cliente
        exclude = ['user','endereco']
        
class EnderecoClienteForm(forms.ModelForm):
    
    class Meta:
        model = Endereco
        
# /CLIENTE       
    
