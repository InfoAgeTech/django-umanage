from __future__ import unicode_literals

from django import forms
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django_core.forms.widgets import ReadonlyWidget


class UserAccountForm(forms.ModelForm):
    """Form for editing a user account."""
    email = forms.EmailField(label=_('Email Address'),
                             widget=ReadonlyWidget,
                             required=False)

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserAccountForm, self).__init__(*args, **kwargs)
        self.fields['email'].help_text = '<a href="{0}">{1}</a>'.format(
            reverse('umanage_change_email'),
            _('change')
        )

    def clean_email(self):
        """Email is readonly."""
        return self.instance.email
