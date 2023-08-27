from rest_framework import serializers

from home.models import Product

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
