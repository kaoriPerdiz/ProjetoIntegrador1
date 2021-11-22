from django.shortcuts import render

from .models import frequencia
from .forms import frequencia_form
from matriculaApp.models import matricula

# Create your views here.
def ver_frequencia(request, fk):
    aluno_selecionado = matricula.objects.get(id = fk)
    frequencia_atual = frequencia.objects.get(crianca = aluno_selecionado)
    return render(request, 'frequenciaMensal.html', {'frequencia': frequencia_atual})

def adicionar_frequencia(request):
    frequencia = frequencia_form()
    criancas = matricula.objects.all().order_by('nome_crianca')
    if request.method == 'POST':
        frequencia = frequencia_form(request.POST)
        if frequencia.is_valid():
            frequencia.save()
    return render(request, 'adicionar_frequencia.html', {'frequencia_form': frequencia, 'criancas': criancas})