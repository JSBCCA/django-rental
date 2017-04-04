from django.shortcuts import render, redirect
from .models import Item

# Create your views here.
def about(request):
    return render(request, 'rental_app/about.html', {})

def rent(request):
    items = Item.objects.all()
    return render(request, 'rental_app/rent.html', {"items":items})

def rented(request, id):
    item = Item.objects.get(pk=id)
    item.num_in_stock -= 1
    item.save()
    return redirect('django_rental:rent')

def returned(request, id):
    item = Item.objects.get(pk=id)
    item.num_in_stock += 1
    item.save()
    return redirect('django_rental:rent')
