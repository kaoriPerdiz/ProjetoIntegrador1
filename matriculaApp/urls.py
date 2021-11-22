from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.todas_matriculas, name='todas_matriculas'),
    path('adicionar_matricula', views.adicionar_matricula, name='adicionar_matriculas'),
    path('deleta_matricula/<int:pk>', views.deleta_matricula, name='deleta_matricula'),
    path('atualiza_matricula/<int:pk>', views.atualiza_matricula, name='atualiza_matricula'),
]