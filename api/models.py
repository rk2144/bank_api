

from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=100)
    

class Branch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    

class Account(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=50)
    