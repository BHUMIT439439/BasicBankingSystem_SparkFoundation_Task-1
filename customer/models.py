from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    balance = models.IntegerField(default=0)
    account_no = models.IntegerField()