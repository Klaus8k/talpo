from django.shortcuts import render, HttpResponseRedirect

from .forms import OffsetForms
from .logic import *

# Create your views here.

ORDER_UNIT = ['offset', 'solvent', 'riso', 'stamp']


# Меню выбора вида продукции
def index(request):
    context = {'unit_menu': ORDER_UNIT}

    return render(request, 'ordercost/index.html', context=context)


def offset(request):
    context = {'unit': 'offset'}

    if request.GET.get('reset'):  # при ключе ресет переходит на реквест но только путь path
        return HttpResponseRedirect(request.path)

    # если есть данные из формы передает очищенные данные в функцию обработки
    if request.method == 'GET':
        form = OffsetForms(request.GET)
        if form.is_valid():
            to_calc = form.cleaned_data
            context['result'] = get_result(to_calc)
            to_calc['unit'] = 'offset'


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
    var_args = [args[key] for key in args]
    var = Culc_offset(var_args)
    if int(var.weigth) < 200:
        return var.culc_130()
    else: return var.culc_300()
