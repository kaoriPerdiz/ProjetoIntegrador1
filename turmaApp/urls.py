from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.todas_turmas, name='todas_turmas'),
    path('adicionar_turma', views.adicionar_turma, name='adicionar_turma'),
    path('atualiza_turma/<int:pk>', views.atualiza_turma, name='atualiza_turma'),
    path('deleta_turma/<int:pk>', views.deleta_turma, name='deleta_turma'),
    path('adicionar_crianca_turma', views.adicionar_crianca_turma, name='adicionar_crianca_turma')
]