from __future__ import unicode_literals

from django.conf import settings
from umanage.exceptions import UManageRequiredSettingImproperlyConfigured


def get_required_setting(settings_key, default=None):
    """Gets a required setting or throws an UManageSettingImproperlyConfigured
    exception if no default value is provided.
    """
    try:
        if default is None:
            return getattr(settings, settings_key)

        return getattr(settings, settings_key, default)
    except AttributeError as e:
        raise UManageRequiredSettingImproperlyConfigured(settings_key=settings_key)
