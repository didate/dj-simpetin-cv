from django.contrib import admin

# admin.py

from django.contrib import admin
from .models import Resume, WorkExperience, Education, Skill, Project, Certification, AdditionalInformation, Reference

admin.site.register(Resume)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(AdditionalInformation)
admin.site.register(Reference)
