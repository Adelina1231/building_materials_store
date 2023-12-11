from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    template = 'products/index.html'
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {'category': category,
               'categories': categories,
               'products': products}
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, template, context)


def product_detail(request, id, slug):
    template = 'products/detail.html'
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    context = {'product': product}
    return render(request, template, context)
