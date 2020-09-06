from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from .models import TablonEjercicios

# Create your views here.
def index(request):
    return render(request,'cargadatos/index.html')

#def lista_tablon(request):
  #  tablon= TablonEjercicios.objects.all()
  #  contexto= {'tablon':tablon}
  #  return render(request,'cargadatos/TablonEjercicios.html',contexto)

class lista_tablon(ListView):
    model = TablonEjercicios
    template_name = 'cargadatos/TablonEjercicios.html'


