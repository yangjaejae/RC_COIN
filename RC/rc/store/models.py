from django.db import models
from photo.fields import ThumbnailImageField
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    loc = models.CharField(max_length=20)

    def __str__(self):
        return self.loc

class Category(models.Model):
    domain = models.CharField(max_length=20)

    def __str__(self):
        return self.domain

class Store(models.Model):
    name = models.CharField(max_length=100, null=True)
    corporate_number = models.CharField(max_length=12, null=True)
    representative = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    url = models.CharField(max_length=100, null=True)
    opening_hour = models.CharField(max_length=2, null=True)
    opening_minute = models.CharField(max_length=2, null=True)
    closing_hour = models.CharField(max_length=2, null=True)
    closing_minute = models.CharField(max_length=2, null=True)
    description = models.TextField(blank=True)
    registered_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.name