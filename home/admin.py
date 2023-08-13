from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','is_enable','created_time']
    list_filter = ['is_enable']
    search_fields = ['title']



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','is_enable','created_time']
    list_filter = ['is_enable']
    filter_horizontal = ['categories']
    search_fields = ['title']