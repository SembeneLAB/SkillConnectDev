from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('accounts/login/', views.signin, name='signin')
]