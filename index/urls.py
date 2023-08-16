from django.urls import path
from . import views

urlpatterns = [
    path('',views.CategoriesGenerics.as_view()),
    path('products/',views.ProductsGenerics.as_view()),
]
