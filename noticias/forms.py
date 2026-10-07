from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'texto', 'categoria', 'tags']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da notícia'}),
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Conteúdo da notícia...'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }