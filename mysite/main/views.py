from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import NewUserForm
from .models import *

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})    

def register(response):
	if response.method == "POST":
		form = UserCreationForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect("/home")
	else:
		form = UserCreationForm()
		
	return render(response, "main/register.html", {"form":form})