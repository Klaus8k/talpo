from django.urls import path
from django.shortcuts import render, HttpResponse
from . import views

urlpatterns = [
    path('', views.index, name='main_index')
]