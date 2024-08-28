from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    images = models.ImageField(
        upload_to='image/', blank=True, default='../profiles/images/nobody.jpg'
    )

    class Meta:
        ordering =['-create_at']

    def __str__(self):
        return f"{self.owner}'s   "
    

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)   

post_save.connect(create_profile, sender=User)
