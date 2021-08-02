from django.db import models
# from cadet_bio.models import Cadet_Bio
# from django.contrib.auth.models import User
from authorized_user.models import CustomUser
from threshold_managment.models import Threshold
from .utils import generate_code


# Create your models here.


class Cadet_Bio(models.Model):
    C_N = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    entry = models.CharField(max_length=20)
    house = models.CharField(max_length=20)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"C/No: {self.C_N},   Name: {self.name}"

    # def get_absolute_url(self):
    #     return reverse("fitness_analyser:detail", args=[self.C_N,])



class Fitness(models.Model):
    push_ups = models.PositiveSmallIntegerField()
    chin_ups = models.PositiveSmallIntegerField()
    sit_ups = models.PositiveSmallIntegerField()
    One_Mile = models.PositiveSmallIntegerField()
    Two_Miles = models.PositiveSmallIntegerField()
    cn = models.ForeignKey(Cadet_Bio, on_delete=models.CASCADE)
    average = models.FloatField(blank=True)
    PT_Test_Date = models.DateField(auto_now=False, auto_now_add=False)

    def save(self, *args, **kwargs):
        self.average = ((self.push_ups * 10/100)+(self.sit_ups * 10/100)+(self.chin_ups * 15/100)+(self.One_Mile * 35/100)+(self.Two_Miles * 30/100) * 100)/4 
        return super().save(*args, **kwargs)


    def __str__(self):     
        return f"C/NO: {self.cn.C_N}, House: {self.cn.house}, Entry: {self.cn.entry}, Average: {self.average}, Dated: {self.PT_Test_Date}, Push-Up: {self.push_ups}"

    # def get_absolute_url(self):
    #     return reverse("fitness_analyser:detail", kwargs={"pk": self.pk})
    
    def get_cadet(self):
        return self.cn.all()


class CSV(models.Model):
    file_name = models.CharField(max_length=120, null=True)
    csv_file = models.FileField(upload_to='csvs', null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)
    
    
