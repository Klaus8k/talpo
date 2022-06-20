from django.shortcuts import render, HttpResponse
from .forms import MathForm

# Create your views here.

PAGES = ['']

def index(request):

    return render(request, 'mainpage/index.html', {'title': 'mainpage'})

