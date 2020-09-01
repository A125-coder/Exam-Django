from django.db import models
from datetime import datetime


class Products(models.Model):
    proguct_title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_favorite = models.BooleanField(default=False)
    features = models.CharField(max_length=250)
    editorial_reviews = models.CharField(max_length=1250)

    def __str__(self):
        return self.product_title
