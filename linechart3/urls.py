from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'linechart3'

urlpatterns = [
    path('',
         views.LineChart3View,
         name='linechart3'),
    ]
