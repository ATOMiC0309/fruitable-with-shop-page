from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Product


# Create your views here.


# def index(request: HttpRequest):
#     context = {
#         'categories': Category.objects.all(),
#         'products': Product.objects.all()[:8],
#     }
#     return render(request, 'shop/index.html', context)


class ProductList(ListView):
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'
    extra_context = {
        'categories': Category.objects.filter(parent=None),
        'title': "Barcha Produclar"
    }


class AllProductList(ProductList):
    template_name = 'shop/shop.html'


def product_by_category(request, pk):
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    context = {
        'categories': Category.objects.filter(parent=None),
        'products': products
    }
    return render(request, 'shop/shop.html', context=context)

