from django.shortcuts import render
from .models import Analista, Meta


# Create your views here.
def home(request):
    return render(request, 'base.html', locals())


def analistas(request):
    analistas = Analista.objects.all()
    return render(request, 'analistas.html', locals())

def metas(request):
    return render(request, 'metas.html', locals())


def avaliacao(request, userId):
    analista = Analista.objects.get(pk=userId)
    metas = Meta.objects.all()
    return render(request, 'avaliacao.html', locals())