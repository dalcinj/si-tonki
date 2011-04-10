from site_bill.sistema.models import *

def context_principal(request):
    if request.user.is_authenticated():
        usuario_logado = request.user
        try:
            cliente = usuario_logado.get_profile()
        except:
            pass
    return locals()

