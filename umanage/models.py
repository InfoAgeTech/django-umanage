from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django_core.models import TokenAuthorization


class AccountActivationAuthorization(TokenAuthorization):
    """Model that handles the account authorization flow."""
    reason_default = 'ACCOUNT_ACTIVATION'

    class Meta:
        proxy = True

    def get_absolute_url(self):
        args = [self.created_user.username, self.token]
        return reverse('umanage_activate_account', args=args)


class ChangeEmailAuthorization(TokenAuthorization):
    """Model that handles the change email flow."""
    reason_default = 'CHANGE_EMAIL'

    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('umanage_change_email_activation', args=[self.token])


class ForgotPasswordAuthorization(TokenAuthorization):
    """Model that handles the forgot password flow."""
    reason_default = 'FORGOT_PASSWORD'

    class Meta:
        proxy = True

    def get_absolute_url(self):
        args = [self.created_user.username, self.token]
        return reverse('umanage_forgot_password_change_password', args=args)
