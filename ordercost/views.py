from django.shortcuts import render
from .forms import OffsetForms
from .logic import result

# Create your views here.

ORDER_UNIT = ['offset', 'solvent', 'riso', 'stamp']


# Меню выбора вида продукции
def index(request):
    context = {'unit_menu': ORDER_UNIT}

    return render(request, 'ordercost/index.html', context=context)


def offset(request):
    print(request)
    context = {'unit': 'offset'}

    if request.method == 'GET':
        form = OffsetForms(request.GET)
        if form.is_valid():
            to_calc = form.cleaned_data
            to_calc['unit'] = 'offset'
            context['result'] = get_result(to_calc)

    else:
        form = OffsetForms()

    context['form'] = form

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


# Сюда напишем функцию для вызова бизнеслогики с нашими значениями из форм
def get_result(args: dict):
    return result(args)
