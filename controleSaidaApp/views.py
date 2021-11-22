from django.shortcuts import render, redirect
from .models import pessoas_autorizadas, controle_saida
from .forms import controle_saida_form, pessoa_autorizada_form

# Create your views here.
def todas_saidas(request):
    saidas = controle_saida.objects.all()
    return render(request, 'todasSaidas.html', {'saidas': saidas,})

def adicionar_saida(request):
    saidas_form = controle_saida_form()
    if request.method == 'POST':
        saidas_form = controle_saida_form(request.POST)
        print(saidas_form)
        if saidas_form.is_valid():
            saidas_form.save()
            return redirect('todas_saidas')
    return render(request, 'adicionarSaida.html', {'saidas_form': saidas_form})

def deleta_saida(request, pk):
    saida_selecionada = controle_saida.objects.get(id = pk)
    saida_selecionada.delete()
    return redirect('todas_saidas')

def atualiza_saida(request, pk):
    saida_selecionada = controle_saida.objects.get(id = pk)
    saida_atualizar = controle_saida_form(instance=saida_selecionada)
    if request.method == 'POST':
        saida_atualizar = controle_saida_form(request.POST, instance = saida_selecionada)
        if saida_atualizar.is_valid():
            saida_atualizar.save()
            return redirect('todas_saidas')
    return render(request, 'atualizarSaida.html', {'saida': controle_saida, 'saida_atualizar': saida_atualizar})

def todas_pessoa_autorizada(request):
    pessoa_autorizada = pessoas_autorizadas.objects.all()
    return render(request, 'todasPessoasAutorizadas.html', {'pessoas_autorizadas': pessoa_autorizada,})

def adicionar_pessoa_autorizada(request):
    pessoas_autorizadas_form = pessoa_autorizada_form()
    if request.method == 'POST':
        pessoas_autorizadas_form = pessoa_autorizada_form(request.POST)
        print(pessoas_autorizadas_form.is_valid())
        if pessoas_autorizadas_form.is_valid():
            pessoas_autorizadas_form.save()
            return redirect('todas_pessoa_autorizada')
    return render(request, 'adicionarPessoaAutorizada.html', {'pessoas_autorizadas_form': pessoas_autorizadas_form})

def deleta_pessoa_autorizada(request, pk):
    pessoa_autorizada_selecionada = pessoas_autorizadas.objects.get(id = pk)
    pessoa_autorizada_selecionada.delete()
    return redirect('todas_pessoa_autorizada')

def atualiza_pessoa_autorizada(request, pk):
    pessoa_autorizada_selecionada = pessoas_autorizadas.objects.get(id = pk)
    pessoa_autorizada_atualizar = pessoa_autorizada_form(instance=pessoa_autorizada_selecionada)
    if request.method == 'POST':
        pessoa_autorizada_atualizar = pessoa_autorizada_form(request.POST, instance = pessoa_autorizada_selecionada)
        if pessoa_autorizada_atualizar.is_valid():
            pessoa_autorizada_atualizar.save()
            return redirect('todas_pessoa_autorizada')
    return render(request, 'atualizarPessoaAutorizada.html', {'pessoa_autorizada': pessoas_autorizadas, 'pessoa_autorizada_atualizar': pessoa_autorizada_atualizar})