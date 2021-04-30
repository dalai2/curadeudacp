
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from codigo_postal import views

router = routers.DefaultRouter()
router.register(r'estados', views.EstadoViewSet)
router.register(r'municipios', views.MunicipioViewSet)
router.register(r'ciudades', views.CiudadViewSet)
router.register(r'oficinas_postales', views.OficinaPostalViewSet)
router.register(r'asentamientos', views.AsentamientoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
