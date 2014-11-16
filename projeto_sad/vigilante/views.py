#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from vigilante.util import get_lat_lng

# Create your views here.
def home(req):
    # -- temporário
    from vigilante.models import Evento

    print ('aqui')
    eventos = Evento.objects.all()
    for e in eventos:
        print('Evento:', e.id)
        print('Endereco:', e.endereco)
        print('Latitude:', e.lat) # o simples acesso à propriedade faz com que o
        # endereço seja convertido num ponto geográfico.
        print('Longitude:', e.lng)
    # temporário --
    
    valores = {}
    if req.method == 'POST':
        # Marcando ponto
        endereco = req.POST['endereco']
        valores['p'] = get_lat_lng(endereco)
    return render_to_response('home.html',
        valores,
        context_instance=RequestContext(req))

