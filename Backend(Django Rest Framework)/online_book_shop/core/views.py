
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def apage(request):
    return HttpResponse("<h1>ok</h1>")


