from django.core.urlresolvers import reverse
from django_core.auth.views import AuthorizationTokenRequiredViewMixin


class UmanageAuthorizationTokenRequiredViewMixin(AuthorizationTokenRequiredViewMixin):

    def get_auth_expired_url(self):
        return reverse('umanage_token_expired')
