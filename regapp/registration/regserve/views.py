from django.shortcuts import render
from django.http import HttpResponse

# views (handlers) go here.

def index(request):
    return HttpResponse("Response from Django backend.")