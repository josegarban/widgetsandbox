from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'linechart1'

urlpatterns = [
    path('',
         views.LineChart1View,
         name='linechart1'),
    ]
