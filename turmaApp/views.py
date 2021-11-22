from django.shortcuts import render, redirect
from .models import turma
from .forms import turma_form

# Create your views here.
def todas_turmas(request):
    turmas = turma.objects.all()
    return render(request, 'todasTurmas.html', {'turmas': turmas})

def adicionar_turma(request):
    turmas_form = turma_form()
    if request.method == 'POST':
        turmas_form = turma_form(request.POST)
        print(turmas_form.is_valid())
        if turmas_form.is_valid():
            turmas_form.save()
            return redirect('todas_turmas')
    return render(request, 'adicionarTurma.html', {'turmas_form': turmas_form})

def atualiza_turma(request, pk):
    turma_selecionada = turma.objects.get(id = pk)
    turma_atualizar = turma_form(instance=turma_selecionada)
    if request.method == 'POST':
        turma_atualizar = turma_form(request.POST, instance = turma_selecionada)
        if turma_atualizar.is_valid():
            turma_atualizar.save()
            return redirect('todas_turmas')
    return render(request, 'atualizarTurma.html', {'turma': turma, 'turma_atualizar': turma_atualizar})

def deleta_turma(request, pk):
    turma_selecionada = turma.objects.get(id = pk)
    turma_selecionada.delete()
    return redirect('todas_turmas')

def adicionar_crianca_turma(request):
    if request.method == 'POST':
        turmas_form = turma_form(request.POST)
        print(turmas_form.is_valid())
        if turmas_form.is_valid():
            turmas_form.save()
            return redirect('todas_turmas')
    return render(request, 'adicionarAlunoTurma.html', {'turmas_form': turmas_form})