from __future__ import unicode_literals

from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from django_core.db.models.mixins.base import AbstractBaseModel
from django_core.db.models.mixins.tokens import AbstractTokenModel
from django.core.urlresolvers import reverse


class ChangeEmail(AbstractTokenModel, AbstractBaseModel):
    """Model that handles the change email flow."""
    new_email_address = models.EmailField()
    expires = models.DateTimeField()
    token_length = 75

    def save(self, *args, **kwargs):

        if not self.expires:
            # token is valid for 7 days
            self.expires = datetime.utcnow() + relativedelta(days=7)

        super(ChangeEmail, self).save(*args, **kwargs)

    def is_valid(self):
        """Boolean indicating if the token for the email change is valid."""
        return datetime.utcnow() < self.expires

    def get_absolute_url(self):
        return reverse('umanage_change_email_activation', args=[self.token])

    def expire(self):
        """Expires the change email token so it's no longer valid."""
        self.expires = datetime(1970, 1, 1)
        self.save()
