import jwt
import uuid

from django.conf import settings
from django.shortcuts import render

from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from .models import ApiKey
from apikey import serializers


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ApiKeyView(APIView):
    def post(self, request):
        serializer = serializers.ApiKeySerializer(data=request.data)
        
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            error_message = "Invalid data. Please check your input."
            return Response(serializer.errors)
