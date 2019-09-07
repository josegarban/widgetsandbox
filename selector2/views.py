from django.shortcuts import render
from .models import MyDate
# Create your views here.

def Select2View(request):
    model       = MyDate
    template    = 'select2.html'
    objects     = model.objects.all()
    return render(request, template, {'objects': objects})
