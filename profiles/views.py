from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from jobs.models import Application, Profile

@login_required
def create_profile(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        country = request.POST['country']
        skills = request.POST['skills']
        job_type = request.POST['availability']
        years_of_experience = request.POST['years_of_experience']
        education = request.POST['education']
        role = request.POST['role']
        aboutme = request.POST['aboutme']
        cv = request.POST['cv']
        linkedin = request.POST['linkedin']
        user = request.user

        profile = Profile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            country=country,
            skills=skills,
            job_type=job_type,
            years_of_experience=years_of_experience,
            education=education,
            cv=cv,
            role=role,
            aboutme = aboutme,
            linkedin=linkedin
        )
        return redirect('/test/')
    else:
        return render(request, 'create-profile.html')


#@login_required
#def update_profile(request, pk):
    # Retrieve the user's profile from the database
    profile = Profile.objects.get(user=request.user, pk=pk)
    
    if request.method == 'POST':
        # Retrieve data from POST request
        profile.name = request.POST.get('name')
        profile.email = request.POST.get('email')
        profile.phone = request.POST.get('phone')
        profile.bio = request.POST.get('bio')
        
        # Save the updated profile object to the database
        profile.save()
        
        # Redirect to user's profile page
        return redirect('account.html', pk=profile.pk)
    
    # If request method is GET, render the update profile template
    return render(request, 'account.html', {'profile': profile})


@login_required
def candidate_details(request, id):
    # Retrieve the user's profile from the database
    try:
        
      profile = get_object_or_404(Profile, id=id, user=request.user)
      
    except Http404:
        # Handle the 404 error here (e.g., display a custom error message)
        return render(request, 'error_404.html')
    
    # Render the profile detail template with the user's profile data
    return render(request, 'candidate-details.html', {'profile': profile})




def dashbord(request):
  job = Application.objects.all()
  context = {
        'job' : job}
  
  return render(request, 'dashbord.html', context)


def success(request):
  return render(request, 'success.html' )

def test(request):
       
  return render(request, 'testc.html')