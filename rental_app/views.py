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
    item.quantity -= 1
    item.save()
    return redirect('django_page:rent')
