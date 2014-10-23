from __future__ import unicode_literals

from django.conf.urls import patterns
from django.conf.urls import url

from .views import ActivateAccountExpiredView
from .views import ActivateAccountSuccessView
from .views import ActivateAccountView


urlpatterns = patterns('',
    url(r'^/activate/expired/?$', ActivateAccountExpiredView.as_view(), name='umanage_activate_account_expired'),
    url(r'^/activate/success/?$', ActivateAccountSuccessView.as_view(), name='umanage_activate_account_success'),
    url(r'^/activate/(?P<username>[\w.@+-]+)/(?P<authorization_token>(\w|-)+)/?$', ActivateAccountView.as_view(), name='umanage_activate_account'),
)
