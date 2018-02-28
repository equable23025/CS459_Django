from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
First Name
Last Name
Telephone
Date of Birth
Credit Amount
Profile Image
Memo 500 characters
'''

class Person(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    telephone=models.CharField(max_length=15)
    dob=models.DateField(blank=True, null=True)
    credit_amount=models.DecimalField(max_digits=15, decimal_places=2)

'''
class User(models.Model):
    id
    username=models.CharField(max_length=100)
    password
    email
'''
class Car(models.Model):
    model = models.CharField(max_length=20)
    detail = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return self.model

class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start = models.DateTimeField(blank=True, null=True)
    stop = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)


