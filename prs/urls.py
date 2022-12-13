from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from clinic.views import clinic, patient, doctor

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('clinic.urls')),
    path('', include('account.urls')),
    path('', include('appointment.urls')),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
