from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'linechart2'

urlpatterns = [
    path('',
         views.LineChart2View,
         name='linechart2'),
    ]
