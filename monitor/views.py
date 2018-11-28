from django.shortcuts import render
from .models import *

# Create your views here.

def monitor(request):
    monitors = Monitor.objects.all()
    context = {}
    context['monitors'] = monitors
    return render(request , 'monitor.html' , context)
