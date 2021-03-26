from django import forms

from .models import Pelicula


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('titulo', 'calificacion', 'pais')


class UpdateMovieForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('titulo', 'calificacion', 'pais')

    def save(self, commit=True):
        movie = self.instance
        movie.titulo = self.cleaned_data['titulo']
        movie.calificacion = self.cleaned_data['calificacion']
        movie.pais = self.cleaned_data['pais']

        if commit:
            movie.save()
        return movie
