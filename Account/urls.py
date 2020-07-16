from django.conf.urls import include, url
from django.urls import path
from Account.views import *

urlpatterns = [
    # url(r'^IsTenantAvailable', include('Account.urls'))
    path('IsTenantAvailable/', IsTenantAvailable_view, name='IsTenantAvailable_view')
]
