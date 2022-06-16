from django.urls import path
from django.shortcuts import render, HttpResponse
from . import views

app_name = 'main_page'
urlpatterns = [
    path('', views.main_index, name='main_index')
]