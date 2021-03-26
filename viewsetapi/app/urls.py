from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include
from . import views

urlpatterns = [
    #path('movies/', create_movie_view, name="create"),
    #path('<slug>/', detail_movie_view, name="detail"),
    #path('<slug>/edit/', edit_movie_view, name="edit"),
    #path('<slug>/edit/', edit_movie_view, name="edit"),

    url(r'^movies$', views.detail_movie_view),
    url(r'^movies/one/(?P<pk>[0-9]+)$', views.detail_onemovie_view),
    path('movies/every/<int:pk>/<str:titulo>/<int:calificacion>/<str:pais>/',views.detail_everymovie_view),
    path('movies/ver', views.get_movie_queryset),
    path('movies/summary/<str:pais>/', views.detail_summarymovie_view),
    path('movies/top/', views.detail_topymovie_view),
    url(r'^movies/delete/(?P<pk>[0-9]+)$', views.delete_movie_view),
    url(r'^movies/edit/(?P<pk>[0-9]+)$', views.edit_movie_view),
    url(r'^movies/add$', views.create_movie_view),

]
