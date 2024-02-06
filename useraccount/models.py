from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
     STATUS_CHOICES = (
         ("Male","MALE"), 
         ("Female", "FEMALE"), 
         ("Other", "OTHER")
         )
     user = models.OneToOneField(User, on_delete=models.CASCADE)    
     full_name = models.CharField(max_length=255, null=True, blank=True)
     email = models.EmailField(null=True, blank=True)
     dob = models.DateField(null=True, blank=True)
     gender = models.CharField(max_length=255,choices=STATUS_CHOICES, null=True, blank=True)
     contact = models.CharField(max_length=255, null=True, blank=True)
     address = models.CharField(max_length=255, null=True, blank=True)
     image = models.ImageField(upload_to="user_image/", null=True, blank=True)

     def __str__(self):
         return str(self.user)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email)
        instance.profile.save()