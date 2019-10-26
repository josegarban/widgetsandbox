from django.shortcuts import render

# Create your views here.

def LineChart3View(request):
    template    = 'linechart3.html'

    return render(request, template, {'objects': "objects"})
