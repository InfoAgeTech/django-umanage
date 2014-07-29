from django.conf.urls import patterns
from django.conf.urls import url

from .views import ForgotUsernameSentView
from .views import ForgotUsernameView


urlpatterns = patterns('',
    url(r'^forgot-username/?$', ForgotUsernameView.as_view(), name='umanage_forgot_username'),
    url(r'^forgot-username/sent/?$', ForgotUsernameSentView.as_view(), name='umanage_forgot_username_sent'),
)
