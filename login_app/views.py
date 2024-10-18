from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('index')  # Redirect to the index page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to login page after logout