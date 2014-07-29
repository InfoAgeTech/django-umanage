from django.conf.urls import patterns
from django.conf.urls import url

from .views import ChangePasswordView


urlpatterns = patterns('',
    url(r'^/change-password/?$', ChangePasswordView.as_view(), name='umanage_change_password'),
)
