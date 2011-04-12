# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
prefixo = settings.PREFIXO
# Create your models here.

# CLIENTE
class Cliente(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    endereco = models.ForeignKey('Endereco', verbose_name="Endereço", null=True, blank=True)
    nome = models.CharField(max_length=128)
    email = models.EmailField(verbose_name="E-mail Principal")
    email2 = models.EmailField(verbose_name="E-mail Secundário",null=True, blank=True)
    data_nascimento = models.DateField(verbose_name="Data de nascimento", null=True, blank=True)
    telefone = models.CharField(max_length=128, null=True, blank=True)
    celular = models.CharField(max_length=128, null=True, blank=True)
    rg = models.CharField(max_length=128,verbose_name="RG", null=True, blank=True)
    cpf = models.CharField(max_length=128,verbose_name="CPF")
    
    def __unicode__(self):
        return self.nome
    
# /CLIENTE

# PRODUTO
class BancoProduto(models.Model):
    categoria = models.ForeignKey('CategoriaProduto')
    marca = models.ForeignKey('MarcaProduto')
    fornecedor = models.ForeignKey('Fornecedor', verbose_name="Fornecedor")
    loja_estoque = models.ForeignKey('LojaEstoque', verbose_name="Loja que está estocado")
    especificacao = models.OneToOneField('EspecificacaoProduto', verbose_name="Especificações do Produto")
    nome = models.CharField(max_length=128, verbose_name="Nome do Produto")
    descricao = models.TextField(verbose_name="Descrição do Produto")
    codigo = models.CharField(max_length=128, verbose_name="Código do Produto")
    quantidade_estoque = models.IntegerField(default = 0)
    valor_unitario_compra = models.FloatField(verbose_name="Valor Unitário de Compra")
    valor_unitario_venda = models.FloatField(verbose_name="Valor Unitário de Venda")
    data_compra_loja = models.DateField(verbose_name="Quando o produto foi comprado e estocado?")
    aparecer_banner = models.BooleanField(default= False, verbose_name="Mostrar no topo da Home?")
    aparecer_vitrini = models.BooleanField(default= False, verbose_name="Mostrar na vitrini da Home?")
    foto1 = models.FileField(upload_to=prefixo+'/static/fotos',null=True, default="default.png")
    foto2 = models.FileField(upload_to=prefixo+'/static/fotos',null=True, default="default.png")
    foto3 = models.FileField(upload_to=prefixo+'/static/fotos',null=True, default="default.png")
    
    def __unicode__(self):
        return self.nome
    
class CategoriaProduto(models.Model):
    categoria = models.CharField(max_length=256, verbose_name="Categoria")
    descricao = models.CharField(max_length=256, verbose_name="Descrição da Categoria")
    
    def __unicode__(self):
        return self.categoria
    
class MarcaProduto(models.Model):
    marca = models.CharField(max_length=256, verbose_name="Marca")
    descricao = models.CharField(max_length=256, verbose_name="Descrição da Marca")
    
    def __unicode__(self):
        return self.marca
    
class Fornecedor(models.Model):
    endereco = models.ForeignKey('Endereco', verbose_name="Endereço do Fornecedor", null=True, blank=True)
    nome = models.CharField(max_length=256, verbose_name="Nome do Fornecedor")
    descricao = models.CharField(max_length=256, verbose_name="Descrição o Fornecedor")
    contato = models.TextField(verbose_name="Contato Fornecedor")    
    
    def __unicode__(self):
        return self.nome
    
class LojaEstoque(models.Model):
    endereco = models.ForeignKey('Endereco', verbose_name="Endereço da Loja", null=True, blank=True)
    nome = models.CharField(max_length=128, verbose_name="Nome da Loja de Estoque/Venda")
    descricao = models.CharField(max_length=256, verbose_name="Descrição da Loja")
    contato = models.TextField(verbose_name="Contato da Loja")    
    
    def __unicode__(self):
        return self.nome
    
class EspecificacaoProduto(models.Model):
    tamanho = models.CharField(max_length=256, null=True, blank=True, verbose_name="Tamanho")
    cor = models.CharField(max_length=256, null=True, blank=True, verbose_name="Cor")
    tecido = models.CharField(max_length=256, null=True, blank=True, verbose_name="Tipo de Tecido")
    
    def __unicode__(self):
        return self.tamanho
    
# /PRODUTO

#class Carrinho(models.Model):
#    cliente = models.OneToOneField('Cliente')
#    produtos = models.ForeignKey('BancoProduto')
    
class Endereco(models.Model):
    rua = models.CharField(max_length=128)
    num = models.CharField(max_length=128, verbose_name="Número")
    complemento = models.CharField(max_length=128, null=True, blank=True)
    bairro = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    estado = models.CharField(max_length=128)
    cep = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.cep    

# PAGAMENTOS   
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
# /PAGAMENTOS

# OUTROS
    
class TextoPagina(models.Model):
    titulo = models.CharField(max_length=256, verbose_name="Título da Página")
    texto = models.TextField(verbose_name="Texto da Página")
    
class Novidade(models.Model):
    titulo = models.CharField(max_length=256, verbose_name="Título da Novidade")
    texto = models.TextField(verbose_name="Texto da Novidade")
    foto = models.FileField(upload_to=prefixo+'/static/fotos',null=True, default="default.jpg")
    link_produto = models.CharField(max_length=256, verbose_name="Link para o novo produto")
    
class Contato(models.Model):
    
    assunto_choice =(
    ('duvida','Dúvida'),
    ('sugestao','Sugestão'),
    ('reclamacao','Reclamação'),
    ('pedido','Pedido de Produto'),
    ('conselheiro', 'Conselheiro'),
    ('ex_membro', 'Ex-membro'),
    )
    
    nome = models.CharField(max_length=128)
    email = models.EmailField(verbose_name="E-mail")
    telefone = models.CharField(max_length=128, null=True, blank=True)
    texto = models.TextField(verbose_name="Comentário")
    assunto = models.CharField(max_length=256, verbose_name="Assunto", choices=assunto_choice)
        
# /OUTROS