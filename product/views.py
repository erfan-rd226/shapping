from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from home.models import Product
from product.serializers import productSerializer

class ProductApi(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = productSerializer