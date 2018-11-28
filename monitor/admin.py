from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Monitor)
class Monitor(admin.ModelAdmin):
    fields = ('name' , 'ip' , 'date' , 'startime' , 'endtime' , 'used_time')
    list_display = ('name' , 'ip' , 'date' , 'startime' , 'endtime' , 'used_time')
