from django.contrib import admin

# admin.py

from django.contrib import admin
from .models import CustomUser, Resume, Skill, TypeSkill, WorkExperience, Education, Project, Certification, AdditionalInformation, Reference

admin.site.register(Resume)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(TypeSkill)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(AdditionalInformation)
admin.site.register(Reference)
admin.site.register(CustomUser)
