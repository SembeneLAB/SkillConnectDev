from django.contrib import admin
from .models import Job, Application, Company, Profile

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'salary', 'deadline', 'company')

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'website', 'logo')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'country', 'role', 'job_type', 'years_of_experience', 'education')

admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Profile, ProfileAdmin)
