from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return HttpResponse("Contatos :D")


def sobre(request):
    return HttpResponse('sobre')
