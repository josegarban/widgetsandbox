from django.shortcuts import render

# Create your views here.

def LineChart1View(request):
    template    = 'linechart1.html'

    return render(request, template, {'objects': "objects"})
