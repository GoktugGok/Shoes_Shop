from django.db import models
from django.contrib.auth.models import User
import random
from django.utils import timezone


def generate_random_number():
    return str(random.randint(100000000, 999999999))

class UserOrder(models.Model):
    users = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    productB = models.CharField(max_length=50,null=True)
    number = models.CharField(max_length=50,null=True)
    random_number = models.CharField(max_length=9, default=generate_random_number)
    payName = models.CharField(max_length=50,null=True)
    payEmail = models.EmailField(null=True)
    payAddress = models.CharField(max_length=100,null=True)
    paycardNumber = models.CharField(max_length=16,null=True)
    deliveryPrice = models.CharField(max_length=50,null=True)
    created = models.DateTimeField(auto_now_add=True)





    

