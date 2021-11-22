from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.todos_bilhete, name='todos_bilhete'),
    path('adicionar_bilhete', views.adicionar_bilhete, name='adicionar_bilhete'),
    path('atualiza_bilhete/<int:pk>', views.atualiza_bilhete, name='atualiza_bilhete'),
    path('deleta_bilhete/<int:pk>', views.deleta_bilhete, name='deleta_bilhete'),
]