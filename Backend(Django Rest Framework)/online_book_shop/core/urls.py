
from django.http import HttpResponse
from django.urls import path

from .views import apage






urlpatterns = [
    path('a/', apage),
]