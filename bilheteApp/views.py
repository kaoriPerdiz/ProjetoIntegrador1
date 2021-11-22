from django.shortcuts import render, redirect
from .models import bilhete
from .forms import bilhete_form

# Create your views here.
def todos_bilhete(request):
    bilhetes = bilhete.objects.all()
    return render(request, 'todosbilhete.html', {'bilhetes': bilhetes})

def adicionar_bilhete(request):
    bilhetes_form = bilhete_form()
    if request.method == 'POST':
        bilhetes_form = bilhete_form(request.POST)
        print(bilhetes_form.is_valid())
        if bilhetes_form.is_valid():
            bilhetes_form.save()
            return redirect('todos_bilhete')
    return render(request, 'adicionarBilhete.html', {'bilhete_form': bilhetes_form})

def deleta_bilhete(request, pk):
    bilhete_selecionado = bilhete.objects.get(id = pk)
    bilhete_selecionado.delete()
    return redirect('todos_bilhete')

def atualiza_bilhete(request, pk):
    bilhete_selecionado = bilhete.objects.get(id = pk)
    bilhete_atualizar = bilhete_form(instance=bilhete_selecionado)
    if request.method == 'POST':
        bilhete_atualizar = bilhete_form(request.POST, instance = bilhete_selecionado)
        if bilhete_atualizar.is_valid():
            bilhete_atualizar.save()
            return redirect('todos_bilhete')
    return render(request, 'atualizarBilhete.html', {'bilhete': bilhete, 'bilhete_atualizar': bilhete_atualizar})