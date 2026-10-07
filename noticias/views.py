from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia
from .forms import NoticiaForm

def lista_noticias(request):
    noticias = Noticia.objects.all()
    context = {'noticias': noticias}
    return render(request, 'noticias/lista.html', context)

def detalhe_noticia(request, id):
    noticia_obj = get_object_or_404(Noticia, id=id)
    context = {'noticia': noticia_obj}
    return render(request, 'noticias/detalhe.html', context)

def criar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noticias:lista')
    else:
        form = NoticiaForm()
    context = {'form': form, 'titulo_pagina': 'Adicionar Notícia'}
    return render(request, 'noticias/form.html', context)