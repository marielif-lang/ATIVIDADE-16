from django.shortcuts import render, get_object_or_404, redirect
from .models import Tag
from .forms import TagForm

def lista_tags(request):
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render(request, 'tag/lista.html', context)

def detalhe_tag(request, id):
    tag_obj = get_object_or_404(Tag, id=id)
    noticias = tag_obj.noticias.all()
    context = {'tag': tag_obj, 'noticias': noticias}
    return render(request, 'tag/detalhe.html', context)

def criar_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag:lista')
    else:
        form = TagForm()
    context = {'form': form, 'titulo_pagina': 'Adicionar Tag'}
    return render(request, 'tag/form.html', context)