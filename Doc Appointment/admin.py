from django.contrib import admin
from .models import Doctors,Speciality,Appointment

# Register your models here.

admin.site.register(Doctors,Speciality,Appointment)
