from django.shortcuts import render, get_object_or_404
from .models import Products


def index(request):
    products = {
        "products": Products.objects.all()
    }
    return render(request, 'pages/index.html', products)


def delivery(request):
    return render(request, 'pages/normal.html')


def contact(request):
    return render(request, 'pages/contact.html')


def faq(request):
    return render(request, 'pages/faq.html')


def products(request):
    return render(request, 'pages/products.html')


def product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    context = {'product': product}
    return render(request, 'pages/product_details.html', context=context)


def product_summary(request):
    return render(request, 'pages/product_summary.html')


def special_offer(request):
    return render(request, 'pages/special_offer.html')


def register(request):
    return render(request, 'pages/register.html')


def login(request):
    return render(request, 'pages/login.html')


def compair(request):
    return render(request, 'pages/compair.html')
