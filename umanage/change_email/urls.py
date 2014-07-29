from django.conf.urls import patterns
from django.conf.urls import url

from .views import ChangeEmailActivationView
from .views import ChangeEmailSentView
from .views import ChangeEmailSuccessView
from .views import ChangeEmailView


urlpatterns = patterns('',
    url(r'^/change-email/?$', ChangeEmailView.as_view(), name='umanage_change_email'),
    url(r'^/change-email/sent/?$', ChangeEmailSentView.as_view(), name='umanage_change_email_sent'),
    url(r'^/change-email/success/?$', ChangeEmailSuccessView.as_view(), name='umanage_change_email_success'),
    url(r'^/change-email/(?P<change_email_token>(\w|-)+)/?$', ChangeEmailActivationView.as_view(), name='umanage_change_email_activation'),
)
