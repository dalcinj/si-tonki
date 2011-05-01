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
    
class EnderecoClienteInline(admin.StackedInline):
    model = Cliente.endereco.through
    #fields = ['rua', 'num', 'complemento', 'bairro', 'cidade', 'estado', 'cep']
    extra = 0

#customizando admin
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['cpf', 'nome']
    list_display = ('cpf', 'nome')
    inlines = [EnderecoClienteInline]
    actions = ['delete_selected']
    exclude = ['endereco']
    
class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'nome', 'categoria', 'marca', 'fornecedor']
    list_filter = ['marca', 'categoria']
    list_display = ('codigo', 'nome', 'categoria', 'marca', 'fornecedor', 'quantidade_estoque')
    actions = ['delete_selected']
    
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

class ContatoAdmin(admin.ModelAdmin):
    search_fields = ['assunto']
    list_filter = ['assunto']
    list_display = ('nome', 'assunto', 'texto')
    actions = ['delete_selected']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(BancoProduto, ProdutoAdmin)
admin.site.register(CategoriaProduto)
admin.site.register(MarcaProduto)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(LojaEstoque, LojaEstoqueAdmin)
admin.site.register(TextoPagina)
admin.site.register(Novidade)
admin.site.register(Contato, ContatoAdmin)
#admin.site.register(Endereco)

