from django.contrib import admin
from .models import City
#admin.site.register(Post)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display  = ('name', 'longitude', 'latitude',)
