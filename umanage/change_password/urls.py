from django.conf.urls import patterns
from django.conf.urls import url

from .views import ChangePasswordSuccessView
from .views import ChangePasswordView
from .views import SetPasswordView


urlpatterns = patterns('',
    url(r'^/change-password/?$', ChangePasswordView.as_view(), name='umanage_change_password'),
    url(r'^/change-password/success/?$', ChangePasswordSuccessView.as_view(), name='umanage_change_password_success'),
    url(r'^/set-password/?$', SetPasswordView.as_view(), name='umanage_set_password'),
)
