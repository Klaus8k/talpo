from django.urls import path
from django.shortcuts import render, HttpResponse
from . import views

app_name = 'poligon'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result')
]
