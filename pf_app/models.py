# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class ContactForm(models.Model):

    #This field store Full Name 
    full_name = models.CharField(max_length=300,blank=True)
    #This field store Email ID
    email_id = models.CharField(max_length=300,blank=True)
    #This field store Contact Number 
    contact_number = models.CharField(max_length=300,blank=True)
    #This field store Message 
    message = models.TextField(max_length=3000,blank=True)
    #This field store Date & Time at which form is submitted
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pk) #Return Primary Key

    class Meta:
        verbose_name_plural = "Contact Form Data"
        verbose_name = "Contact Form"

#CustomUser Model
class CustomUser(AbstractUser):

    # Datafields
    SUPER_ADMIN = 1
    ADMIN = 2
    NORMAL_USER = 3
    ROLE_CHOICES = (  
      (SUPER_ADMIN,'super_admin'),
      (ADMIN,'admin'),
      (NORMAL_USER,'normal_user'),
    )
    #This field store User's Role
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,default=NORMAL_USER)
    #This field store User's Name
    name = models.CharField(max_length=264, blank='True')