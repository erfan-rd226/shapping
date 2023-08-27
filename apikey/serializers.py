
import jwt

from django.conf import settings
from rest_framework import serializers

from .models import ApiKey


class ApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKey
        fields = '__all__'
        extera_kwargs = {
            "token": "read_only"
        }

    def generate_token(self, validated_data:dict):
        user = validated_data.get("User")
        payload = {
            "type": "api_key",
            "user_id": user,
            "exp":"2022-12-31T23:59:59Z",
        }

        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256")
        return token

    def validate(self, attrs):
        user = attrs.get("user")
        expire_time = attrs.get("expire_time")
        is_active = attrs.get("is_active")
        token = self.generate_token(attrs)

        ApiKey.objects.create(
            user=user,
            expire_time=expire_time,
            is_active=is_active,
            token=token
        )

        return attrs
