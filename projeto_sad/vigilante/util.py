# -*- coding:utf-8 -*-
import urllib, urllib2, json
from django.utils.encoding import smart_str

def get_lat_lng(location):
    '''Pega as coordenadas geográficas de um ponto através de um endereço
    utilizando o serviço do Google Maps.
    :param location:
        O endereço a ser buscado no Google Maps. Uma string.
    :returns:
        Uma string no formato lat,lng (ex.: -6.4628458,-37.1087525)
        ou uma string vazia, caso haja algum problema na busca.'''
    
    location = urllib.quote_plus(smart_str(location))
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % location
    response = urllib2.urlopen(url).read() 
    result = json.loads(response)
    if result['status'] == 'OK':
        lat = str(result['results'][0]['geometry']['location']['lat'])
        lng = str(result['results'][0]['geometry']['location']['lng'])
        return '%s,%s' % (lat, lng)
    else:
        return ''