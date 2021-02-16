#This file is created manually by me. This is app's url file
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
