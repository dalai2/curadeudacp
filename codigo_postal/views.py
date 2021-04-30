from rest_framework import viewsets
from rest_framework import permissions
import django_filters.rest_framework

from codigo_postal.models import Estado, Asentamiento, Municipio, Ciudad, OficinaPostal
from codigo_postal.serializers import EstadoSerializer, AsentamientoSerializer, MunicipioSerializer, OficinaPostalSerializer, CiudadSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    """ endpoint que permite visualizar o editar Estados """
    queryset = Estado.objects.all().order_by('-codigo_estado')
    serializer_class = EstadoSerializer
    permission_classes = [permissions.IsAuthenticated]


class MunicipioViewSet(viewsets.ModelViewSet):
    """ endpoint que permite visualizar o editar asentamientos """
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = [permissions.IsAuthenticated]


class CiudadViewSet(viewsets.ModelViewSet):
    """ endpoint que permite visualizar o editar asentamientos """
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    permission_classes = [permissions.IsAuthenticated]


class OficinaPostalViewSet(viewsets.ModelViewSet):
    """ endpoint que permite visualizar o editar asentamientos """
    queryset = OficinaPostal.objects.all()
    serializer_class = OficinaPostalSerializer
    permission_classes = [permissions.IsAuthenticated]


class AsentamientoViewSet(viewsets.ModelViewSet):
    """ endpoint que permite visualizar o editar asentamientos """
    queryset = Asentamiento.objects.all().order_by('-asentamiento')
    serializer_class = AsentamientoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
