from django.db import models
from fitness_analyser.models import Fitness
from fitness_analyser.models import Cadet_Bio
from threshold_managment.models import Threshold
# from django.contrib.auth.models import User
from authorized_user.models import CustomUser

# Create your models here.

class ED(models.Model):
    ED_count = models.PositiveSmallIntegerField(default=0)
    cn = models.OneToOneField(Cadet_Bio, on_delete=models.CASCADE)

    def __str__(self):
        return f" C/No: {self.cn.C_N}, Entry: {self.cn.entry}, House: {self.cn.house}, No. of ED's {self.ED_count}"

    