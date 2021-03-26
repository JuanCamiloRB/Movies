from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50, blank=False, default='')
    calificacion = models.PositiveSmallIntegerField(max_length=1, blank=False, validators=[MaxValueValidator(5),MinValueValidator(1)])
    pais = models.CharField(max_length=50, blank=False, default='')
    ocalificacion = models.BooleanField( default=False)


    def __str__(self):
        return self.titulo

