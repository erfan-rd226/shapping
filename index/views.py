from django.shortcuts import render
from home.models import Category,Product
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from home.serializers import CategorySerializer ,ProductSerializer


class CategoriesGenerics(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsGenerics(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer