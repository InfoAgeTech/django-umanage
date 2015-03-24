from __future__ import unicode_literals

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
from django_core.utils.validators import is_valid_email
from django_core.utils.validators import validate_password_strength

from ..models import ForgotPasswordAuthorization
from .emails import send_forgot_password_email


class ForgotPasswordForm(forms.Form):
    """Form for forgot password."""
    username_or_email = forms.CharField(max_length=100)

    def clean_username_or_email(self):

        username_or_email = self.cleaned_data.get('username_or_email', '')
        username_or_email = username_or_email.strip()

        User = get_user_model()

        try:
            if is_valid_email(username_or_email):
                user = User.objects.get(email__iexact=username_or_email)
            else:
                user = User.objects.get(username__iexact=username_or_email)
        except User.DoesNotExist as e:
            raise ValidationError(_('No user found matching that username or '
                                    'email.'))

        self.user = user
        return username_or_email

    def send_email(self):
        """Sends the email for the forgot password flow"""
        authorization = ForgotPasswordAuthorization.objects.create(
            created_user=self.user
        )
        send_forgot_password_email(to_user=self.user,
                                   authorization=authorization)


class UManageSetPasswordForm(SetPasswordForm):

    next = forms.CharField(max_length=200, required=False,
                           widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(UManageSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].validators.append(validate_password_strength)
