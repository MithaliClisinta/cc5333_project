from django.db import models
from django.urls import reverse
from django.utils import timezone
from account.models import User

department = (
    ('Dentistry', "Dentistry"),
    ('Cardiology', "Cardiology"),
    ('ENT Specialists', "ENT Specialists"),
    ('Astrology', 'Astrology'),
    ('Neuroanatomy', 'Neuroanatomy'),
    ('Blood Screening', 'Blood Screening'),
    ('Eye Care', 'Eye Care'),
    ('Physical Therapy', 'Physical Therapy'),
)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=100)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    qualification_name = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    department = models.CharField(choices=department, max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    # return reverse('appointment:delete-appointment', kwargs={'pk': self.pk})


class TakeAppointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    message = models.TextField()
    phone_number = models.CharField(max_length=120)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.full_name


class DocAppointment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=10, unique=True)
    end_time = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.full_name    


class symptoms(models.Model):
    symptoms = models.TextField()
    prescription = models.CharField(max_length=120)
    prescribed_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.symptoms    
    
