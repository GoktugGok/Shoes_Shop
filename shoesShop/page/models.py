from django.db import models
from django.contrib.auth.models import User

class Communication(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField(blank=True, max_length=255)