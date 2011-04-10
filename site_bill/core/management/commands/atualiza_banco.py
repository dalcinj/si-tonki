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
        
        def cria_usuario(username, email, password):
            user = User.objects.create_user(username, email, password)
            return user
        
        user1 = cria_usuario('cliente1', 'jhonstondalcin@gmail.com', 'cliente1')
        user2 = cria_usuario('cliente2', 'jhonstondalcin@gmail.com', 'cliente2')
        
        
        def cria_cliente(user, nome, email, email2, telefone, celular, rg, cpf, data_nascimento):
            cliente = Cliente(user = user, email=email, email2=email2, nome = nome, telefone = telefone, rg = rg, cpf = cpf, data_nascimento = data_nascimento)
            cliente.save()
            return cliente
        
        cliente1 = cria_cliente(user1, 'Cliente1', 'jhonstondalcin@gmail.com', 'jhonstondalcin@gmail.com', '7272-3060', '7272-3060', '46.705.983-4', '383.747.188-89', '1990-09-19')
        cliente2 = cria_cliente(user2, 'Cliente2', 'jhonstondalcin@gmail.com', 'jhonstondalcin@gmail.com', '1234-5678', '7272-3060', '46.705.983-4', '383.747.188-89', '1990-09-19')