from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.CharField('TYPE', max_length=1)
    email = models.CharField('EMAIL', max_length=100, default='')
    age = models.IntegerField('AGE', default=0)
    gender = models.CharField('GENDER', max_length=2)
    create_date = models.DateTimeField('CREATE_DATE', auto_now_add=True)
    status = models.CharField('STATUS', max_length=1, default='Y')
    email = models.EmailField('email address', unique=True)