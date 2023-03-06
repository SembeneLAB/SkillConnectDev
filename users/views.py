from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import login as dj_login


# Create your views here.

def signup(request):
  
  if (request.method == 'POST'):    
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User.objects.create_user(username, email, password)
    response = redirect('/accounts/login/')
    return response
    
  return render(request, 'sign-up.html')



def signin(request):    
  if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            response = redirect('/create_profile/')
            return response
        else:
            error_message = 'Invalid username or password'
  else:
        error_message = ''
  return render(request, 'sign-in.html', {'error_message': error_message})