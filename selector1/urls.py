from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'select1'

urlpatterns = [
    path('',
         views.Select1View,
         name='select1'),
    ]
