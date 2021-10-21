import json

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


def something(request):
    print(request.user)

def products(request, pk=None):
    title = 'Каталог'

    links_catalog = []
    products = Product.objects.all().order_by('price')
    for product in products:
        if product.category not in links_catalog:
            links_catalog += ProductCategory.objects.filter(name=product.category)
    basket = Basket.objects.filter(user=request.user)


    with open("mainapp/menu.json", "r") as read_file:
        links_menu = json.load(read_file)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        context = {
            'title': title,
            'links_catalog': links_catalog,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products.html', context=context)
    same_products = Product.objects.all()[1:3]

    context = {
        'title': title,
        'links_catalog': links_catalog,
        'links_menu': links_menu,
        'same_products': same_products,
        'products': products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context=context)

#Разбить на 2 вьюхи, только те категории, товары с которыми есть