# models.py

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    github = models.CharField(max_length=30, blank=True, null=True)
    linkedin = models.CharField(max_length=30, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return self.username

class Resume(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resumes')
    title = models.CharField(max_length=255, help_text="Title of your resume")
    summary = models.TextField(blank=True, help_text="A brief summary about yourself or this resume")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    libelle_summary = models.CharField(max_length=50, blank=True)
    libelle_education = models.CharField(max_length=50, blank=True)
    libelle_experience = models.CharField(max_length=50, blank=True)
    libelle_project = models.CharField(max_length=50, blank=True)
    libelle_language = models.CharField(max_length=50, blank=True)
    libelle_skill = models.CharField(max_length=50, blank=True)
    libelle_reference = models.CharField(max_length=50, blank=True)
    libelle_certification = models.CharField(max_length=50, blank=True)
    libelle_additional_info = models.CharField(max_length=50, blank=True)
    libelle_interest = models.CharField(max_length=50, blank=True)
    
    template = models.CharField(max_length=10, blank=True)
    colour = models.CharField(max_length=6, blank=True)


    def __str__(self):
        return f"{self.user.username} - {self.title}"

class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_experiences')
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    position = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class WorkExperienceDescription(models.Model):
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE, related_name='descriptions')
    description = models.TextField()
    position = models.IntegerField(default=0)
    def __str__(self):
        return f"Description for {self.work_experience.job_title} at {self.work_experience.company}"
    
class WorkExperienceTool(models.Model):
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE, related_name='tools')
    name = models.CharField(max_length=255)
    position = models.IntegerField(default=0)
    def __str__(self):
        return f"Tool: {self.name} for {self.work_experience.job_title} at {self.work_experience.company}"

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    position = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.degree} in {self.field_of_study} at {self.school}"

class TypeSkill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='type_skills')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.resume})"

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    type_skill = models.ForeignKey(TypeSkill, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=255)
    position = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    position = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    

class ProjectTool(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tools')
    name = models.CharField(max_length=255)
    position = models.IntegerField(default=0)
    def __str__(self):
        return f"Tool: {self.name} for project {self.project.title}"
    

class Certification(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField(max_length=255)
    authority = models.CharField(max_length=255)
    date_earned = models.DateField()
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class AdditionalInformation(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='additional_info')
    information = models.TextField()
    position = models.IntegerField(default=0)
    def __str__(self):
        return "Additional Info"

class Reference(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15,  blank=True)
    email = models.EmailField(null=True, blank=True)
    company = models.CharField(max_length=255, blank=True)
    position = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.relationship})"
    

class Language(models.Model):
    LANGUAGE_LEVELS = (
        ('basic', 'Basic'),
        ('fluent', 'Fluent'),
        ('native', 'Native/Bilingual'),
    )
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=15, choices=LANGUAGE_LEVELS)
    position = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.get_proficiency_display()})"

class Interest(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='interests')
    name = models.CharField(max_length=255)
    position = models.IntegerField(default=0)

    def __str__(self):
        return self.name