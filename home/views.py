# from django.shortcuts import render
# from django.conf import settings
# from rest_framework import viewsets
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.pagination import PageNumberPagination
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Category,Product
# from .serializers import CategorySerializer,ProductSerializer


# class paginationshop(PageNumberPagination):
#     page_size = settings.PAGINATION_PAGE_SIZE


# class CategoryViewSetApi(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     pagination_class = paginationshop
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title','is_enable']


# class ProductViewSetApi(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     pagination_class = paginationshop
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['categories','title']
    


from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer


class paginationshop(PageNumberPagination):
    page_size = settings.PAGINATION_PAGE_SIZE


class CategoryViewSetApi(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = paginationshop
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','is_enable']


class ProductViewSetApi(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = paginationshop
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories','title']   
    