from django.db import models

from shop.models import Product


# class OrderStatus(models.Model):
#     name = models.CharField('Значение', max_length=100)

#     class Meta:
#         verbose_name = 'Статус заказа'
#         verbose_name_plural = 'Статус заказов'

#     def __str__(self):
#         return self.name


class Order(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('Почта')
    phone = models.CharField('Номер телефона', max_length=20)
    address = models.CharField('Адрес', max_length=255)
    postal_code = models.CharField('Индекс', max_length=20)
    status = models.BooleanField('Статус заказа', default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return f'Заказ #{self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE,
                              verbose_name='Заказ')
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE,
                                verbose_name='Товар')
    price = models.DecimalField('Сумма', max_digits=10,
                                decimal_places=2)
    quantity = models.PositiveIntegerField('Количество', default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
