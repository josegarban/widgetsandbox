from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'annotatedtimeline'

urlpatterns = [
    path('',
         views.AnnotatedTimelineView,
         name='annotatedtimeline'),
    ]
