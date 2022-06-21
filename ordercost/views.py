from django.shortcuts import render
from .forms import OffsetForms

# Create your views here.

ORDER_UNIT = ['offset','solvent','riso','stamp']

# Меню выбора вида продукции
def index(request):
    context = {'unit_menu': ORDER_UNIT}

    return render(request, 'ordercost/index.html', context=context)

def offset(request):
    if request.method == 'GET':
        form = OffsetForms(request.GET)
        if form.is_valid():
            print (form.cleaned_data) # выполнение бизнес логики и вывод в результат.
# надо посмотреть как блок выводить когда надо. То есть результат выводим в блоке, а он или из шаблона или блок контента.
    else:
        form = OffsetForms()

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

