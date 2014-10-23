from __future__ import unicode_literals

from django.conf.urls import patterns
from django.conf.urls import url

from .views import ForgotPasswordChangePasswordView
from .views import ForgotPasswordChangeSuccessView
from .views import ForgotPasswordExpiredView
from .views import ForgotPasswordSentView
from .views import ForgotPasswordView


urlpatterns = patterns('',
    url(r'^forgot-password/?$', ForgotPasswordView.as_view(), name='umanage_forgot_password'),
    url(r'^forgot-password/expired/?$', ForgotPasswordExpiredView.as_view(), name='umanage_forgot_password_expired'),
    url(r'^forgot-password/sent/?$', ForgotPasswordSentView.as_view(), name='umanage_forgot_password_sent'),
    url(r'^forgot-password/success/?$', ForgotPasswordChangeSuccessView.as_view(), name='umanage_forgot_password_success'),
    url(r'^forgot-password/(?P<username>[\w.@+-]+)/(?P<authorization_token>(\w|-)+)/?$', ForgotPasswordChangePasswordView.as_view(), name='umanage_forgot_password_change_password'),
)
