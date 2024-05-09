from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Products

def hello_world(request):
    product = Products.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))