from django.db import models

from django.contrib.auth.models import User

class HealthProfile(models.Models):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    age = models.IntegerField()
    activity_level = models.CharField(max_lenght=50, choices=[
        ('sedentary','Sedentary'),
        ('light','Light'),
        ('moderate','Moderate'),
        ('activate','Activate'),
        ('very_active','Very Active')
    ])
    calorie_goal = models.FloatField()
    
    def __str__(self):
        return self.user.username
    
class FoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateField()
    food_name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()
    carbohydrates = models.FloatField()
    fats = models.FloatField()

    def __str__(self):
        return f'{self.date} - {self.food_name}'