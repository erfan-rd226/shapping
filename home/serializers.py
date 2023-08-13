from .models import Category , Product 
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        filter = ['id','title','description','is_enable']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Product
        filter = ['id','title','categories','description','is_enable']