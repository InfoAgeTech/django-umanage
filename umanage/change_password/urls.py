from django.conf.urls import patterns
from django.conf.urls import url

from .views import ChangePasswordSuccessView
from .views import ChangePasswordView


urlpatterns = patterns('',
    url(r'^/change-password/?$', ChangePasswordView.as_view(), name='umanage_change_password'),
    url(r'^/change-password/success/?$', ChangePasswordSuccessView.as_view(), name='umanage_change_password_success'),
)
