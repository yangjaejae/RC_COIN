from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(blank=True)
    gender = models.CharField(max_length=2)
    birth_year = models.CharField(max_length=4)
    birth_month = models.CharField(max_length=2)
    birth_date = models.CharField(max_length=2)
    type = models.IntegerField(default=2)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.profile.gender = instance.gender
        instance.profile.birth_year = instance.birth_year
        instance.profile.birth_month = instance.birth_month
        instance.profile.birth_date = instance.birth_date
        instance.profile.type = instance.type
        instance.profile.status = instance.status
    instance.profile.save()
