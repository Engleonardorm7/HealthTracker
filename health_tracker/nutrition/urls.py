from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthProfileViewSet, FoodEntryViewSet, FoodNutritionViewSet

router = DefaultRouter()
router.register(r'health_profiles',HealthProfileViewSet)
router.register(r'food_entries',FoodEntryViewSet)
router.register(r'food_nutrition',FoodNutritionViewSet, basename='food_nutrition')

urlPatterns = [
    path('',include(router.urls)),
]