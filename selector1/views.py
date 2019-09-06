from django.shortcuts import render
from .models import City
# Create your views here.

def Select1View(request):
    cities = City.objects.all()
    return render(request, 'index.html', {'cities': cities})
