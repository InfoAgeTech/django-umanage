from __future__ import unicode_literals

from django.conf.urls import patterns
from django.conf.urls import url

from .views import AccountEditView
from .views import AccountView


urlpatterns = patterns('',
    url(r'^/?$', AccountView.as_view(), name='umanage_account_view'),
    url(r'^/edit/?$', AccountEditView.as_view(), name='umanage_account_edit'),
)
