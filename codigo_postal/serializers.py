from codigo_postal.models import Ciudad, Asentamiento, Estado, Municipio, OficinaPostal
from rest_framework import serializers


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado
        fields = ['nombre_estado', 'codigo_estado']


class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Municipio
        fields = ['codigo_municipio', 'estado', 'municipio']


class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['nombre', 'codigo_ciudad']


class OficinaPostalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OficinaPostal
        fields = ['oficina_postal']


class AsentamientoSerializer(serializers.HyperlinkedModelSerializer):
    lookup_field = 'cp_asentamiento'

    class Meta:
        model = Asentamiento
        fields = ['asentamiento', 'oficina_postal', 'codigo_ciudad', 'codigo_municipio',
                  'clave_asentamiento', 'cp_asentamiento', 'zona_asentamiento', 'estado']
