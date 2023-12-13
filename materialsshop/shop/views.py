from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request):
    template = 'product/index.html'
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {'categories': categories,
               'products': products}
    return render(request, template, context)


def product_detail(request, product_id):
    template = 'product/detail.html'
    product = get_object_or_404(Product,
                                id=product_id,
                                available=True)
    context = {'product': product}
    return render(request, template, context)
