# -*- coding:utf-8 -*-
from django.db import models
from vigilante.util import get_lat_lng

'''Possíveis tipos de Evento. Os pares indicam o valor a ser guardado no banco
(ex.: ASSALTO) e um valor amigável ao usuário (ex.: Assalto).'''
TIPOS_DE_EVENTOS = (
    ('ASSALTO',  'Assalto'),
    ('FURTO',    'Furto'),
    ('HOMICIDIO','Homicídio'),
    ('SUICIDIO', 'Suicídio'),
    ('DROGAS',   'Drogas'),
)

# Create your models here.
class Evento(models.Model):
    '''O evento representa uma ocorrência. Mantive o mesmo nome do banco original.'''
    _lat     = models.TextField(blank=True) # Latitude
    _lng     = models.TextField(blank=True) # Longitude
    endereco = models.TextField()           # Endereço da ocorrência em texto
    tipo     = models.CharField(max_length=30, choices=TIPOS_DE_EVENTOS)
    data     = models.DateField()
    
    @property
    def lat(self):
        '''Método acessador (getter) da latitude.
        :returns:
            A latitude do ponto. Uma string.'''
        if (self._lat == '') or (self._lng == ''):
            self._obter_lat_lng()
        return self._lat
    
    @property
    def lng(self):
        '''Método acessador (getter) da longitude.
        :returns:
            A longitude do ponto. Uma string.'''
        if (self._lat == '') or (self._lng == ''):
            self._obter_lat_lng()
        return self._lng
    
    def _obter_lat_lng(self):
        '''Preenche os valores _lat e _lng deste objeto através do endereço
        utilizando o serviço do Google Maps.'''
        ponto = get_lat_lng(self.endereco) # Usa a função para acessar o Maps
        if ponto:                          # Se o ponto não for nulo
            vet_lat_lng = ponto.split(',') # Quebra em um vetor [lat, lng]
            self._lat = vet_lat_lng[0]     # Atribui a latitude (índice 0)
            self._lng = vet_lat_lng[1]     # Atribui a longitude (índice 1)
            self.save()                    # Salva o modelo no banco
    
