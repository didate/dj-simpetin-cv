# models.py

from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    title = models.CharField(max_length=255, help_text="Title of your resume")
    summary = models.TextField(blank=True, help_text="A brief summary about yourself or this resume")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"

class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_experiences')
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.degree} in {self.field_of_study} at {self.school}"

class Skill(models.Model):
    SKILL_TYPES = (
        ('soft', 'Soft Skill'),
        ('technical', 'Technical Skill'),
    )
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=255)
    skill_type = models.CharField(max_length=10, choices=SKILL_TYPES)

    def __str__(self):
        return f"{self.get_skill_type_display()}: {self.name}"

class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class Certification(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=255)
    authority = models.CharField(max_length=255)
    date_earned = models.DateField()

    def __str__(self):
        return self.name

class AdditionalInformation(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='additional_info')
    information = models.TextField()

    def __str__(self):
        return "Additional Info"

class Reference(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15,  blank=True)
    email = models.EmailField(null=True, blank=True)
    company = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name} ({self.relationship})"