from __future__ import unicode_literals

from django.shortcuts import redirect
from umanage.models import TokenAuthorization


class AuthorizationTokenRequiredViewMixin(object):
    """View mixin that requires an authorization token."""
    authorization_class = TokenAuthorization
    authorization = None
    authorization_user = None
    authorization_token_url_kwarg = 'authorization_token'

    def dispatch(self, request, *args, **kwargs):

        auth_class = self.get_authorization_class()
        auth_user = self.get_authorization_user()
        auth_kwargs = {
            'token': kwargs.get(self.authorization_token_url_kwarg)
        }

        if auth_user and auth_user.is_authenticated():
            auth_kwargs['created_user'] = self.get_authorization_user()

        self.authorization = auth_class.objects.get_by_token_or_404(
            **auth_kwargs
        )

        if self.authorization.is_expired():
            return redirect(self.get_auth_expired_url())

        return super(AuthorizationTokenRequiredViewMixin,
                     self).dispatch(request, *args, **kwargs)

    def get_authorization_user(self, **kwargs):
        """Gets the user the authorization object is for."""
        if self.authorization_user is not None:
            return self.authorization_user

        self.authorization_user = self.request.user
        return self.request.user

    def get_authorization_class(self):
        return self.authorization_class

    def get_auth_expired_url(self):
        return reversed('umanage_token_expired')

    def get_context_data(self, *args, **kwargs):
        context = super(AuthorizationTokenRequiredViewMixin,
                        self).get_context_data(*args, **kwargs)
        context['authorization'] = self.authorization
        return context
