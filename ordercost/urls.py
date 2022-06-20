from django.urls import path
from django.shortcuts import render, HttpResponse
from . import views

app_name = 'ordercost'
urlpatterns = [
    path('', views.index, name='index'),
    path('offset/', views.offset, name = 'offset'),
    path('riso/', views.riso, name = 'riso'),
    path('solvent/', views.solvent, name = 'solvent'),
    path('stamp/', views.stamp, name = 'stamp'),
    ]
