from django.shortcuts import render
from django.http import HttpResponse
from .models import Uslug, Gorod, Cruise, Booking

def index(request):
    uslugi = Uslug.objects.all()
    gorodi = Gorod.objects.all()
    cruises = Cruise.objects.all()
    bookings = Booking.objects.all()
    return render(request,'main/index.html',{'uslugi':uslugi,'gorodi':gorodi,'cruises':cruises,'bookings':bookings})

