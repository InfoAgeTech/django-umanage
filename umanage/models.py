from __future__ import unicode_literals

from datetime import datetime
from datetime import timedelta

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django_core.db.models.mixins.base import AbstractBaseModel
from django_core.db.models.mixins.tokens import AbstractTokenModel


@python_2_unicode_compatible
class TokenAuthorization(AbstractTokenModel, AbstractBaseModel):
    """Model that provides a token for authorization purposes."""
    new_email_address = models.EmailField(blank=True, null=True)
    expires = models.DateTimeField()
    token_length = 75

    def save(self, *args, **kwargs):

        if not self.expires:
            # token is valid for 24 hours if not set
            self.expires = datetime.utcnow() + timedelta(
                days=1
            )

        super(TokenAuthorization, self).save(*args, **kwargs)

    def is_valid(self):
        """Boolean indicating if the token is valid."""
        return not self.is_expired()

    def is_expired(self):
        """Boolean indicating if the token for the has expired."""
        return datetime.utcnow() > self.expires

    def expire(self):
        """Expires the change email token so it's no longer valid."""
        self.expires = datetime(1970, 1, 1)
        self.save()


@python_2_unicode_compatible
class AccountActivationAuthorization(TokenAuthorization):
    """Model that handles the account authorization flow."""

    class Meta:
        proxy = True

    def get_absolute_url(self):
        args = [self.created_user.username, self.token]
        return reverse('umanage_activate_account', args=args)


@python_2_unicode_compatible
class ChangeEmailAuthorization(TokenAuthorization):
    """Model that handles the change email flow."""

    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('umanage_change_email_activation', args=[self.token])


@python_2_unicode_compatible
class ForgotPasswordAuthorization(TokenAuthorization):
    """Model that handles the forgot password flow."""

    class Meta:
        proxy = True

    def get_absolute_url(self):
        args = [self.created_user.username, self.token]
        return reverse('umanage_forgot_password_change_password', args=args)
