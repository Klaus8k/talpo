from django.shortcuts import render, HttpResponse
from .forms import MathForm

# Create your views here.

def index(request):

    return render(request, 'main_page/index.html', {'name': 'main_page'})

