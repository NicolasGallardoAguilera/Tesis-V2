from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TablonEjercicios,Lista,Ejercicios

# Create your views here.
def index(request):
    return render(request,'cargadatos/index.html')


class lista_tablon(ListView):
    model = TablonEjercicios
    template_name = 'cargadatos/TablonEjercicios.html'

 
class vista_lista(LoginRequiredMixin,ListView):
    model= Lista
    queryset= Lista.objects.filter(nrc=2020)
    template_name = 'cargadatos/vista_lista.html'

class vista_ejercicios_alumnos(LoginRequiredMixin,ListView):
    model= TablonEjercicios
    queryset= TablonEjercicios.objects.filter(UsuarioUnab='nico')
    template_name = 'cargadatos/vista_ejercicios_alumnos.html'

class listado_ejercicios(LoginRequiredMixin,  ListView):
    model= Ejercicios
    template_name = 'cargadatos/listado_ejercicios.html'

class vista_grafico(TemplateView):
    template_name = 'cargadatos/grafico.html'


