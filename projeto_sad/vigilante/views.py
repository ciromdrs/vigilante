#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from vigilante.util import get_lat_lng
from django.http.response import HttpResponse
from vigilante.models import Evento
import json

# Create your views here.
def home(req):
    valores = {}
    if req.method == 'POST':
        # Marcando ponto
        endereco = req.POST['endereco']
        valores['p'] = get_lat_lng(endereco)
    return render_to_response('home.html',
        valores,
        context_instance=RequestContext(req))

def get_eventos_json(req):
    '''Retorna uma coleção de Eventos transformados em JSON para plotar no mapa.
        (É possível passar parâmetros para o método json.dumps através dos *args
        e **kwds)'''
    #if req.is_ajax():
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
