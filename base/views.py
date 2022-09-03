from contextlib import redirect_stderr
from pickletools import read_uint1
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
        password = request.POST.get('password')
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
    form = forms.AddItem()
    if request.method == 'POST':
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
    context =  {'items':items, 'form':form}
    return render(request, 'home.html', context)


def delete(request, pk):
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