from django.shortcuts import render
import json


def main(request):
    title = 'Магазин'

    with open("geekshop/menu.json", "r") as read_file:
        links_menu = json.load(read_file)

    context = {
        'title': title,
        'links_menu': links_menu,
    }

    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'Контакты'

    with open("geekshop/menu.json", "r") as read_file:
        links_menu = json.load(read_file)

    with open("geekshop/locations.json", "r") as read_file:
        locations = json.load(read_file)

    context = {
        'title': title,
        'links_menu': links_menu,
        'locations': locations,
    }

    return render(request, 'geekshop/contact.html', context=context)
