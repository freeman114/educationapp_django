from django.conf.urls import include, url

urlpatterns = [
    url(r'^IsTenantAvailable', include('Account.urls'))
]
