from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from .forms import ProfileForm, SignUpForm
from accounts.models import Profile


def register(request):
    if request.method == 'POST':
        user_form = SignUpForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            username = user_form.cleaned_data.get('username')
            user_profile = Profile(user=user)
            profile_form = ProfileForm(request.POST, instance=user_profile)
            profile_form.save()
            messages.info(request, "Your account has been successfully created!")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('camper:list')
        else:
            messages.error(request, "Correct the errors below")
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/register.html', context)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('camper:list')
            else:
                messages.error(request, f"Invalid username or password")
        else:
            messages.error(request, f"Invalid username or password")
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, "You are logged out successfully!")
    return redirect('accounts:login')
    

    