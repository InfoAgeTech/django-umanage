from __future__ import unicode_literals

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext as _


class UManageRequiredSettingImproperlyConfigured(ImproperlyConfigured):
    """UManange exceptions for not having a correct settings key."""

    def __init__(self, settings_key=None, message=None, *args, **kwargs):

        if not message and settings_key is not None:
            message = _('No setting found for "{0}".  This is a required '
                        'setting for the django-umanage app.'.format(
                                                                settings_key))

        super(UManageRequiredSettingImproperlyConfigured, self).__init__(
            message,
            *args,
            **kwargs
        )


class UManageSettingImproperlyConfigured(ImproperlyConfigured):
    """UManange exceptions for not having a correct settings key."""

    def __init__(self, settings_key=None, message=None, *args, **kwargs):

        if not message and settings_key is not None:
            message = _('"{0}" setting is set incorrectly.'.format(
                settings_key
            ))

        super(UManageSettingImproperlyConfigured, self).__init__(
            message,
            *args,
            **kwargs
        )
