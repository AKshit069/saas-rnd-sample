from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    
    if request.method == "GET":
        
        # Dynamically fetch the username and password from the form
        username = "akshit"#request.POST.get("username")
        password = "akshit"#request.POST.get("password")
        # Authenticate the user
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Login here!")
                return redirect("/")
    return render(request, "auth/login.html", {})



