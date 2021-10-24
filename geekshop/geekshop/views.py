from django.shortcuts import render
import json

from basketapp.models import Basket
from mainapp.models import Product, Contacts


def main(request):
    title = 'Магазин'

    with open("geekshop/menu.json", "r") as read_file:
        links_menu = json.load(read_file)
    basket = []
    products = Product.objects.all()[:4]
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products': products,
        'basket': basket,
    }

    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'Контакты'
    basket = Basket.objects.filter(user=request.user)


    with open("geekshop/menu.json", "r") as read_file:
        links_menu = json.load(read_file)

    locations = Contacts.objects.all()
    for location in locations:
        print(location.phone)

    context = {
        'title': title,
        'links_menu': links_menu,
        'locations': locations,
        'basket': basket,
    }

    return render(request, 'geekshop/contact.html', context=context)
