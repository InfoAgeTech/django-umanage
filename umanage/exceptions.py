from __future__ import unicode_literals

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext as _
from umanage import APP_URL


class UManageSettingImproperlyConfigured(ImproperlyConfigured):
    """UManange exceptions for not having a correct settings key."""

    def __init__(self, settings_key, message=None, *args, **kwargs):

        if not message:
            message = _('No setting found for "{0}".  This is a required '
                        'setting for the django-umanage app. For more '
                        'information see:\n\n{1}'.format(settings_key,
                                                         APP_URL))

        super(UManageSettingImproperlyConfigured, self).__init__(
            message=message,
            *args, **kwargs
        )
