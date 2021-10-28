from PIL import Image
from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='имя',
        unique=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='название',
        max_length=128,
    )

    image = models.ImageField(
        upload_to='products_images',
        blank=True,
    )

    short_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=64,
        blank=True,
    )

    description = models.TextField(
        verbose_name='описание продукта',
        blank=True,
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='цена',
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    is_active = models.BooleanField(verbose_name='активный', default=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 270 or img.width > 270:
            output_size = (270, 270)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Contacts(models.Model):
    city = models.CharField(
        verbose_name='город',
        max_length=64,
        blank=False,
    )

    phone = models.PositiveBigIntegerField(
        verbose_name='номер телефона',
        blank=True,
    )

    email = models.CharField(
        verbose_name='email',
        max_length=128,
        blank=True,
    )

    address = models.TextField(
        verbose_name='адрес',
        blank=True,
    )

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'контакты'
