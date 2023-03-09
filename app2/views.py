from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def address(request):
    return HttpResponse('<h1>kandathin karayil house</h1>')
