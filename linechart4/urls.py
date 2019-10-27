from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'linechart4'

urlpatterns = [
    path('',
         views.LineChart4View,
         name='linechart4'),
    ]
