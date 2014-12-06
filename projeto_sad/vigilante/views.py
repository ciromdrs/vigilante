#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http.response import HttpResponse
from vigilante.models import Evento, TIPOS_DE_EVENTOS
from datetime import datetime

import json

# Create your views here.
def home(req):
    '''Renderiza a página inicial.'''
    valores = { # Valores a renderizar na página
        'tipos': TIPOS_DE_EVENTOS}
    return render_to_response('home.html',
        valores,
        context_instance=RequestContext(req))

def get_eventos_json(req, query):
    '''Pega uma coleção de Eventos e transforma em JSON para plotar no mapa.
    :param query:
        Filtros da consulta.
    :returns:
        HttpResponse contendo dados JSON com um vetor chamado "eventos" contendo
        os dados (lant e lng) necessários para plotar os pontos no mapa.'''
    qs = Evento.objects     # Objeto QuerySet dos Eventos
    tipo  = req.GET['tipo'] # Não sei porque, mas o tipo não está chegando como parâmetro
    campo_data_ini = req.GET['data_ini'] # Filtro de data de início
    campo_data_fim = req.GET['data_fim'] # Filtro de data de fim
    
    eventos = [] # Lista de eventos a ser enviada
    
    if tipo:
        qs = qs.filter(tipo=tipo)
    
    if campo_data_ini:
        data_ini = datetime.strptime( # convertendo campo_data_ini para datetime
            campo_data_ini, '%Y-%m-%d') 
        qs = qs.filter(data__gte=data_ini)
    
    if campo_data_fim:
        data_fim = datetime.strptime( # convertendo campo_data_ini para datetime
            campo_data_fim, '%Y-%m-%d') 
        qs = qs.filter(data__lte=data_fim)
    
    for e in qs.iterator():
        
        obj = {
            # Pode adicionar outros campos aqui
            'lat' : e.lat,
            'lng' : e.lng,
        }
        print("obj:", obj)
        eventos.append(obj)
    return HttpResponse(json.dumps({'eventos':eventos}))
