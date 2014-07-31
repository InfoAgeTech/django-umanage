from __future__ import unicode_literals

from django.conf.urls import patterns
from django.conf.urls import url

from .views import LogoutView


urlpatterns = patterns('',
    url(r'^logout/?$', LogoutView.as_view(), name='umanage_logout'),
)
