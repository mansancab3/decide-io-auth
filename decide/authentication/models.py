from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
   SEX_CHOICES = (
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
   )
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   sex = models.TextField(max_length=500, choices=SEX_CHOICES, default='Hombre')
   location = models.CharField(max_length=30, blank=True)
   birth_date = models.DateField(null=True, blank=True)

   def _str_(self):
   		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
