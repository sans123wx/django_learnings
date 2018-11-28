from django.urls import path
from .views import *

urlpatterns = [
        path('' , monitor , name = 'monitor'),
    ]
