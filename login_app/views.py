from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            print("login successful")
            return redirect('index')  # Ensure this name matches the index route
        else:
            messages.error(request, 'Invalid username or password.')
            print("login failed")

    return render(request, 'login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)  # Log the user out
    return render(request, 'logout.html')  # Redirect to the login page