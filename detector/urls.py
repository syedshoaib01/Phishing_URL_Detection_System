from django.urls import path
from . import views

urlpatterns = [
    path('api/detect/', views.detect_api, name='detect_api'),
]
