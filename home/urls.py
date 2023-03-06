from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = "home"

urlpatterns = [
  path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)