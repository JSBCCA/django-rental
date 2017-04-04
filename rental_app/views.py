from django.shortcuts import render, redirect
from .models import Item
from django.contrib import messages

# Create your views here.
def about(request):
    return render(request, 'rental_app/about.html', {})

def rent(request):
    items = Item.objects.all()
    return render(request, 'rental_app/rent.html', {"items":items})

def rented(request, id):
    item = Item.objects.get(pk=id)
    if item.num_in_stock > 0:
        item.num_in_stock -= 1
        messages.success(request, "You have rented " + item.name + "!")
    item.save()
    return redirect('django_rental:rent')

def returned(request, id):
    item = Item.objects.get(pk=id)
    if item.num_in_stock < item.max_stock:
        item.num_in_stock += 1
    messages.success(request, "You have returned " + item.name + "!")
    item.save()
    return redirect('django_rental:rent')
