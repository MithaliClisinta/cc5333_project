"""
doctor_appointment_system URL Configuration

"""

from django.urls import path
from appointment.views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'appointment'

urlpatterns = [

                  path('', HomePageView.as_view(), name='home'),
                  path('service', ServiceView.as_view(), name='service'),
                  path('doctor/appointment/create', AppointmentCreateView.as_view(), name='doctor-appointment-create'),
                  path('doctor/appointment/', AppointmentListView.as_view(), name='doctor-appointment'),
                  path('patient/appointment/', DocAppointmentListView.as_view(), name='patient-appointment'),
                  path('patient/symptoms/', symptomsListView.as_view(), name='patient-symptoms'),
                  path('patient/prescription/', updatesymptoms.as_view(), name='update-symptoms'),
                  path('patient/diagnosis&treatment/create', symptomsView.as_view(), name='patient-symptoms-create'),
                  path('<pk>/delete/', AppointmentDeleteView.as_view(), name='delete-appointment'),
                  path('<pk>/patient/delete', PatientDeleteView.as_view(), name='delete-patient'),
                  path('patient/appointment/create', TakeAppointmentView.as_view(), name='take-appointment'),
                  path('patient/appointment/', AppointmentListView.as_view(), name='book_appointment'),
                  path('search/', SearchView.as_view(), name='search'),
                  path('patient/', PatientListView.as_view(), name='patient-list'),
                  path('doctor/', DoctorListView.as_view(), name='doctor-list'),
   
    
    #path('patients/<int:appointment_id>', PatientPerAppointmentView.as_view(), name='patient-list'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
