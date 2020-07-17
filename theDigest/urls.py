"""theDigest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('api/services/app/Account/', include('Account.urls')),
    url(r'^api/services/app/Tenant/', include('Tenant.urls')),
    url(r'^api/services/app/Announcement/', include('Announcement.urls')),
    url(r'^api/services/app/GradeTimetable/', include('GradeTimetable.urls')),
    # url(r'^api/services/app/Homework/', include('Homework.urls')),
    # url(r'^api/services/app/Message/', include('Message.urls')),
    # url(r'^api/services/app/Role/', include('Role.urls')),
    # url(r'^api/services/app/SchoolTerm/', include('SchoolTerm.urls')),
    # url(r'^api/services/app/SchoolVenue/', include('SchoolVenue.urls')),
    # url(r'^api/services/app/Session_Token/', include('Session_Token.urls')),
    # url(r'^api/services/app/Student/', include('Student.urls')),
    # url(r'^api/services/app/Subject/', include('Subject.urls')),
    # url(r'^api/services/app/User/', include('User.urls'))
]
