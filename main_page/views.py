from django.shortcuts import render, HttpResponse
from django.template import loader
# Create your views here.
def main_index(request):
   print('--------------', request, '--------------')

   template = loader.get_template('main_page/index.html')
#   responce = render(request, template_name='main_page/index.html')
   return HttpResponse(template.render(request=request, context={}))