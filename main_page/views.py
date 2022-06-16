from django.shortcuts import render, HttpResponse

# Create your views here.
def main_index(request):
   print('--------------', request, '--------------')

   responce = render(request, template_name='main_page/index.html')
   return responce