from tokenize import Number
from django.db import models

# Create your models here.
class phonebook(models.Model):
    Name=models.CharField(max_length=20)
    Number=models.IntegerField(max_length=20)

def __str__(self):
    return self.name()