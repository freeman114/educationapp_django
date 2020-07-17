from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def istenantavailable_view(request):
    return HttpResponse("IsTenantAvailable")


def inviteuser_view(request):
    return HttpResponse("InviteUser")


def activateuser_view(request):
    return HttpResponse("ActivateUser")
