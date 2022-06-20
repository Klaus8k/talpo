from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app_order_cost/index.html', context={'app_name':'order-cost'})