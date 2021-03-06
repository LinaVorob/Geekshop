from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='phone_form')
def phone_form(number):
    """
    Преобразует обычное число в правильный формат телефоного номера
    """
    number = str(number)
    return f'+{number[0]}({number[1:4]})-{number[4:7]}-{number[7:9]}-{number[9:]}'


@register.filter(name='one_word')
def one_word(email):
    """
    fnlkwnf;
    :param email:
    :return:
    """

    return email[1]

