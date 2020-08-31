from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def delivery(request):
    return render(request, 'pages/normal.html')


def contact(request):
    return render(request, 'pages/contact.html')


def faq(request):
    return render(request, 'pages/faq.html')


def products(request):
    return render(request, 'pages/products.html')


def product_details(request):
    return render(request, 'pages/product_details.html')
