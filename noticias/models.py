from django.db import models
from django.contrib.auth.models import User
from categoria.models import Categoria
from tag.models import Tag

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias')
    tags = models.ManyToManyField(Tag, related_name='noticias')

    def __str__(self):
        return self.titulo

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"