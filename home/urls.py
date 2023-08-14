from django.urls import path , include
from rest_framework.routers import DefaultRouter 
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('categories',views.CategoryViewSetApi)
router.register('products',views.ProductViewSetApi)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
] 
