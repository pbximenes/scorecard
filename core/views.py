from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'base.html', locals())


def analistas(request):
    return render(request, 'analistas.html', locals())

def metas(request):
    return render(request, 'metas.html', locals())