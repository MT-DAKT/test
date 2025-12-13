from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from listings.models import Band
from listings.forms import BandForm, ContactUsForm
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
           
            subject=f"Message from {form.cleaned_data['name'] or 'anonyme'}",
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['tmodibo078@gmail.com'],
           
            return redirect('contact-success')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', context={'form': form})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail',  band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band-create.html', context={'form': form})


def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band-update.html', {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    
    return render(request, 'listings/band-delete.html', context={'band': band})

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band-list.html', context={'bands': bands})

def band_detailt(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band-detail.html', context={'band': band})

def about(request):
    return HttpResponse('<h1>A propos</h1>  <p>Nous adorons merch !</p>' )