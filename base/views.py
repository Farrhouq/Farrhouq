from contextlib import redirect_stderr
from pickletools import read_uint1
from django.shortcuts import render,redirect
from . import models
from . import forms

# Create your views here.
def home_page(request):
    form = forms.AddItem()
    if request.method == 'POST':
        name = request.POST.get('name')
        deadline = request.POST.get('deadline')
        models.Item.objects.create(
            name = name,
            deadline = deadline,
        )
        if form.is_valid():
            form.save()
    items = models.Item.objects.all()
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