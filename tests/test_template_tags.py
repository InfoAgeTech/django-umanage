from __future__ import unicode_literals

from django import forms
from django.test.testcases import TestCase
from django.test.utils import override_settings
from mock import patch
from umanage.templatetags.umanage import render_umanage_form


class TemplateTagTestCase(TestCase):
    """Test case for template tags."""

    @override_settings(UMANAGE_FORM_RENDERER='as_table')
    @patch('django.forms.forms.Form.as_table')
    def test_render_umanage_form_as_table(self, mock_as_table):
        frm = forms.Form()
        render_umanage_form(frm)
        self.assertTrue(mock_as_table.called)

    @override_settings(UMANAGE_FORM_RENDERER='as_ul')
    @patch('django.forms.forms.Form.as_ul')
    def test_render_umanage_form_as_ul(self, mock_as_ul):
        frm = forms.Form()
        render_umanage_form(frm)
        self.assertTrue(mock_as_ul.called)

    @override_settings(UMANAGE_FORM_RENDERER='as_p')
    @patch('django.forms.forms.Form.as_p')
    def test_render_umanage_form_as_p(self, mock_as_p):
        frm = forms.Form()
        render_umanage_form(frm)
        self.assertTrue(mock_as_p.called)
