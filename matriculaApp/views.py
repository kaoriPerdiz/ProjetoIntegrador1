from django.shortcuts import redirect, render
from .models import matricula
from .forms import matricula_form
from turmaApp.models import turma

# Create your views here.
def todas_matriculas(request):
    matriculas = matricula.objects.all()
    return render(request, 'todasMatriculas.html', {'matriculas': matriculas})

def adicionar_matricula(request):
    matriculas_form = matricula_form()
    turmas = turma.objects.all()
    if request.method == 'POST':
        matriculas_form = matricula_form(request.POST)
        print(matriculas_form.is_valid())
        if matriculas_form.is_valid():
            matriculas_form.save()
            return redirect('todas_matriculas')
    return render(request, 'adicionarMatricula.html', {'matriculas_form': matriculas_form, 'turmas': turmas})

def deleta_matricula(request, pk):
    matricula_selecionada = matricula.objects.get(id = pk)
    matricula_selecionada.delete()
    return redirect('todas_matriculas')

def atualiza_matricula(request, pk):
    matricula_selecionada = matricula.objects.get(id = pk)
    matricula_atualizar = matricula_form(instance=matricula_selecionada)
    if request.method == 'POST':
        matricula_atualizar = matricula_form(request.POST, instance = matricula_selecionada)
        if matricula_atualizar.is_valid():
            matricula_atualizar.save()
            return redirect('todas_matriculas')
    return render(request, 'atualizarMatricula.html', {'matricula': matricula, 'matricula_atualizar': matricula_atualizar})