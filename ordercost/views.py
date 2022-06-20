from django.shortcuts import render
from . import forms

# Create your views here.

ORDER_UNIT = ['offset','solvent','riso','stamp']

# Меню выбора вида продукции
def index(request):
    context = {'unit_menu': ORDER_UNIT}

    return render(request, 'ordercost/index.html', context=context)

def offset(request):
    form = forms.OffsetForms()
    context = {'unit': 'offset', 'form' : form}
    return render(request, 'ordercost/offset.html', context=context)

def solvent(request):
    context = {'unit': 'solvent'}
    return render(request, 'ordercost/solvent.html')

def riso(request):
    context = {'unit': 'riso'}
    return render(request, 'ordercost/riso.html')

def stamp(request):
    context = {'unit': 'stamp'}
    return render(request, 'ordercost/stamp.html')