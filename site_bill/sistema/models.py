# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# CLIENTE
class Cliente(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    nome = models.CharField(max_length=128)
    email = models.EmailField(verbose_name="E-mail Principal")
    email2 = models.EmailField(verbose_name="E-mail Secundário",null=True, blank=True)
    data_nascimento = models.DateField(verbose_name="Data de nascimento", null=True, blank=True)
    endereco = models.ForeignKey('EnderecoCliente', verbose_name="Endereço", null=True, blank=True)
    telefone = models.CharField(max_length=128, null=True, blank=True)
    celular = models.CharField(max_length=128, null=True, blank=True)
    rg = models.CharField(max_length=128,verbose_name="RG", null=True, blank=True)
    cpf = models.CharField(max_length=128,verbose_name="CPF", null=True, blank=True)
    
    def __unicode__(self):
        return self.nome
    
class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=128)
    num = models.CharField(max_length=128, verbose_name="Número")
    complemento = models.CharField(max_length=128, null=True, blank=True)
    bairro = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    estado = models.CharField(max_length=128)
    cep = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.cep
    
# /CLIENTE

# PRODUTO
class Produto(models.Model):
    tipo = models.ForeignKey('TipoProduto')
    nome = models.CharField(max_length=128, verbose_name="Nome do Produto")
    descricao = models.CharField(max_length=256, verbose_name="Descrição do Produto")
    codigo = models.CharField(max_length=128, verbose_name="Código do Produto")
    quantidade_estoque = models.IntegerField()
    valor_unitario_compra = models.FloatField(verbose_name="Valor Unitário de Compra")
    valor_unitario_venda = models.FloatField(verbose_name="Valor Unitário de Venda")
    local_compra = models.ForeignKey('LocalCompra', verbose_name="Local da compra")
    loja_estoque = models.ForeignKey('LojaEstoque', verbose_name="Loja que está estocado")
    data_compra = models.DateField()
    
    def __unicode__(self):
        return self.nome
    
class TipoProduto(models.Model):
    tipo = models.CharField(max_length=128, verbose_name="Tipo")
    descricao = models.CharField(max_length=256, verbose_name="Descrição")
    
    def __unicode__(self):
        return self.tipo
    
class LocalCompra(models.Model):
    nome = models.CharField(max_length=128, verbose_name="Nome do Local")
    descricao = models.CharField(max_length=256, verbose_name="Descrição do Local")
    contato = models.CharField(max_length=128, verbose_name="Contato do Local")
    endereco = models.ForeignKey('EnderecoProduto', verbose_name="Endereço do Fornecedor", null=True, blank=True)
    
    def __unicode__(self):
        return self.nome
    
class LojaEstoque(models.Model):
    nome = models.CharField(max_length=128, verbose_name="Nome do Loja")
    descricao = models.CharField(max_length=256, verbose_name="Descrição do Loja")
    contato = models.CharField(max_length=128, verbose_name="Contato do Loja")
    endereco = models.ForeignKey('EnderecoProduto', verbose_name="Endereço da Loja", null=True, blank=True)
    
    def __unicode__(self):
        return self.nome
    
class EnderecoProduto(models.Model):
    rua = models.CharField(max_length=128)
    num = models.CharField(max_length=128, verbose_name="Número")
    complemento = models.CharField(max_length=128, null=True, blank=True)
    bairro = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    estado = models.CharField(max_length=128)
    cep = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.cep
    
# /PRODUTO
    
#class Pagamento(models.Model):
#    cliente = models.ForeignKey(Cliente)
#    valor = models.FloatField()
#    data = models.DateField()
#    
#class Boleto(models.Model):
#    pagamento = models.ForeignKey(Pagamento)
#    
#class Divida(models.Model):
#    cliente = models.ForeignKey(Cliente)
#    valor = models.FloatField()
#    data_cobranca = models.DateField()