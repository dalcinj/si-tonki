# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
prefixo = settings.PREFIXO
# Create your models here.

# CLIENTE
class Cliente(models.Model):
    user = models.ForeignKey(User, unique=True)
    endereco = models.ManyToManyField('Endereco', verbose_name="Endereço", null=True, blank=True)
    nome = models.CharField(max_length=128)
    email = models.EmailField(verbose_name="E-mail")
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
    nome = models.CharField(max_length=128, verbose_name="Nome do Produto")
    descricao = models.TextField(verbose_name="Descrição do Produto")
    codigo = models.CharField(max_length=128, verbose_name="Código do Produto")
    quantidade_estoque = models.IntegerField(default = 0, verbose_name="Quantidade no Estoque")
    valor_unitario_compra = models.FloatField(verbose_name="Valor Unitário de Compra")
    valor_unitario_venda = models.FloatField(verbose_name="Valor Unitário de Venda")
    data_compra_loja = models.DateField(verbose_name="Quando o produto foi comprado e estocado?")
    aparecer_banner = models.BooleanField(default= False, verbose_name="Mostrar no topo das páginas?")
    aparecer_vitrini = models.BooleanField(default= False, verbose_name="Mostrar na vitrini da Home?")
    tamanho = models.CharField(max_length=256, null=True, blank=True, verbose_name="Tamanho")
    cor = models.CharField(max_length=256, null=True, blank=True, verbose_name="Cor")
    tecido = models.CharField(max_length=256, null=True, blank=True, verbose_name="Tipo de Tecido")
    foto1 = models.FileField(upload_to=prefixo+'/static/fotos',null=True, default="default.png")
    foto2 = models.FileField(upload_to=prefixo+'/static/fotos',null=True, default="default.png")
    foto3 = models.FileField(upload_to=prefixo+'/static/fotos',null=True, default="default.png")
    
    def __unicode__(self):
        return self.nome
    
    @classmethod
    def pega_prod_cat(cls, categoria):
        try:
            lista_prod_cat = BancoProduto.objects.filter(categoria = categoria)
        except:
            lista_prod_cat = None
        return lista_prod_cat
    
    @classmethod
    def pega_prod_marca(cls, marca):
        try:
            lista_prod_marca = BancoProduto.objects.filter(marca = marca)
        except:
            lista_prod_marca = None
        return lista_prod_marca
    
    @classmethod
    def pega_prod_id(cls, id_produto):
        try:
            produto = BancoProduto.objects.get(pk = id_produto)
        except:
            produto = None
        return produto
    
class CategoriaProduto(models.Model):
    categoria = models.CharField(max_length=256, verbose_name="Categoria")
    descricao = models.CharField(max_length=256, verbose_name="Descrição da Categoria")
    
    def __unicode__(self):
        return self.categoria
    
    @classmethod
    def pega_gategoria_id(cls, id_categoria):
        try:
            categoria = CategoriaProduto.objects.get(pk = id_categoria)
        except:
            categoria = None
        return categoria
    
class MarcaProduto(models.Model):
    marca = models.CharField(max_length=256, verbose_name="Marca")
    descricao = models.CharField(max_length=256, verbose_name="Descrição da Marca")
    
    def __unicode__(self):
        return self.marca
    
    @classmethod
    def pega_marca_id(cls, id_marca):
        try:
            marca = MarcaProduto.objects.get(pk = id_marca)
        except:
            marca = None
        return marca
    
class Fornecedor(models.Model):
    endereco = models.ManyToManyField('Endereco', verbose_name="Endereço do Fornecedor", null=True, blank=True)
    nome = models.CharField(max_length=256, verbose_name="Nome do Fornecedor")
    descricao = models.CharField(max_length=256, verbose_name="Descrição o Fornecedor")
    contato = models.TextField(verbose_name="Contato Fornecedor")    
    
    def __unicode__(self):
        return self.nome
    
class LojaEstoque(models.Model):
    endereco = models.ManyToManyField('Endereco', verbose_name="Endereço da Loja", null=True, blank=True)
    nome = models.CharField(max_length=128, verbose_name="Nome da Loja de Estoque/Venda")
    descricao = models.CharField(max_length=256, verbose_name="Descrição da Loja")
    contato = models.TextField(verbose_name="Contato da Loja")    
    
    def __unicode__(self):
        return self.nome
    
# /PRODUTO

#CARRINHO
class Carrinho(models.Model):
    cliente = models.OneToOneField('Cliente')
    data_compra = models.DateField(verbose_name="Quando a compra foi efetuada?", null=True, blank=True)
    valor_total = models.FloatField(verbose_name="Valor Total da Compra", default=0)
    concluido = models.BooleanField()
    
    @classmethod
    def pega_carrinho_atual(cls, cliente):
        return Carrinho.objects.filter(cliente=cliente).get(concluido=False)
        

class ProdutoCarrinho(models.Model):
    carrinho = models.ForeignKey('Carrinho')
    produto = models.ForeignKey('BancoProduto')
    quantidade = models.IntegerField()
    valor_total = models.FloatField()

class POSCarrinho(models.Model):
    cliente = models.OneToOneField('Cliente')
    carrinho = models.ForeignKey('Carrinho')

# /CARRINHO
    
class Endereco(models.Model):
    rua = models.CharField(max_length=128)
    num = models.CharField(max_length=128, verbose_name="Número")
    complemento = models.CharField(max_length=128, null=True, blank=True)
    bairro = models.CharField(max_length=128)
    cidade = models.CharField(max_length=128)
    estado = models.CharField(max_length=128)
    cep = models.CharField(max_length=128, verbose_name="CEP")
    
    def __unicode__(self):
        return self.cep
    
    @classmethod
    def pega_endereco_id(cls, id_endereco):
        try:
            endereco = Endereco.objects.get(id=id_endereco)
        except:
            endereco = None
        return endereco

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
    foto = models.FileField(upload_to=prefixo+'/static/fotos',null=True, default="default.png")
    lugar = models.CharField(max_length=256, unique=True, verbose_name="Qual página aparece?")
    
    def __unicode__(self):
        return self.lugar
    
    @classmethod
    def pega_texto_lugar(cls, lugar):
        try:
            texto = TextoPagina.objects.get(lugar = lugar)
        except:
            texto = None
        return texto
    
class Novidade(models.Model):
    titulo = models.CharField(max_length=256, verbose_name="Título da Novidade")
    texto = models.TextField(verbose_name="Texto da Novidade")
    foto = models.FileField(upload_to=prefixo+'/static/fotos', null=True, blank=True, default="default.jpg")
    link_produto = models.CharField(max_length=256, verbose_name="Link para o novo produto")
    
    def __unicode__(self):
        return self.titulo
    
class Contato(models.Model):
    
    assunto_choice =(
    ('duvida','Dúvida'),
    ('sugestao','Sugestão'),
    ('reclamacao','Reclamação'),
    ('pedido','Pedido de Produto'),
    )
    
    nome = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    telefone = models.CharField(max_length=128, null=True, blank=True)
    texto = models.TextField(verbose_name="Comentário")
    assunto = models.CharField(max_length=256, verbose_name="Assunto", choices=assunto_choice)
    
    def __unicode__(self):
        return self.assunto
        
# /OUTROS