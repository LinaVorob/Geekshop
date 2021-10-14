import json

from django.shortcuts import render

from mainapp.models import ProductCategory


def products(request):
    title = 'Каталог'

    links_catalog = ProductCategory.objects.all()

    with open("mainapp/menu.json", "r") as read_file:
        links_menu = json.load(read_file)


    context = {
        'title': title,
        'links_catalog': links_catalog,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/products.html', context=context)
