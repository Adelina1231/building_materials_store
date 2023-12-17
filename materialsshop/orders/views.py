from django.shortcuts import render

from cart.cart import Cart
from .models import OrderItem
from .forms import OrderForm
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    template = 'orders/order_create.html'
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            template = 'orders/order_created.html'
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'],
                                         )
            cart.clear()
            order_created.delay(order.id)
            return render(request, template, {'order': order})
    else:
        form = OrderForm()
    return render(request, template, {'cart': cart, 'form': form})
