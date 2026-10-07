from django.shortcuts import render
from noticias.models import Noticia

def home(request):
    noticias_recentes = Noticia.objects.all().order_by('-data_publicacao')[:5]
    context = {
        'noticias': noticias_recentes
    }
    return render(request, 'core/home.html', context)