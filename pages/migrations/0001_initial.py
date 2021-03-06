# Generated by Django 3.1 on 2020-09-01 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proguct_title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(default=datetime.datetime.now)),
                ('photo_0', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_favorite', models.BooleanField(default=False)),
                ('features', models.CharField(max_length=250)),
                ('editorial_reviews', models.CharField(max_length=1250)),
            ],
        ),
    ]
