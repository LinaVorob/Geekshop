from django.shortcuts import render
import json

from mainapp.models import Product, Contacts


def main(request):
    title = 'Магазин'

    with open("geekshop/menu.json", "r", encoding='utf-8') as read_file:
        links_menu = json.load(read_file)
    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:4]

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
    }

    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'Контакты'


    with open("geekshop/menu.json", "r", encoding='utf-8') as read_file:
        links_menu = json.load(read_file)

    locations = Contacts.objects.all()
    for location in locations:
        print(location.phone)

    context = {
        'title': title,
        'links_menu': links_menu,
        'locations': locations,
    }

    return render(request, 'geekshop/contact.html', context=context)
