from __future__ import unicode_literals

from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('',
    url(r'', include('umanage.forgot_username.urls')),
    url(r'', include('umanage.forgot_password.urls')),
    url(r'^account', include('umanage.urls')),
)
