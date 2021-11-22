from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('todas_saidas', views.todas_saidas, name='todas_saidas'),
    path('adicionar_saida', views.adicionar_saida, name='adicionar_saida'),
    path('atualiza_saida/<int:pk>', views.atualiza_saida, name='atualiza_saida'),
    path('deleta_saida/<int:pk>', views.deleta_saida, name='deleta_saida'),
    path('adicionar_pessoa_autorizada', views.adicionar_pessoa_autorizada, name='adicionar_pessoa_autorizada'),
    path('todas_pessoa_autorizada', views.todas_pessoa_autorizada, name='todas_pessoa_autorizada'),
    path('atualiza_pessoa_autorizada/<int:pk>', views.atualiza_pessoa_autorizada, name='atualiza_pessoa_autorizada'),
    path('deleta_pessoa_autorizada/<int:pk>', views.deleta_pessoa_autorizada, name='deleta_pessoa_autorizada'),
]