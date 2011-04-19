# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from site_bill.sistema.models import *
from site_bill.sistema.forms import *

# Create your views here.

def lista_produtos_categoria(request, id_categoria):
    categoria = CategoriaProduto.pega_gategoria_id(id_categoria)
    lista_produtos = BancoProduto.pega_prod_cat(categoria)
    return render_to_response("produtos_categoria.html", locals(), context_instance=RequestContext(request))

def lista_produtos_marca(request, id_marca):
    marca = MarcaProduto.pega_marca_id(id_marca)
    lista_produtos = BancoProduto.pega_prod_marca(marca)
    return render_to_response("produtos_marca.html", locals(), context_instance=RequestContext(request))

def detalhes_produto(request, id_produto):
    produto = BancoProduto.pega_prod_id(id_produto)
    return render_to_response("detalhes_produto.html", locals(), context_instance=RequestContext(request))