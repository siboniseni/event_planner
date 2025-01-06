from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('user_auth:login')
        else:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('events:index')  # Redirect to the polls home page
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('user_auth:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})


def authenticate_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is None:
        messages.error(request, "Invalid username or password")
        return redirect('user_auth:login')
    else:
        login(request, user)
        return redirect('events:index')

