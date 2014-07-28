from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls import include


urlpatterns = patterns('',
    url(r'', include('umanage.change_email.urls')),
    url(r'', include('umanage.change_password.urls')),
)
