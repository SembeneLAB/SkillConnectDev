from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = "job"

urlpatterns = [
  path('job_details/<int:id>/', views.job_details, name='job_details'),
  path('job_list/', views.job_list, name='job_list'),
  path('apply/<int:job_id>/', views.apply, name='apply'),
  #path('test/', views.test, name='test'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)