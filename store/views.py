from django.shortcuts import render
from .models import Product, Category


def all_products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "store/home.html", context)