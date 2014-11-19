#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http.response import HttpResponse
from vigilante.models import Evento, TIPOS_DE_EVENTOS
import json

# Create your views here.
def home(req):
    valores = { # Valores a renderizar na página
        'tipos': TIPOS_DE_EVENTOS}
    return render_to_response('home.html',
        valores,
        context_instance=RequestContext(req))

def get_eventos_json(req, tipo):
    '''Retorna uma coleção de Eventos transformados em JSON para plotar no mapa.'''
    qs = Evento.objects # Objeto QuerySet dos Eventos
    print(req.GET)
    eventos = [] # Lista de eventos a ser enviada
    dados = {}   # Dicionário a ser convertido em JSON
    for e in Evento.objects.all():
        obj = {
            # Pode adicionar outros campos aqui
            'lat' : e.lat,
            'lng' : e.lng,
        }
        eventos.append(obj)
    dados['eventos'] = eventos
    return HttpResponse(json.dumps(dados))
