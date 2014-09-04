from __future__ import unicode_literals

from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

from umanage.forgot_username.emails import send_change_forgot_username_email


class ForgotUsernameForm(forms.Form):
    """Form for forgot password."""
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')

        User = get_user_model()

        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist as e:
            raise ValidationError(_('No user found with that email address.'))

        self.user = user
        return email

    def send_email(self):
        """Sends the email for the forgotten password."""
        send_change_forgot_username_email(to_user=self.user)
