from django.shortcuts import render
from django.http import HttpResponse
from .models import Articolo, Giornalista

def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage.html", context)
# Create your views here.