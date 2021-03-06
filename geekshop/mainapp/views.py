import json
import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product



def get_hot_product():
    products = Product.objects.filter(is_active=True)
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None, page=1):
    title = 'Каталог'

    links_catalog = []
    products = Product.objects.select_related('category').filter(is_active=True, quantity__gte=1).order_by('price')
    for product in products:
        if product.category not in links_catalog:
            links_catalog += ProductCategory.objects.filter(name=product.category)

    with open("mainapp/menu.json", "r", encoding='utf-8') as read_file:
        links_menu = json.load(read_file)

    if pk is not None:
        if pk == 0:
            category = {'pk': 0, 'name': 'все'}
            products = Product.objects.filter(is_active=True, category__is_active=True, quantity__gte=1).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True, quantity__gte=1).order_by('price')
        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        context = {
            'title': title,
            'links_catalog': links_catalog,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
        }

        return render(request, 'mainapp/products.html', context=context)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    context = {
        'title': title,
        'links_catalog': links_catalog,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'products': products,
    }

    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    links_catalog = []
    products = Product.objects.filter(is_active=True).order_by('price')
    for item in products:
        if item.category not in links_catalog:
            links_catalog += ProductCategory.objects.filter(name=item.category)
    with open("mainapp/menu.json", "r", encoding='utf-8') as read_file:
        links_menu = json.load(read_file)
    context = {
        'title': product.name,
        'links_menu': links_menu,
        'links_catalog': links_catalog,
        'product': product,
        'same_products': get_same_products(product),
    }
    return render(request, 'mainapp/product.html', context)
