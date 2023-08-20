from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from home.models import Category,Product
from home.views import paginationshop
from home.serializers import CategorySerializer ,ProductSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class CategoriesGenerics(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = paginationshop
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'is_enable']

    @method_decorator(cache_page(60))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class ProductsGenerics(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = paginationshop
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories','title']

    @method_decorator(cache_page(60))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    