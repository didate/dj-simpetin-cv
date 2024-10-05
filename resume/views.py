from django.shortcuts import get_object_or_404, render, redirect
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

def resume_detail(request, resume_id):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if not logged in

    # Get the resume for the authenticated user
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)

    # Filter the skills
    technical_skills = resume.skills.filter(skill_type='technical')
    soft_skills = resume.skills.filter(skill_type='soft')

    return render(request, 'resume/resume_detail.html', {
        'resume': resume,
        'technical_skills': technical_skills,
        'soft_skills': soft_skills,
    })