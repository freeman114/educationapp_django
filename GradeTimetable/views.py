
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def creategradetimetable_view(request):
    return HttpResponse("creategradetimetable")


def deletegradetimetable_view(request):
    return HttpResponse("deletegradetimetable")


def getgradetimetable_view(request):
    return HttpResponse("getgradetimetable")

def getgradetimetables_view(request):
    return HttpResponse("getgradetimetables")


def updategradetimetable_view(request):
    return HttpResponse("updategradetimetable")

