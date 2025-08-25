from django.shortcuts import render, redirect,get_object_or_404
from .forms import UploadForm
from .models import Carrinho, ItemCarrinho, Produto, Pedido, ItemPedido, Perfil
from .ProcessarArquivo import ProcessarPDF
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from PyPDF2.errors import PdfReadError



# Renderiza a página inicial do site
def index(request):
    return render(request, 'index.html')


@login_required
def impressao(request):
    url_arquivo = f"/media/temp/livro.pdf"

    return render(request, 'impressao.html', {
     
        'url_arquivo': url_arquivo,
    })

def pagamento(request):
    return render(request, 'pagamento.html')

# Renderiza a Pagina Quem Somos
def quemsomos(request):
    return render(request, 'quemsomos.html')



