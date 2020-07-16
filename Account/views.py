from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def IsTenantAvailable_view(request):
    return HttpResponse("Hello, this is account app.")
