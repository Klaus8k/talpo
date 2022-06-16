from django.shortcuts import render, HttpResponse


# Create your views here.

def main_index(request):
   context = {'site_name': 'talpo.ru'}
   response = render(request, template_name='main_page/index.html',
                     context=context)

   return response