from django.conf.urls import include, url
from Account.views import *

urlpatterns = [
    url(r'^IsTenantAvailable', istenantavailable_view, name="IsTenantAvailable_view"),
    url(r'^InviteUser', inviteuser_view, name='InviteUser_view'),
    url(r'^ActivateUser', activateuser_view, name='ActivateUser_view')
]
