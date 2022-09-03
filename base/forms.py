from dataclasses import fields
import imp
from django.forms import ModelForm
from .models import Item, Room
from django.contrib.auth.models import User

class AddItem(ModelForm):
    class Meta:
        model = Item
        exclude = ['owner']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name']

