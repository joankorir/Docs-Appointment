from django.urls import path

from . import views
from django.conf.urls import url
# from django.contrib.auth import views as auth

urlpatterns = [
    path('',views.index,name='index'),
    url('create_appointment/', views.create_appointment, name = 'create_appointment'),
	url('register_doctor/', views.register_doctor, name = 'register_doctor'),
	url('register_speciality/', views.register_speciality, name = 'register_specialty'),
	url('see_appointments/', views.appointment_list, name = 'appointment_list'),
	url('create_user/', views.AddingUser),
	url('(?P<pk>[-\d]+)/edit/', views.appointment_edit, name='appointment_edit'),
	url('(?P<pk>[-\d]+)/delete/', views.appointment_delete, name='appointment_delete'),
	url('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),

]
