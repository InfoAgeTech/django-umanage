from django.conf.urls import include
from django.conf.urls import url

from .views import TokenExpiredView


urlpatterns = [
    url(r'^/token-expired/?$', TokenExpiredView.as_view(), name='umanage_token_expired'),
    url(r'', include('umanage.accounts.urls')),
    url(r'', include('umanage.activate_account.urls')),
    url(r'', include('umanage.change_email.urls')),
    url(r'', include('umanage.change_password.urls')),
]
