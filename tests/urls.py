from django.conf.urls import include
from django.conf.urls import url


urlpatterns = [
    url(r'', include('umanage.auth.urls')),
    url(r'', include('umanage.forgot_username.urls')),
    url(r'', include('umanage.forgot_password.urls')),
    url(r'^account', include('umanage.urls')),
]
