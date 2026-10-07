from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria
from .forms import CategoriaForm

def lista_categorias(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'categoria/lista.html', context)

def detalhe_categoria(request, id):
    categoria_obj = get_object_or_404(Categoria, id=id)
    noticias = categoria_obj.noticias.all()
    context = {'categoria': categoria_obj, 'noticias': noticias}
    return render(request, 'categoria/detalhe.html', context)

def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria:lista')
    else:
        form = CategoriaForm()
    context = {'form': form, 'titulo_pagina': 'Adicionar Categoria'}
    return render(request, 'categoria/form.html', context)