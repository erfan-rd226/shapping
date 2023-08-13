from django.urls import path , include
from rest_framework.routers import DefaultRouter 
from . import views


router = DefaultRouter(trailing_slash=False)
router.register('categories/',views.CategoryViewSetApi)
router.register('products/',views.ProductViewSetApi)


urlpatterns = router.urls

