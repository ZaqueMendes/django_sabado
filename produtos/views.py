from django.shortcuts import render
from django.http import HttpResponse

def ver_produto(request):
  return HttpResponse('Olá, tudo bem?') 