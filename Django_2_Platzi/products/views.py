from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Products
from .forms import ProductForm
# from .mixins import LoginRequiredMixin


class ProductList(ListView):
    model = Products

# def hello_world(request):
#     product = Products.objects.order_by('id')
#     template = loader.get_template('index.html')
#     context = {
#         'product': product
#     }
#     return HttpResponse(template.render(context, request))

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Products

# def product_detail(request, pk):
#     # aquí retorna el detalle de un product según el PK recibido
#     product_object = get_object_or_404(Products, pk=pk)
#     template = loader.get_template('product_detail_template.html')
#     title = product_object.name
#     context = {
#         'product_object': product_object,
#         'title' : title
#     }
#     return HttpResponse(template.render(context, request))

class NewProductView(LoginRequiredMixin, CreateView):
    model = Products
    # template_name = 'new_product_template.html'
    fields = '__all__'
    success_url = '/'

# def new_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save()
#             product.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = ProductForm()


#     template = loader.get_template('new_product_template.html')

#     title = 'new article'
#     context = {
#         'form': form,
#         'title' : title
#     }
#     return HttpResponse(template.render(context, request))







