from django.db import models

"""Modelos de codigos postales"""


class Estado(models.Model):
    """ Modelo de estados. contiene el nombre e identificador por estado """
    nombre_estado = models.CharField('estado', max_length=30)
    codigo_estado = models.PositiveSmallIntegerField(
        primary_key=True)

    def __str__(self):
        return self.nombre_estado

    class Meta:
        unique_together = ['codigo_estado', 'nombre_estado']


class Municipio(models.Model):
    """ Modelo de municipios. contiene el nombre e identificador por municipio y el estado al que pertenece"""
    codigo_municipio = models.PositiveSmallIntegerField()
    estado = models.ForeignKey(
        Estado, on_delete=models.CASCADE, blank=True, null=True)
    municipio = models.CharField('municipio', max_length=100)

    def __str__(self):
        return self.municipio


class Ciudad(models.Model):
    """ Tiene el codigo de ciudad y el nombre de ciudad al que pertenece el codigo """
    nombre = models.CharField('ciudad', max_length=100)
    codigo_ciudad = models.PositiveSmallIntegerField(
        'codigo ciudad', primary_key=True)

    def __str__(self):
        return self.nombre


class OficinaPostal(models.Model):
    """ Lista de codigos postales de las oficinas postales asignadas """
    oficina_postal = models.PositiveSmallIntegerField(
        'oficina', primary_key=True)

    def __str__(self):
        return self.oficina_postal


class Asentamiento(models.Model):
    """ Datos de los asentamientos: nombre/codigo asentamiento, oficina postal correspondiente, codigo de municipio y codigo postal del asentamiento """
    asentamiento = models.CharField(max_length=110)
    oficina_postal = models.ForeignKey(
        OficinaPostal, on_delete=models.SET_NULL, blank=True, null=True)
    codigo_ciudad = models.ForeignKey(
        Ciudad, on_delete=models.SET_NULL, blank=True, null=True)
    codigo_municipio = models.ForeignKey(
        Municipio, on_delete=models.SET_NULL, blank=True, null=True)
    clave_asentamiento = models.PositiveSmallIntegerField(
        'clave asentamiento')
    cp_asentamiento = models.PositiveSmallIntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    ZONAS = [
        ('U', 'Urbano'),
        ('R', 'Rural'),
    ]

    zona_asentamiento = models.CharField(max_length=1, choices=ZONAS)

    def __str__(self):
        return self.asentamiento
