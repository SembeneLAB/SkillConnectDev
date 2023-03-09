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
        job= request.POST.get('job')
        deadline= request.POST.get('deadline')
        availability= request.POST.get('availability')
        years_of_experience = request.POST.get('years_of_experience')
        company_id = request.POST.get('company_id')
        company_name = request.POST.get('company_name')

        
        job = Job.objects.create(
            title=title,
            description=description,
            requirements=requirements,
            location=location,
            salary=salary,
            language=language,
            years_of_experience=years_of_experience,
            role=role,
            job=job,
            deadline=deadline,
            company_id=company_id,
            Job_type=availability,
            company_name=company_name,
        )
        
        return redirect('/create_job/success')
    
    return render(request, '/hire/')


def success(request):
  return render(request, 'success.html' )


def hire(request):
  company = Company.objects.all()
  context = {
        'company' : company}
       
  return render(request, 'create-job.html', context)