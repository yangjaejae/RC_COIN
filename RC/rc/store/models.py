from django.db import models

# Create your models here.

class Location(models.Model):
    loc = models.CharField('LOCATION', max_length=20)

class Category(models.Model):
    domain = models.CharField('CATEGORY', max_length=20)

class Store(models.Model):
    name = models.CharField('NAME', max_length=100)
    description = models.TextField('DESCRIPTION')
    img = models.CharField('IMG', max_length=100)
    location = models.ForeignKey(Location, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    status = models.CharField('STATUS', max_length=1, default='Y')