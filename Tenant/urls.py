from django.conf.urls import include, url
from django.urls import path
from Tenant.views import *

urlpatterns = [
    path('Create/', create_view, name='Create_view'),
    path('ActivateTenant/', activatetenant_view, name='InviteUser_view')
]
