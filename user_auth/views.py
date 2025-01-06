from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegistrationForm


# View for user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('user_auth:login')  # Stay on the login page if authentication fails
        else:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            # Redirect to 'next' page or events home page
            return redirect(request.GET.get('next', 'events:home'))
    
    return render(request, 'registration/login.html')  # Render login page


# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('user_auth:login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})  # Render signup page


def user_logout(request):
    logout(request)
    return redirect('events:home')  # Redirect to home after logout



