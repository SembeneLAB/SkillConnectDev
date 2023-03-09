import datetime
from django.db import models
from django.contrib.auth.models import User


    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    country = models.CharField(max_length=255, default='')
    role = models.CharField(max_length=100, default='')
    skills = models.TextField(default='') #user will choose among different skills
    aboutme = models.TextField(default='')
    job_type = models.CharField(max_length=100, null=True) #part time or full time
    years_of_experience = models.PositiveSmallIntegerField(null=True) #number of years of work experience
    education = models.CharField(max_length=255, default='') #user will choose among different different education
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    cv = models.FileField(upload_to='pdfs/', default='') #user will upload cv in pdf format
    


class Job(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    requirements = models.TextField(default='')
    location = models.CharField(max_length=255, default='')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    job = models.CharField(max_length=100, default='')
    role = models.CharField(max_length=100, default='')
    Job_type = models.CharField(max_length=100, null=True) #part time or full time
    language = models.CharField(max_length=255, default='')
    years_of_experience = models.PositiveSmallIntegerField(null=True)
    deadline = models.DateField(null=True)
    company_name = models.CharField(max_length=100, default='')
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    
class Application(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE, null=True)
    applicant = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)
    
class Company(models.Model):
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    website = models.URLField(null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)