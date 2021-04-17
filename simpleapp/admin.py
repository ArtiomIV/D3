from django_d1_task.simpleapp.models import Category, Product
from django.contrib import admin
from .models import Product, Category
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)