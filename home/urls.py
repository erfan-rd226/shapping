from django.urls import path , include
from rest_framework.routers import DefaultRouter 
from . import views
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


# router = DefaultRouter()
# router.register('categories',views.CategoryViewSetApi)
# router.register('products',views.ProductViewSetApi)


schema_view = get_schema_view(
   openapi.Info(
      title="shopping",
      default_version='v1.0.0',
      description="this is about shopping",
      contact=openapi.Contact(email="erfanrajabzade7278@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
   authentication_classes=(JWTAuthentication,),
)


urlpatterns = [

    # path('', include(router.urls)),
    path("product/", views.ProductViewSetApi.as_view()),
    path("category/", views.CategoryViewSetApi.as_view()),
    path('token/', TokenObtainPairView.as_view(), name="token-obtain"),
    path('token/refresh/', TokenRefreshView.as_view(), name= 'token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='verify'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] 
