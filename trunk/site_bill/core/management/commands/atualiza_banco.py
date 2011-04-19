# -*- coding: utf-8 -*-

from django.core.management.base import NoArgsCommand
from django.contrib.auth.models import User
from site_bill.sistema.models import *
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from datetime import *

class Command(NoArgsCommand):
    help = """Cria Groupos"""

    requires_model_validation = 0

    def handle_noargs(self, **options):
        
        def cria_endereco(rua, num, complemento, bairro, cidade, estado, cep):
            endereco = Endereco(rua = rua, num = num, complemento = complemento, bairro = bairro, cidade = cidade, estado = estado, cep = cep)
            endereco.save()
            return endereco
        cliente1_endereco1 = cria_endereco('rua1 cliente1', '12341', 'complemento 11', 'bairro11', 'cidade11', 'estado11', '12312-123')
        cliente1_endereco2 = cria_endereco('rua2 cliente1', '12342', 'complemento 12', 'bairro12', 'cidade12', 'estado12', '12312-123')
        cliente2_endereco1 = cria_endereco('rua1 cliente2', '12343', 'complemento 2', 'bairro2', 'cidade2', 'estado2', '12312-123')
        fornecedor1_endereco = cria_endereco('rua fornecedor1', '1234', 'complemento 1', 'bairro1', 'cidade1', 'estado1', '12312-123')
        fornecedor2_endereco = cria_endereco('rua fornecedor2', '1234', 'complemento 2', 'bairro2', 'cidade2', 'estado2', '12312-123')
        estoque1_endereco = cria_endereco('rua estoque1', '1234', 'complemento 1', 'bairro1', 'cidade1', 'estado1', '12312-123')
        estoque2_endereco = cria_endereco('rua estoque2', '1234', 'complemento 2', 'bairro2', 'cidade2', 'estado2', '12312-123')
        
        def cria_usuario(username, email, password):
            user = User.objects.create_user(username, email, password)
            return user
        usuario1 = cria_usuario('cliente1', 'jhonstondalcin@gmail.com', 'cliente1')
        usuario2 = cria_usuario('cliente2', 'marciohariki@gmail.com', 'cliente2')
        
        def cria_usuario_admin(username, email, password):
            usuario = cria_usuario(username, email, password)
            usuario.is_staff = True
            usuario.is_active = True
            usuario.is_superuser = True
            usuario.save()
            return usuario
        admin = cria_usuario_admin('admin', 'jhonstondalcin@gmail.com', 'admin')
        adminnistrador = cria_usuario_admin('adminnistrador', 'marciohariki@gmail.com', 'adminnistrador')
        
        # CLIENTES
        def cria_cliente(user, endereco, nome, email, email2, telefone, celular, rg, cpf, data_nascimento):
            cliente = Cliente(user = user, endereco = endereco, email=email, email2=email2, nome = nome, telefone = telefone, rg = rg, cpf = cpf, data_nascimento = data_nascimento)
            cliente.save()
            return cliente
        cliente1 = cria_cliente(usuario1, cliente1_endereco1, 'Cliente1', 'jhonstondalcin@gmail.com', 'jhonstondalcin@gmail.com', '7272-3060', '7272-3060', '46.705.983-4', '383.747.188-89', '1990-09-19')
        cliente2 = cria_cliente(usuario2, cliente2_endereco1, 'Cliente2', 'marciohariki@gmail.com', 'marciohariki@gmail.com', '1234-5678', '1234-5678', '56.705.983-4', '483.747.188-89', '1991-09-19')
        # /CLIENTES
        
        # PRODUTOS
        def cria_categoria_produto(categoria, descricao):
            categoria_produto = CategoriaProduto(categoria = categoria, descricao = descricao)
            categoria_produto.save()
            return categoria_produto
        categoria1_produto = cria_categoria_produto('Tênis', 'Os tênis da Bill World Sports são originais, eles combinam com você!')
        categoria2_produto = cria_categoria_produto('Camisas de Times', 'As camisas de times da Bill World Sports são originais, eles combinam com você!')
        
        def cria_marca_produto(marca, descricao):
            marca_produto = MarcaProduto(marca = marca, descricao = descricao)
            marca_produto.save()
            return marca_produto
        marca1_produto = cria_marca_produto('Adidas', 'Adidas é uma empresa x, seus produtos são ótimos.')
        marca2_produto = cria_marca_produto('Puma', 'Puma é uma empresa y, seus produtos são ótimos.')
        
        def cria_fornecedor(nome, descricao, contato, endereco):
            fornecedor = Fornecedor(nome = nome, descricao = descricao, contato = contato, endereco = endereco)
            fornecedor.save()
            return fornecedor
        fornecedor1 = cria_fornecedor('loja fornecedora1', 'descricao fornecedora 1', 'responsável pelo fornecedor: josé, tel 1111-1111', fornecedor1_endereco)
        fornecedor2 = cria_fornecedor('loja fornecedora2', 'descricao fornecedora 2', 'responsável pelo fornecedor: joão, tel 1111-1111', fornecedor2_endereco)
        
        def cria_loja_estoque(nome, descricao, contato, endereco):
            loja_estoque = LojaEstoque(nome = nome, descricao = descricao, contato = contato, endereco = endereco)
            loja_estoque.save()
            return loja_estoque
        loja_estoque1 = cria_loja_estoque('loja estoque 1', 'descricao estoque 1', 'responsável pela loja estoque: josé, tel 1111-1111', estoque1_endereco)
        loja_estoque2 = cria_loja_estoque('loja estoque 2', 'descricao estoque 2', 'responsável pela loja estoque: joão, tel 1111-1111', estoque2_endereco)
        
        def cria_banco_produto(categoria, marca, fornecedor, loja_estoque, nome, descricao, codigo, quantidade_estoque, valor_unitario_compra, valor_unitario_venda, data_compra_loja, aparecer_banner, aparecer_vitrini, tamanho, cor, tecido):
            banco_produto = BancoProduto(categoria = categoria, marca = marca, fornecedor = fornecedor, loja_estoque = loja_estoque, nome = nome, descricao = descricao, codigo = codigo, quantidade_estoque = quantidade_estoque, valor_unitario_compra = valor_unitario_compra, valor_unitario_venda = valor_unitario_venda, data_compra_loja = data_compra_loja, aparecer_banner = aparecer_banner, aparecer_vitrini = aparecer_vitrini, tamanho = tamanho, cor = cor, tecido = tecido)
            banco_produto.save()
            return banco_produto
        banco_produto1 = cria_banco_produto(categoria1_produto, marca1_produto, fornecedor1, loja_estoque1, 'Tenis Adidas Modelo 2011', 'O mais novo modelo de tenis da adidas', '#0001T', '0', '70.55', '90.99', '2011-01-01', True, False, 'M', 'Azul/Marrom' , 'Couro')
        banco_produto2 = cria_banco_produto(categoria2_produto, marca2_produto, fornecedor2, loja_estoque2, 'Camisa Puma Modelo 2011', 'A mais nova camisa do time X', '#0001C', '5', '40.55', '70.99', '2011-01-01', False, True, 'P', 'Vermelho' , '100% Algodão')
        
        # /PRODUTOS
        
        # OUTROS
        def cria_texto(titulo, texto, lugar):
            texto_pagina = TextoPagina(titulo = titulo, texto=texto, lugar = lugar)
            texto_pagina.save()
            return texto_pagina
        texto_home = cria_texto('Titulo vitrini', 'texto vitrini', 'vitrini')
        texto_minha_conta = cria_texto('Titulo minha_conta', 'minha_conta', 'minha_conta')
        texto_novidades = cria_texto('Titulo novidades', 'texto novidades', 'novidades')
        texto_institucional = cria_texto('Titulo Institucional', 'texto institucional', 'institucional')
        texto_contato = cria_texto('Titulo contato', 'texto contato', 'contato')
        texto_carrinho = cria_texto('Titulo carrinho ', 'texto carrinho', 'carrinho')
        
        def cria_novidade(titulo, texto, link_produto):
            novidade = Novidade(titulo = titulo, texto = texto, link_produto = link_produto)
            novidade.save()
            return novidade
        novidade1 = cria_novidade('Chegaram os novos tenis da adidas', 'Você que estava esperando, chegaram hoje os tenis da Adidas! Corra pegar o seu!', 'link_produto_noticia1')
        novidade2 = cria_novidade('Em breve camisetas do seu time!', 'Em breve camisetas do seu time! Dia XX/XX elas chegam na loja de Taguaí, não perca!', 'link_produto_noticia2')
        
        # /OUTROS