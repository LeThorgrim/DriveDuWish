from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from pathlib import Path

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            print("login successful")
            return redirect('main')  # Ensure this name matches the index route
        else:
            messages.error(request, 'Invalid username or password.')
            print("login failed")

    return render(request, 'login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)  # Log the user out
        return redirect('login')
    return render(request, 'logout.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, f'Account created for {username}!')
            Path(f'media/{username}').mkdir(parents=True, exist_ok=True)
            return redirect('login')

    return render(request, 'register.html')