from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    is_done = models.BooleanField(default=False)
     
    def __str__(self):
        return self.name 


