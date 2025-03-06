from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogAppViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'blogs', BlogAppViewSet, basename='blogapp')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
