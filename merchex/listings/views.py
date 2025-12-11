from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', context={'bands': bands})

def about(request):
    return HttpResponse('<h1>A propos</h1>  <p>Nous adorons merch !</p>' )