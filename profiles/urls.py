from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = "profiles"

urlpatterns = [
  path('candidate_details/<int:id>/', views.candidate_details, name='candidate_details'),
  path('create_profile/', views.create_profile, name='create_profile'),
  path('success/', views.success, name='success'),
  path('dashbord/', views.dashbord, name='dashbord'),
  path('dashbord/None', views.dashbord, name='dashbord'),
  path('test/', views.test, name='test'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)