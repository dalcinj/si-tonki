from site_bill.sistema.models import *

def context_principal(request):
    if request.user.is_authenticated():
        usuario_logado = request.user
        try:
            cliente = usuario_logado.get_profile()
        except:
            pass
    lista_produtos_banner = BancoProduto.objects.filter(aparecer_banner=True)
    return locals()

