from django.db import models


class Category(models.Model):
    name = models.CharField('Название категории', max_length=255, unique=True)
    slug = models.SlugField('Адрес', max_length=255, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.SET_NULL,
                                 verbose_name='Категория',
                                 null=True)
    name = models.CharField('Название товара', max_length=255)
    slug = models.SlugField('Адрес', max_length=255, unique=True)
    image = models.ImageField('Изображение',
                              upload_to='products/images/',
                              blank=True)
    description = models.TextField('Описание товара',
                                   null=True,
                                   blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('Количество товара')
    available = models.BooleanField('Наличие товара', default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
