# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from datetime import *

from site_bill.sistema.models import *
from site_bill.sistema.forms import *

# Create your views here.
def vitrini(request):
    texto = TextoPagina.pega_texto_lugar('vitrini')
    lista_produtos_vitrini = BancoProduto.objects.filter(aparecer_vitrini=True)
    return render_to_response("vitrini.html", locals(), context_instance=RequestContext(request))
    
def institucional(request):
    texto = TextoPagina.pega_texto_lugar('institucional')
    return render_to_response("institucional.html", locals(), context_instance=RequestContext(request))
    
def contato(request):
    texto = TextoPagina.pega_texto_lugar('contato')
    return render_to_response("contato.html", locals(), context_instance=RequestContext(request))
    
def login(request):
    erro = False
    login_form = LoginForm()
    if request.method == 'GET':
        return render_to_response('login.html', locals(), context_instance=RequestContext(request))
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('minha_conta')
            else:
                erro = True
                return render_to_response('login.html', locals(), context_instance=RequestContext(request))
        else:
            erro = True
            return render_to_response('login.html', locals(), context_instance=RequestContext(request))

    
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/vitrini/")