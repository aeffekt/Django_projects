# las lineas comentadas hacen lo mismo que render, solo que sin usar este shortcut
#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .models import Item

def index(request):
    items_list = Item.objects.filter(done_status=False).order_by('-date_created')
    
    context={
        'items_list': items_list,
    }
    return render(request, 'todo/index.html', context)
    #template = loader.get_template('todo/index.html')
    #return HttpResponse(template.render(context, request))

