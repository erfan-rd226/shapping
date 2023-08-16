from django.shortcuts import render
from home.models import Category,Product
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from home.serializers import CategorySerializer ,ProductSerializer


# @api_view(['GET'])
# def CategoriesVeiws(request:Request):
#     category = Category.objects.all()
#     serializer = CategorySerializer(category, many=True)
#     return Response(serializer.data, status.HTTP_200_OK)


# @api_view(['GET'])
# def productsVeiws(request:Request):
#     product = Product.objects.all()
#     serializer = ProductSerializer(product, many=True)
#     return Response(serializer.data, status.HTTP_200_OK)

class CategoriesGenerics(generics.ListAPIView):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)


class ProductsGenerics(generics.ListAPIView):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True) 