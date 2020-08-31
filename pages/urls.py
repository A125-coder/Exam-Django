from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('normal.html', views.delivery, name="delivery"),
    path('contact.html', views.contact, name="contact"),
    path('faq.html', views.faq, name="faq"),
    path('products.html', views.products, name="products"),
    path('product_details.html', views.product_details, name="product_details"),
]
