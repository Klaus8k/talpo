from django.shortcuts import render, HttpResponse
from .forms import MathForm

# Create your views here.

def index(request):

    form = MathForm()

    return render(request, 'poligon/index.html', {'form': form})


def result(request):
    print(request.POST)

    return HttpResponse(f"<h1>{int(request.POST['x']) + int(request.POST['y'])}</h1>")
