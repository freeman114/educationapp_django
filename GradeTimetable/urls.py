from django.conf.urls import include, url
from django.urls import path
from GradeTimetable.views import *

urlpatterns = [
    path('CreateGradeTimetable/', creategradetimetable_view, name='CreateGradeTimetable_view'),
    path('DeleteGradeTimetable/', deletegradetimetable_view, name='DeleteGradeTimetable_view'),
    path('GetGradeTimetable/', getgradetimetable_view, name='GetGradeTimetable_view'),
    path('GetGradeTimetables/', getgradetimetables_view, name='GetGradeTimetables_view'),
    path('UpdateGradeTimetable/', updategradetimetable_view, name='UpdateGradeTimetable_view'),
]
