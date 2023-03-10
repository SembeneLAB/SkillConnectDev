from cProfile import Profile
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from jobs.models import Application, Company, Job, Profile

# Create your views here.
def job_details(request, id):
  
  try:
       job = get_object_or_404(Job, id=id)
  except Http404:
        # Handle the 404 error here (e.g., display a custom error message)
        return render(request, 'error_404.html')
      
      
  return render(request, 'job-details.html', {'job': job})


def job_list(request):
  job = Job.objects.all()
  context = {
        'job' : job}
       
  return render(request, 'job-list.html', context)



#@login_required
#def apply(request, job_id):
    # Get the current user's profile
    #profile = Profile.objects.get(user=request.user)
    #profile = Profile.objects.get(user=request.user)
    #user_profile = get_object_or_404(Profile, pk=profile.pk)

    # Get the company the user wants to apply to
    #job = get_object_or_404(Job, id=job_id)

    # Create a new application object and render the application form
    #application = Application(applicant=user_profile, job=job)
    
    
    #application.save()
    
    #context = {
    #    'job': job }

    # Render the application form
    #return render(request, 'success.html', context)
  
  
  
  
@login_required 
def apply(request, job_id):
    profile = Profile.objects.get(user=request.user)
    user_profile = get_object_or_404(Profile, pk=profile.pk)
    try:
        # Check if the application already exists
        existing_application = Application.objects.get(job=job_id, applicant=user_profile)
        return existing_application
    except Application.DoesNotExist:
        # Create a new application
        job = get_object_or_404(Job, id=job_id)
        application = Application(job=job, applicant=user_profile)
        application.save()
        context = {
        'job': job }
        
      
        
    return render(request, 'success.html', context)

  

#def test(request):   
  
  
    
  #return render(request, 'test.html')
