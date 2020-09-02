from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index.html', views.index, name="index"),
    path('normal.html', views.delivery, name="delivery"),
    path('contact.html', views.contact, name="contact"),
    path('faq.html', views.faq, name="faq"),
    path('products.html', views.products, name="products"),
    path('product/<int:product_id>/',
         views.product, name="product"),
    path('product_summary.html', views.product_summary, name="product_summary"),
    path('special_offer.html', views.special_offer, name="special_offer"),
    path('register.html', views.register, name="register"),
    path('login.html', views.login, name="login"),
    path('compair.html', views.compair, name="compair"),
]
