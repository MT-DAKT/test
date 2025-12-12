from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.forms import ContactUsForm

def contact(request):
    form = ContactUsForm()
    return render(request, 'listings/contact.html', context={'form': form})

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band-list.html', context={'bands': bands})

def band_detailt(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band-detail.html', context={'band': band})

def about(request):
    return HttpResponse('<h1>A propos</h1>  <p>Nous adorons merch !</p>' )