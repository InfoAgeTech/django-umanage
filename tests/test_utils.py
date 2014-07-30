from __future__ import unicode_literals

from django.test.testcases import TestCase
from django.test.utils import override_settings
from umanage.exceptions import UManageSettingImproperlyConfigured
from umanage.utils.configuration import get_required_setting


class UManageUtilsTestCase(TestCase):
    """Test case for utilities."""

    @override_settings(MY_SETTING='HELLO_WORLD')
    def test_get_required_settings(self):
        val = get_required_setting(settings_key='MY_SETTING')
        self.assertEqual(val, 'HELLO_WORLD')

    def test_get_required_settings_fail(self):
        """Test for ensuring the proper exception is thrown."""
        with self.assertRaises(UManageSettingImproperlyConfigured):
            val = get_required_setting(settings_key='NON_EXISTENT_SETTING')
            self.assertEqual(val, 'HELLO_WORLD')
