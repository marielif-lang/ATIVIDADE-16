from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path('', views.lista_noticias, name='lista'),
    path('nova/', views.criar_noticia, name='criar'),
    path('<int:id>/', views.detalhe_noticia, name='detalhe'),
]