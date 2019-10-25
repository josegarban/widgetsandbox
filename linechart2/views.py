from django.shortcuts import render

# Create your views here.

def LineChart2View(request):
    template    = 'linechart2.html'

    return render(request, template, {'objects': "objects"})
