from django.core.management.base import BaseCommand
import json, os

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product, Contacts
from basketapp.models import Basket

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='utf8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        users = load_from_json('users')

        ShopUser.objects.all().delete()
        super_user = ShopUser.objects.create_superuser('admin', 'admin@geekshop.local', 'qwerty', age=25)
        for user in users:
            new_user = ShopUser(**user)
            new_user.save()

        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        contacts = load_from_json('contacts')
        Contacts.objects.all().delete()
        for contact in contacts:
            new_contact = Contacts(**contact)
            new_contact.save()

        baskets = load_from_json('baskets')
        Basket.objects.all().delete()
        for basket in baskets:
            new_basket = Contacts(**basket)
            new_basket.save()

        if super_user:
            print('БД готова')
