
from django.shortcuts import render

def index(request):
    return render(request, 'atendimento/index.html')

def cadastro(request):
    return render(request, 'atendimento/cadastro.html')

def fila(request):
    return render(request, 'atendimento/fila.html')

def banco(request):
    return render(request, 'atendimento/banco.html')
