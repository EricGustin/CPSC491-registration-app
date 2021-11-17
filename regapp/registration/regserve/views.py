from django.shortcuts import render
from django.http import HttpResponse

# Create your views (handlers) here.

def index(request):
    return HttpResponse("Response from Django backend.")