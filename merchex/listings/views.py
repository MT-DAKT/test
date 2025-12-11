from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band

# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""<h1>hello django!</h1>
                        <p>Mes groupes préférés sont:</p>
                        <u>
                        <li>{bands[0].name}</li>
                        <li>{bands[1].name}</li>
                        <li>{bands[2].name}</li>
                        </u>""")

def about(request):
    return HttpResponse('<h1>A propos</h1>  <p>Nous adorons merch !</p>' )