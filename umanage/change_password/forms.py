from __future__ import unicode_literals

from django.contrib.auth.forms import PasswordChangeForm
from django_core.utils.validators import validate_password_strength


class UManagePasswordChangeForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(UManagePasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].validators.append(validate_password_strength)
