"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',
         admin.site.urls),
    path('selector1/',
         include('selector1.urls', namespace = 'selector1')),
    path('selector2/',
         include('selector2.urls', namespace = 'selector2')),
    path('linechart1/',
         include('linechart1.urls', namespace = 'linechart1')),
    path('linechart2/',
         include('linechart2.urls', namespace = 'linechart2')),
    path('linechart3/',
         include('linechart3.urls', namespace = 'linechart3')),
    path('annotatedtimeline1/',
         include('annotatedtimeline1.urls', namespace = 'annotatedtimeline1')),
    path('annotatedtimeline2/',
         include('annotatedtimeline2.urls', namespace = 'annotatedtimeline2')),
     ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
