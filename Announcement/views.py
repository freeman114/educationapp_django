from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def createannouncement_view(request):
    return HttpResponse("createannouncement")


def publishannouncement_view(request):
    return HttpResponse("publishannouncement")


def archiveannouncement_view(request):
    return HttpResponse("archiveannouncement")

def getallannouncements_view(request):
    return HttpResponse("getallannouncements")


def getmasterannouncements_view(request):
    return HttpResponse("getmasterannouncements")

def getannouncement_view(request):
    return HttpResponse("getannouncement")


def deleteannouncement_view(request):
    return HttpResponse("deleteannouncement")
