from django.shortcuts import render
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

class ProductsGenerics(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = paginationshop
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories','title'] 