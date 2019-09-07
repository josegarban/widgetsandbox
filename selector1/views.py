from django.shortcuts import render
from .models import City
# Create your views here.

def Select1View(request):
    template    = 'select1.html'
    model       = City
    objects     = model.objects.all()
    return render(request, template, {'objects': objects})
