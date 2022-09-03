from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    deadline = models.CharField(max_length=30)
     
    def __str__(self) -> str:
        return self.name 