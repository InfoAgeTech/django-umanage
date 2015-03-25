from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext as _
from django_core.forms.mixins.users import UserAuthorizationRequiredForm
from django_core.forms.widgets import ReadonlyWidget
from umanage.change_email.emails import send_change_email_activation_email
from umanage.change_email.emails import send_change_email_notice_email
from umanage.models import ChangeEmailAuthorization


class ChangeEmailForm(UserAuthorizationRequiredForm):
    """Form for changing a user's email."""
    error_messages = dict(UserAuthorizationRequiredForm.error_messages, **{
        'invalid_confirm_email': _("The new email and new email confirm must "
                                   "match exactly. Please enter it again."),
    })
    current_email = forms.EmailField(label=_('Current Email'),
                                     max_length=100, widget=ReadonlyWidget,
                                     required=False)
    new_email = forms.EmailField(label=_('New Email'))
    new_email_confirm = forms.EmailField(label=_('New Email Confirm'))

    def __init__(self, *args, **kwargs):
        super(ChangeEmailForm, self).__init__(*args, **kwargs)

        if 'current_email' not in self.initial:
            self.initial['current_email'] = self.user.email

        self.fields.keyOrder = ('current_email', 'password', 'new_email',
                                'new_email_confirm')

    def clean_new_email_confirm(self):
        new_email = self.cleaned_data['new_email']
        new_email_confirm = self.cleaned_data['new_email_confirm']

        if new_email != new_email_confirm:
            raise forms.ValidationError(
                self.error_messages['invalid_confirm_email'],
                code='invalid_confirm_email',
            )

        return new_email_confirm

    def send_email(self):
        """Sends the necessary emails and returns the ChangeEmail object. This
        method assumes the form has already made a call to ``.clean(...)``.
        """
        authorization = ChangeEmailAuthorization.objects.create(
            new_email_address=self.cleaned_data.get('new_email'),
            created_user=self.user
        )
        send_change_email_notice_email(
            to_user=self.user,
            authorization=authorization
        )
        send_change_email_activation_email(
            to_user=self.user,
            to_email=self.cleaned_data.get('new_email'),
            authorization=authorization
        )
        return authorization
