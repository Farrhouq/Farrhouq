from contextlib import redirect_stderr
from multiprocessing import context
from pickletools import read_uint1
from unicodedata import name
from django.shortcuts import render,redirect
from . import models
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


# Create your views here.

def loginUser(request):
    form = forms.UserForm()
    if request.method == 'POST':
        name = request.POST.get('username')
        user = User.objects.get(username=name)
        if user.username != '':
            login(request, user)
            return redirect('home')
    context = {'form':form, }
    return render(request, 'login.html', context)


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('home')
    context = {'form':form}
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def home_page(request):
    items = request.user.item_set.all()
    rooms = request.user.room_set.all()
    form = forms.AddItem()
    form2 = forms.RoomForm()
    if request.method == 'POST':
        if request.POST.get("form_type") == 'formOne':
           user = request.user
           name = request.POST.get('name')
           deadline = request.POST.get('deadline')
           models.Item.objects.create(
               name = name,
               deadline = deadline,
               owner = user,
            )
           if form.is_valid():
               form.save()
        elif request.POST.get("form_type") == 'formTwo':
            form2 = forms.RoomForm()
            if request.method == 'POST':
                room_name = request.POST.get('name')
                models.Room.objects.create(
                    name=room_name,
                    user = request.user,
                )
                if form.is_valid():
                    form.save()
    context =  {'items':items, 
        'form':form,
        'rooms':rooms,
        'form2':form2,
        }
    return render(request, 'home.html', context)


def addItem(request, pk):
    item = models.RoomItem.objects.get(id=pk)
    room = item.room
    user = request.user
    name = item
    deadline = 'One Month'
    models.Item.objects.create(
        name = name,
        deadline = deadline,
        owner = user,
        )
    return redirect('room', room.id)


def delete_item(request, pk):
    item = models.Item.objects.get(id=pk)
    item.delete()
    return redirect('home')


def update_item(request, pk):
    item = models.Item.objects.get(id=pk)
    form = forms.AddItem(instance=item)
    if request.method == 'POST':
        name = request.POST.get('name')
        deadline = request.POST.get('deadline')
        item.name = name
        item.deadline = deadline
        item.save()
        return redirect('home')
    items = models.Item.objects.all()
    context =  {'items':items, 'form':form}
    return render(request, 'update_item.html', context)


def createRoom(request):
    form = forms.RoomForm
    if request.method == 'POST':
        room_name = request.POST.get('name')
        models.Room.objects.create(
            name=room_name,
            user = request.host,
            )
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'rooms.html', context)


def deleteRoom(request, pk):
    room = models.Room.objects.get(id=pk)
    room.delete()
    return redirect('home')

def updateRoom(request, pk):
    room = models.Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'updateRoom.html', context)

def room(request, pk):
    room = models.Room.objects.get(id=pk)
    room_items = room.roomitem_set.all()
    form = forms.RoomItemForm()
    if request.method == 'POST':
        room_item_name = request.POST.get('name')
        models.RoomItem.objects.create(
            name = room_item_name,
            room = room,
        )
        if form.is_valid():
            form.save()
    context = {
        'room':room,
        'room_items':room_items,
        'form':form,
    }
    return render(request, 'room.html', context)
    

def deleteRoomItem(request, pk):
    room_item = models.RoomItem.objects.get(id=pk)
    room = room_item.room
    room_item.delete()
    return redirect('room', room.id)