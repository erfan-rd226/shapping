from django.shortcuts import render
from home.models import Category,Product
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def CategoriesVeiws(request:Request):
    category = list(Category.objects.all())
    return Response({'categoy':category}, status.HTTP_200_OK)



@api_view(['GET'])
def productsVeiws(request:Request):
    product = list(Product.objects.all())
    return Response({'product':product}, status.HTTP_200_OK)