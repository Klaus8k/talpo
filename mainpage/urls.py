from django.urls import path
from django.shortcuts import render, HttpResponse
from . import views

app_name = 'mainpage'
urlpatterns = [
    path('', views.index, name='index'),
]
