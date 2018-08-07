from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Doctors(models.Model):
    name = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)

    class Meta:
         ordering = ('id' ,)
class Speciality(models.Model):
    speciality_name= models.CharField(max_length=200)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True, blank=True )
    doctor =models.CharField(max_length=200)
    description = models.TextField(max_length=20000)
    date = models.DateField(default = 0)

    class Meta:
         ordering = ('id',)

    def __str__(self):
        return self.user.username
