from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import UserManager

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    phone_number = models.CharField(unique=True, blank=True, null=True, max_length=20,
                                    error_messages={
                                        'unique': "A user with that phone number already exists."
                                    })

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()
    
    def __str__(self):
        return "{}".format(self.username)
