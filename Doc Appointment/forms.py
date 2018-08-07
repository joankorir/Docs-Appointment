from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Speciality,Doctor,Appointment


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class RegisterDoctorForm(ModelForm):
	choices = tuple(Speciality.objects.all().values_list())
	speciality = forms.ChoiceField(choices=choices)

	class Meta:
		model = Doctor
        exclude = ['speciality']
