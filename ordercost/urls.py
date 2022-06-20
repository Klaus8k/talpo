from django.urls import path
from django.shortcuts import render, HttpResponse
from . import views

app_name = 'ordercost'
urlpatterns = [
    path('', views.index, name='index'),
]
