from django.shortcuts import render
from .models import MyDate
# Create your views here.

def Select2_1View(request):
    model       = MyDate
    template    = 'select2_1.html'
    objects     = model.objects.all()
    return render(request, template, {'objects': objects})

def Select2_2View(request):
    model       = MyDate
    template    = 'select2_2.html'
    objects     = model.objects.all()
    return render(request, template, {'objects': objects})

def Select2_3View(request):
    model       = MyDate
    template    = 'select2_3.html'
    objects     = model.objects.all()
    return render(request, template, {'objects': objects})
