from django.db import models
from fitness_analyser.models import Cadet_Bio
# from django.contrib.auth.models import User
from authorized_user.models import CustomUser


# Create your models here.

class Reports(models.Model):
    cn = models.ForeignKey(Cadet_Bio, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='reports', blank=True)
    remarks = models.TextField()
    # created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return str(self.name, self.cn.C_N)
