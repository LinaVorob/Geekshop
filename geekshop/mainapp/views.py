import json

from django.shortcuts import render


def products(request):
    title = 'Каталог'

    with open("mainapp/catalog.json", "r") as read_file:
        links_catalog = json.load(read_file)

    with open("mainapp/menu.json", "r") as read_file:
        links_menu = json.load(read_file)


    context = {
        'title': title,
        'links_catalog': links_catalog,
        'links_menu': links_menu,
    }

    return render(request, 'mainapp/products.html', context=context)
