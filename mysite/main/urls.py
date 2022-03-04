from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    
]