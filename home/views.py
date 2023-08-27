from django.shortcuts import render
from django.conf import settings

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination

from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer


class PaginationShop(PageNumberPagination):
    page_size = settings.PAGINATION_PAGE_SIZE


class CategoryViewSetApi(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PaginationShop
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','is_enable']


class ProductViewSetApi(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PaginationShop
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories','title']   
    