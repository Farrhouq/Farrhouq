from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    deadline = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    created = models.DateTimeField(auto_now=True)
     
    def __str__(self) -> str:
        return self.name 

class Room(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    