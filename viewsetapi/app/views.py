from django.core import serializers
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.utils import json

from rest_framework.viewsets import ModelViewSet
from .models import Pelicula
from .serializer import PeliculaSerializer

from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count
from django.http import HttpResponse, JsonResponse

from .models import Pelicula
from .forms import CreateMovieForm, UpdateMovieForm

@api_view(['POST'])
def create_movie_view(request):
    if request.method == 'POST':
        pelicula_data = JSONParser().parse(request)
        pelicula_serializer = PeliculaSerializer(data=pelicula_data)
        if pelicula_serializer.is_valid():
            pelicula_serializer.save()
            return JsonResponse(pelicula_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(pelicula_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_movie_view(request):
        if request.method == 'GET':
            pelicula = Pelicula.objects.all()
            name = request.GET.get('name', None)
            if name is not None:
                pelicula = pelicula.filter(name__icontains=name)

            pelicula_serializer = PeliculaSerializer(pelicula, many=True)
            return JsonResponse(pelicula_serializer.data, safe=False)

@api_view(['GET'])
def detail_onemovie_view(request, pk):
    try:
        pelicula = Pelicula.objects.get(pk=pk)
    except Pelicula.DoesNotExist:
        return JsonResponse({'message': 'el nombre no existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        pelicula_serializer = PeliculaSerializer(pelicula)
        return JsonResponse(pelicula_serializer.data)

@api_view(['GET'])
def detail_everymovie_view(request,pk,titulo,calificacion,pais):
    try:
        pelicula = Pelicula.objects.all()
    except Pelicula.DoesNotExist:
        return JsonResponse({'message': 'el nombre no existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        pelicula= Pelicula.objects.filter(pk=pk).filter(titulo=titulo).filter(calificacion=calificacion).filter(pais=pais)
    pelicula_serializer = PeliculaSerializer(pelicula, many=True)
    return JsonResponse(pelicula_serializer.data, safe=False)



@api_view(['GET'])
def detail_summarymovie_view(request, pais):
    try:
        pelicula = Pelicula.objects.all()
    except Pelicula.DoesNotExist:
        return JsonResponse({'message': 'el nombre no existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        pelicula = Pelicula.objects.annotate(contador=Count('pais')).filter(pais=pais)
        pelicula_serializer = PeliculaSerializer(pelicula, many=True)
        return JsonResponse(pelicula_serializer.data, safe=False)

@api_view(['GET'])
def detail_topymovie_view(request):
    try:
        pelicula = Pelicula.objects.all()
    except Pelicula.DoesNotExist:
        return JsonResponse({'message': 'el nombre no existe'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        pelicula = Pelicula.objects.annotate(total=Count('calificacion')).order_by('-calificacion')[:5]
    pelicula_serializer = PeliculaSerializer(pelicula, many=True)
    return JsonResponse(pelicula_serializer.data, safe=False )



@api_view(['PUT'])
def edit_movie_view(request, pk):
    pelicula = Pelicula.objects.get(pk=pk)
    if request.method == 'PUT':
        persona_data = JSONParser().parse(request)
        persona_serializer = PeliculaSerializer(pelicula, data=persona_data)
        if persona_serializer.is_valid():
            persona_serializer.save()
            return JsonResponse(persona_serializer.data)
        return JsonResponse(persona_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_movie_view(request, pk):
    pelicula = Pelicula.objects.get(pk=pk)
    if request.method == 'DELETE':
        pelicula.delete()
        return JsonResponse({'message': 'Pelicula eliminada correctamente'}, status=status.HTTP_204_NO_CONTENT)

def get_movie_queryset(query=None):
    queryset = []
    queries = query.split(" ")  # python install 2019 = [python, install, 2019]
    for q in queries:
        posts = Pelicula.objects.filter(
            Q(titulo__icontains=q) |
            Q(calificacion__icontains=q) |
            Q(pais__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))

# Create your views here.
