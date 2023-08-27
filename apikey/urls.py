from django.urls import path
from .views import ApiKeyView

urlpatterns = [
    path('apikey/',ApiKeyView.as_view()),
]
