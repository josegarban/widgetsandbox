from django.shortcuts import render

# Create your views here.

def LineChart4View(request):
    template    = 'linechart4.html'

    return render(request, template, {'objects': "objects"})
