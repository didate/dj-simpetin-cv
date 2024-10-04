from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def home_view(request):
    return render(request, 'resume/home.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signup
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to the homepage after signup
    else:
        form = UserCreationForm()
    
    return render(request, 'resume/signup.html', {'form': form})
