from django.db import models
# from django.contrib.auth.models import User
from authorized_user.models import CustomUser

# Create your models here.

class Threshold(models.Model):
    Fitness_Standard_per = models.PositiveSmallIntegerField()
    updated_On = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return str(self.Fitness_Standard_per)