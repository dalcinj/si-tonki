# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from django.http import HttpResponseRedirect, HttpResponse

from site_bill.sistema.models import *
from site_bill.sistema.forms import *

###########################
######## Funções ##########
###########################

def calcula_carrinho(lista_produtos_carrinho):
    valor = 0
    for produto in lista_produtos_carrinho:
        valor += produto.valor_total
    return valor

###########################
######## Páginas ##########
###########################

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

###Carrinho
def carrinho(request):
    texto = TextoPagina.pega_texto_lugar('carrinho')
    cliente = request.user.get_profile()
    carrinho = Carrinho.pega_carrinho_atual(cliente)
    lista_produtos_carrinho = ProdutoCarrinho.objects.filter(carrinho=carrinho)
    valor_total_compra = calcula_carrinho(lista_produtos_carrinho)
    return render_to_response("carrinho.html", locals(), context_instance=RequestContext(request))
    
def add_carrinho(request, id_produto):
    produto = BancoProduto.objects.get(id=id_produto)
    cliente = request.user.get_profile()
    carrinho = Carrinho.objects.filter(cliente=cliente).get(concluido=False)
    try:
        produto_carrinho = ProdutoCarrinho.objects.get(produto=produto)
        produto_carrinho.quantidade += 1
        produto_carrinho.valor_total += produto_carrinho.produto.valor_unitario_venda
        produto_carrinho.save()
    except:
        produto_carrinho = ProdutoCarrinho(carrinho=carrinho, produto=produto, quantidade=1, valor_total=produto.valor_unitario_venda)
        produto_carrinho.save()
    return HttpResponseRedirect('/carrinho/')

def remove_carrinho(request, id_produto_carrinho):
    produto_carrinho = ProdutoCarrinho.objects.get(id=id_produto_carrinho)
    produto_carrinho.delete()
    return HttpResponseRedirect('/carrinho/')
    
def atualiza_carrinho(request):
    cliente = request.user.get_profile()
    carrinho = Carrinho.pega_carrinho_atual(cliente)
    lista_produtos_carrinho = ProdutoCarrinho.objects.filter(carrinho=carrinho)
    count = 1
    for produto_carrinho in lista_produtos_carrinho:
        try:
            qtd = request.POST['qtd-'+str(count)]
            produto_carrinho.quantidade = float(qtd)
            produto_carrinho.valor_total = float(qtd)*produto_carrinho.produto.valor_unitario_venda
            produto_carrinho.save()
        except:
            pass
        count += 1
    return HttpResponseRedirect('/carrinho/')
    
##Finalizar Compra
def verificacao_carrinho(request):
    cliente = request.user.get_profile()
    carrinho = Carrinho.pega_carrinho_atual(cliente)
    lista_produtos_carrinho = ProdutoCarrinho.objects.filter(carrinho=carrinho)
    return render_to_response("verificacao_carrinho.html", locals(), context_instance=RequestContext(request))
   
    