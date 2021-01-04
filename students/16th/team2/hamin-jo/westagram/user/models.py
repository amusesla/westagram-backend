from django.db import models

class User(models.Model):
    name     = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
    email    = models.CharField(max_length=50, null=True)
    phone    = models.IntegerField(null=True)