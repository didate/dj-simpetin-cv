from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from resume.models import Resume
from resume.signup_form import CustomUserCreationForm

def home_view(request):
    return render(request, 'resume/home.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signup
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to the homepage after signup
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'resume/signup.html', {'form': form})


def resume_list(request):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if not logged in

    # Get all resumes for the authenticated user
    resumes = Resume.objects.filter(user=request.user)

    return render(request, 'resume/resume_list.html', {'resumes': resumes})