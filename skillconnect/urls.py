from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='index')),
    
    path('', include('companies.urls', namespace='create_job')),
    path('', include('companies.urls', namespace='create_job_success')),

 
    path('', include('users.urls', namespace="signin")),
    path('', include('users.urls', namespace="signup")),
    
    path('', include('jobs.urls', namespace="job_details")),  
    path('', include('jobs.urls', namespace="job_list")),
    path('', include('jobs.urls', namespace="apply")),
    #path('', include('jobs.urls', namespace="test")),
    
    path('', include('profiles.urls', namespace="candidate_details")),  
    path('', include('profiles.urls', namespace="create_profile")),
    path('', include('profiles.urls', namespace="success")),
    path('', include('profiles.urls', namespace="dashbord")),
    path('', include('profiles.urls', namespace="test")),


    

    

]
