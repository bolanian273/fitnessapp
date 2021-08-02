from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser): 
    Adju = models.BooleanField(default=False)
    HM = models.BooleanField(default=False)
    Staff = models.BooleanField(default=False)
    JH = models.BooleanField(default=False)
    SSH = models.BooleanField(default=False)
    HH = models.BooleanField(default=False)

