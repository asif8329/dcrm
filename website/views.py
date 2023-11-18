from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('home')  # Corrected: Added 'return'
        else:
            messages.error(request, 'There is an error. Please fill the form again.')
            return redirect('home')  # Corrected: Added 'return'
    else:
        return render(request, 'website/home.html')
def login_user(request):
    # Your implementation for the login_user view goes here
    pass

def logout_user(request):
    logout(request)
    messages.success(request, 'successfully,logout.')
    return redirect('home')  # Corrected: Added 'return'
def register_user(request):
    return render(request,'website/register.html',{})