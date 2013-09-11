from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    
    wpibox = models.IntegerField(null=True,blank=True)
    phone = models.CharField(max_length=24,null=True,blank=True)
    addr = models.TextField(null=True,blank=True)
    
    @property
    def fullname(self):
        return self.user.first_name + " " + self.user.last_name
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)