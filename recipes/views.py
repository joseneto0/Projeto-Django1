from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Home :D')


def contato(request):
    return HttpResponse("Contatos :D")


def sobre(request):
    return HttpResponse('sobre')