from django.shortcuts import render

from jobs.models import Job

# Create your views here.
def index(request):
  job = Job.objects.all()
  context = {
        'job' : job}
       
  return render(request, 'index.html', context)