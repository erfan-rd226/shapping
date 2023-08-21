from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    is_enable = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'categorys'

    

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    categories = models.ForeignKey('Category', related_name='product',on_delete=models.CASCADE)
    is_enable = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        db_table = 'products'

