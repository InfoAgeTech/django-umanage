from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.test.testcases import TestCase
from django_core.utils.random_utils import random_alphanum
from django_testing.user_utils import create_user
from umanage.forgot_password.forms import ForgotPasswordForm
from umanage.forgot_username.forms import ForgotUsernameForm


class UManageForgotPasswordFormsTestCase(TestCase):
    """Test case for forgot password forms."""

    def test_forgot_password_form_username_valid(self):
        """Test the forgot password user's username"""
        user = create_user()
        form = ForgotPasswordForm(data={'username_or_email': user.username})
        self.assertTrue(form.is_valid())
        self.assertEqual(user.username, form.clean_username_or_email())

    def test_forgot_password_form_email_valid(self):
        """Test the forgot password user's email"""
        user = create_user()
        form = ForgotPasswordForm(data={'username_or_email': user.email})
        self.assertTrue(form.is_valid())
        self.assertEqual(user.email, form.clean_username_or_email())

    def test_forgot_password_form_user_invalid(self):
        """Test the forgot password user's email"""
        form = ForgotPasswordForm(data={'username_or_email': random_alphanum()})
        self.assertFalse(form.is_valid())

        with self.assertRaises(ValidationError):
            form.clean_username_or_email()

    def test_forgot_password_form_send_email(self):
        """Test the forgot password email is sent."""
        user = create_user()
        form = ForgotPasswordForm(data={'username_or_email': user.email})
        form.is_valid()
        form.send_email()


class UManageForgotUsernameFormsTestCase(TestCase):
    """Test case for forgot username forms."""

    def test_forgot_username_form_email_valid(self):
        """Test the forgot username valid email"""
        user = create_user()
        form = ForgotUsernameForm(data={'email': user.email})
        self.assertTrue(form.is_valid())
        self.assertEqual(user.email, form.clean_email())

    def test_forgot_username_form_email_invalid(self):
        """Test the forgot username user's email"""
        random_email = '{0}@{1}.com'.format(random_alphanum(5),
                                            random_alphanum(5))
        form = ForgotUsernameForm(data={'email': random_email})
        self.assertFalse(form.is_valid())

        form.cleaned_data['email'] = random_email

        with self.assertRaises(ValidationError):
            form.clean_email()

    def test_forgot_username_form_send_email(self):
        """Test the forgot username valid email"""
        user = create_user()
        form = ForgotUsernameForm(data={'email': user.email})
        form.is_valid()
        form.send_email()
