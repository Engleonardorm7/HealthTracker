from django.shortcuts import render

from rest_framework import viewsets
from .models import HealthProfile, FoodEntry
from .serializers import HealthProfileSerializer, FoodEntrySerializer
import requests


class HealthProfileViewSet(viewsets.ModelViewSet):
    queryset = HealthProfile.objedcts.all()
    serializer_class = HealthProfileSerializer


class FoodEntryViewSet(viewsets.ModelViewSet):
    queryset = FoodEntry.objects.all()
    serializer_class = FoodEntrySerializer


class FoodNutritionViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        food_name = request.query_params.get('food_name')
        if not food_name:
            return Response({'error':'food_name parameter is required'}, status=400)

        response = request.get(f'https://api.myfitnesspal.com/v1/foods/{food_name}')
        if response.status_code==200:
            data = response.json()
            return Response(data)
        else:
            return Response({"error": "Failed to fetch data from MyFitnessPal"}, status=response.status_code)