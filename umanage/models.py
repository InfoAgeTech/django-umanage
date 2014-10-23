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
    """Model that provides a token for authorization purposes.
    
    Fields:
    
    * expires: the date and time when the token expires
    * reason: a reason the token was generated.  This is preferably a constant
        but can be any string value.
    """
    new_email_address = models.EmailField(blank=True, null=True)
    expires = models.DateTimeField()
    reason = models.CharField(max_length=50, blank=True, null=True)
    token_length = 75

    def __str__(self, *args, **kwargs):
        return str(self.id)

    def save(self, *args, **kwargs):

        if not self.expires:
            # token is valid for 24 hours if not set
            self.expires = datetime.utcnow() + timedelta(days=1)

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


class AccountActivationAuthorization(TokenAuthorization):
    """Model that handles the account authorization flow."""

    class Meta:
        proxy = True

    def get_absolute_url(self):
        args = [self.created_user.username, self.token]
        return reverse('umanage_activate_account', args=args)


class ChangeEmailAuthorization(TokenAuthorization):
    """Model that handles the change email flow."""

    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('umanage_change_email_activation', args=[self.token])


class ForgotPasswordAuthorization(TokenAuthorization):
    """Model that handles the forgot password flow."""

    class Meta:
        proxy = True

    def get_absolute_url(self):
        args = [self.created_user.username, self.token]
        return reverse('umanage_forgot_password_change_password', args=args)
