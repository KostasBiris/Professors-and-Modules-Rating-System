from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from .models import *

# Create your views here.

def index(request):
    return render(request, "main/base.html", {})

def home(request):
    return render(request, "main/home.html", {})    

def register_request(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/home")
	else:
		form = UserCreationForm()
		
	return render(request, "main/register.html", {"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect("home")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	return redirect("home")


def list_request(request):
	modules_list = Module.objects.all()
	return render(request, 'main/list.html', {'modules_list': modules_list})