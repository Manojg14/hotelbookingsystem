from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.forms import UserCreationForm


# Create your models here.
class Userdetails(models.Model):
    
    name = models.CharField(max_length = 100)
    address = models.TextField()
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    pincode = models.CharField(max_length = 10)
    phonenumber = models.CharField(max_length = 20)
    emailid = models.EmailField(max_length = 30)
    date = models.DateField()
    time = models.TimeField()
    adults = models.PositiveSmallIntegerField()
    kids = models.PositiveSmallIntegerField(blank=True, null=True)
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
    ]
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    specialrequest = models.CharField(max_length = 100)
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)  
    content = models.TextField(blank=True, null=True)  
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    


    
