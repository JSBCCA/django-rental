from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'rental_app/about.html', {})

def rent(request):
    return render(request, 'rental_app/rent.html', {})