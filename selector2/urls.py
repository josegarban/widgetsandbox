from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'select2'

urlpatterns = [
    path('',
         views.Select2View,
         name='select2'),
    ]
