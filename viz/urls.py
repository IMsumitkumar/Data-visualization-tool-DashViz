from django.urls import path
from .views import *

urlpatterns = [
    path('', visual, name='visual'),
]