from django.urls import path
from . import views

app_name = 'categoria'

urlpatterns = [
    path('', views.lista_categorias, name='lista'),
    path('nova/', views.criar_categoria, name='criar'),
    path('<int:id>/', views.detalhe_categoria, name='detalhe'),
]