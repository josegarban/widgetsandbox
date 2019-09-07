from django.contrib import admin
from .models import MyDate

@admin.register(MyDate)
class MyDateAdmin(admin.ModelAdmin):
    list_display  = ('mydate',)
