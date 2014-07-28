from django.conf.urls import patterns
from django.conf.urls import url

from .views import ChangeEmailActivationView
from .views import ChangeEmailView


urlpatterns = patterns('',
#     url(r'^/add/?$', SlideAssetAddView.as_view(), name='slide_asset_add'),
    url(r'^/change-email/?$', ChangeEmailView.as_view(), name='umanage_change_email'),
    url(r'^/change-email/(?P<change_email_token>(\w|-)+)/?$', ChangeEmailActivationView.as_view(), name='umanage_change_email_activation'),
#     url(r'^/(?P<slide_asset_id>\d+)/?$', SlideAssetView.as_view(), name='slide_asset_view'),
#     url(r'^/(?P<slide_asset_id>\d+)/edit/?$', SlideAssetEditView.as_view(), name='slide_asset_edit'),
)
