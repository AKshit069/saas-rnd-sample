from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):    
    if request.method == "POST":  
        # Dynamically fetch the username and password from the form
        username = request.POST.get("username") or None
        password = request.POST.get("password") or None
        # Authenticate the user
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Login here!")
                return redirect("/")
    return render(request, "auth/login.html", {})


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None
        
        try:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect("/login/")  # Redirect after successful registration
        except Exception as e: 
            print(f"Error occurred: {e}")
            return render(request, "auth/register.html", {"error": "Could not create user. Please try again."})

    # Handle GET request
    return render(request, "auth/register.html", {})


