from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('categorias/', include('categoria.urls')),
    path('tags/', include('tag.urls')),
    path('noticias/', include('noticias.urls')),
]