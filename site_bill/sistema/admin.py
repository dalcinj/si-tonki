from site_bill.sistema.models import *
from django.contrib import admin
#try:
#    import Image
#except ImportError:
#    from PIL import Image

from django import forms
from forms import *

#class ProdutoInline(admin.StackedInline):
#    model = BancoProduto
#    exclude = ['prova']
#    fieldsets = [
#        (None,               {'fields': ['codigo']}),
#        ('Dados', {'fields': [('nome','descricao'),('categoria','marca'),('loja_estoque','fornecedor'),('quantidade','valor_unitario_compra', 'valor_unitario_venda')], 'classes': ['collapse']}),
#    ]
#    extra = 1
#
#class CategoriaInline(admin.TabularInline):
#    model = CategoriaProduto
#    extra = 1
#
#class MarcaInline(admin.StackedInline):
#    model = MarcaProduto
#    extra = 1
#    
#class FornecedorInline(admin.StackedInline):
#    model = Fornecedor
#    extra = 1
#
#class LojaEstoqueInline(admin.StackedInline):
#    model = LojaEstoque
#    extra = 1
    
class EspecificacaoInline(admin.StackedInline):
    model = EspecificacaoProduto
    
class EnderecoInline(admin.StackedInline):
    model = Endereco
    extra = 1

#customizando admin

class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['cpf', 'nome']
    list_display = ('cpf', 'nome')
    #inlines = [EnderecoInline]
    actions = ['delete_selected']
    exclude = ['endereco']
    
class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'nome', 'categoria', 'marca', 'fornecedor']
    list_filter = ['marca', 'categoria']
    list_display = ('codigo', 'nome', 'categoria', 'marca', 'fornecedor', 'quantidade_estoque')
    #inlines = [EspecificacaoInline]
    actions = ['delete_selected']
    exclude = ['especificacao']
    
class FornecedorAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao')
    #inlines = [EnderecoInline]
    actions = ['delete_selected']
    exclude = ['endereco']
    
class LojaEstoqueAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_display = ('nome', 'descricao')
    #inlines = [EnderecoInline]
    actions = ['delete_selected']
    exclude = ['endereco']


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(BancoProduto, ProdutoAdmin)
admin.site.register(CategoriaProduto)
admin.site.register(MarcaProduto)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(LojaEstoque, LojaEstoqueAdmin)
admin.site.register(TextoPagina)
admin.site.register(Novidade)
admin.site.register(Contato)
#admin.site.register(EspecificacaoProduto)
#admin.site.register(Endereco)

