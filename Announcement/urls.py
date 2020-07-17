from django.conf.urls import include, url
from django.urls import path
from Announcement.views import *

urlpatterns = [
    path('CreateAnnouncement/', createannouncement_view, name='CreateAnnouncement_view'),
    path('PublishAnnouncement/', publishannouncement_view, name='PublishAnnouncement_view'),
    path('ArchiveAnnouncement/', archiveannouncement_view, name='ArchiveAnnouncement_view'),
    path('GetAllAnnouncements/', getallannouncements_view, name='GetAllAnnouncements_view'),
    path('GetMasterAnnouncements/', getmasterannouncements_view, name='GetMasterAnnouncements_view'),
    path('GetAnnouncement/', getannouncement_view, name='GetAnnouncement_view'),
    path('DeleteAnnouncement/', deleteannouncement_view, name='DeleteAnnouncement_view')
]
