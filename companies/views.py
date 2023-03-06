from django.http import HttpResponse
from django.shortcuts import render, redirect
from jobs.models import Company, Job

def create_job(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        requirements = request.POST.get('requirements')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        language = request.POST.get('language')
        role= request.POST.get('role')
        type= request.POST.get('type')
        deadline= request.POST.get('deadline')
        availability= request.POST.get('availability')
        years_of_experience = request.POST.get('years_of_experience')
        company_id = request.POST.get('company_id')
        
        job = Job.objects.create(
            title=title,
            description=description,
            requirements=requirements,
            location=location,
            salary=salary,
            language=language,
            years_of_experience=years_of_experience,
            role=role,
            type=type,
            deadline=deadline,
            company_id=company_id,
            Job_type=availability
        )
        
        return redirect('success.html')
    
    return render(request, '/hire/')


def success(request):
  return render(request, 'success.html' )


def hire(request):
  company = Company.objects.all()
  context = {
        'company' : company}
       
  return render(request, 'create-job.html', context)