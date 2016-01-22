from django.conf.urls import url

from .views import LogoutView


urlpatterns = [
    url(r'^logout/?$', LogoutView.as_view(), name='umanage_logout'),
]
