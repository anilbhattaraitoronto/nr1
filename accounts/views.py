from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username=request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already used for another account.')
                return redirect('home')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is already used by another account.")
                    return redirect('home')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                    user.save()
                    messages.success(request, "You are registered now. Please login.")
                    return redirect('home')
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('home')

    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Your password or username or both are incorrect!')
            return redirect('login')

    return redirect('home')

def logout_view(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('home')

