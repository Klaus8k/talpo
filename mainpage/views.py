from django.shortcuts import render, HttpResponse

from talpo import settings
from .forms import MathForm

# Create your views here.

PAGES = settings.INSTALLED_APPS[6:] # non django apps. better do it with split('.') no django


def index(request):

        return render(request, 'mainpage/index.html', {'apps': PAGES})

