from django.urls import path
from . import views

app_name = 'tag'

urlpatterns = [
    path('', views.lista_tags, name='lista'),
    path('nova/', views.criar_tag, name='criar'),
    path('<int:id>/', views.detalhe_tag, name='detalhe'),
]