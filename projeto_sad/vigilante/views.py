#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from vigilante.util import get_lat_lng

# Create your views here.
def home(req):
    valores = {}
    if req.method == 'POST':
        # Marcando ponto
        endereco = req.POST['endereco']
        valores['p'] = get_lat_lng(endereco)
        
        # Marcando áreas de risco
        # Obs.: esses valores futuramente virão do banco de dados, 
        # mas por enquanto estão só no código-fonte (hard-coded)
        valores['areas'] = []
        valores['areas'] += [-6.462477,-37.1083922, 'red'] # Odilon Lebarre, 167, Caicó - RN, Brasil
        valores['areas'] += [-6.4621788,-37.0943734, 'blue'] # Av. Cel. Martiniano, 781, Caicó - RN, Brasil
        valores['areas'] += [-6.4652023,-37.0942773, 'green'] # Rua Generina Vale, 1206, Caicó- RN, Brasil
    return render_to_response('home.html',
        valores,
        context_instance=RequestContext(req))