'''from django.db import models
from shop.models import Product


class Cart(models.Model):
    product = models.ForeignKey(Product, related_name='cart',
                                verbose_name='Товар')
    count = models.IntegerField('Количество', default=1)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
'''
