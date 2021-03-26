from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Pelicula

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = ('titulo', 'calificacion', 'pais')
