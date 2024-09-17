from rest_framework import serializers
from .models import HealthProfile, FoodEntry

class HealthProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProfile
        fields = '__all__'

class FoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodEntry,
        fields = '__all__'