from django.urls import path
from . import views

urlpatterns = [
    path('',views.CategoriesVeiws),
    path('products/',views.productsVeiws)
]
