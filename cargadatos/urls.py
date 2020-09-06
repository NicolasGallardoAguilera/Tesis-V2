from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from cargadatos.views import index, lista_tablon


urlpatterns = [
    url('^$',index),
    #url('lista/', lista_tablon),
    url('lista/', lista_tablon.as_view()),
]
