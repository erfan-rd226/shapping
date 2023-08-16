from django.shortcuts import render
from home.models import Category,Product
from home.views import paginationshop
from rest_framework import generics
from home.serializers import CategorySerializer ,ProductSerializer


class CategoriesGenerics(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = paginationshop

class ProductsGenerics(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = paginationshop