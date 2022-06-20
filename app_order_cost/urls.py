from django.urls import path
from django.shortcuts import render, HttpResponse
from . import views

app_name = 'app_order_cost'
urlpatterns = [
    path('', views.index, name='index'),
]
