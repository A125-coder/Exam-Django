from django.contrib import admin
from .models import Products

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'price', 'is_published',
                    'list_date', 'description')
    list_display_links = ('product_title', 'price', 'description')
    list_editable = ('is_published', )
    list_per_page = 30


admin.site.register(Products, ProductsAdmin)
