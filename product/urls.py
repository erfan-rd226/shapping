from django.urls import path
from .views import ProductApi

urlpatterns = [
    path("products-test/", ProductApi.as_view())
]