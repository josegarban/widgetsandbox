from django.shortcuts import render

# Create your views here.

def AnnotatedTimelineView(request):
    template    = 'annotatedtimeline1.html'

    return render(request, template, {'objects': "objects"})
