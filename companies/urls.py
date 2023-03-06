from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = "companies"

urlpatterns = [
  path('create_job', views.create_job, name='create_job'),
  path('create_job/success', views.success, name='create_job_success'),
  path('hire/', views.hire, name='hire'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)