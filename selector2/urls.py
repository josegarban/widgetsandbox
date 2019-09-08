from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'select2'

urlpatterns = [
    path('1/',
         views.Select2_1View,
         name='select2'),
    path('2/',
         views.Select2_2View,
         name='select2'),
    ]
