from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test.utils import override_settings
from django_core.utils.random_utils import random_alphanum
from django_testing.testcases.auth import AuthenticatedUserTestCase
from django_testing.testcases.auth import UnauthenticatedUserTestCase
from django_testing.testcases.urls import UrlTestCaseMixin
from django_testing.user_utils import create_user
from umanage.exceptions import UManageSettingImproperlyConfigured
from umanage.models import AccountActivationAuthorization
from umanage.models import ChangeEmailAuthorization
from umanage.models import ForgotPasswordAuthorization

from .urls import urlpatterns


User = get_user_model()

UNAUTHENTICATED_URL_NAMES = [
    'umanage_forgot_password',
    'umanage_forgot_password_change_password',
    'umanage_forgot_password_expired',
    'umanage_forgot_password_sent',
    'umanage_forgot_password_success',
    'umanage_forgot_username',
    'umanage_forgot_username_sent'
]


class UManageAuthenticatedUrlTests(UrlTestCaseMixin, AuthenticatedUserTestCase):
    """Test case for ensuring all authenticated umanage urls return a correct
    response.
    """

    urlpatterns = urlpatterns
    exclude_url_names = UNAUTHENTICATED_URL_NAMES

    def test_umanage_forgot_password_view(self):
        """Test the forgot password url for a user who's already logged in
        which should redirect them.
        """
        self.response_test_get(
            url=reverse('umanage_forgot_password'),
            expected_status_code=302
        )

    def test_umanage_forgot_username_view(self):
        """Test the forgot username url for a user who's already logged in
        which should redirect them.
        """
        self.response_test_get(
            url=reverse('umanage_forgot_username'),
            expected_status_code=302
        )

    def test_umanage_change_email_view(self):
        """Test the change email url to ensure it renders correctly."""
        self.response_test_get(
            url=reverse('umanage_change_email')
        )

    def test_umanage_change_email_activation_view(self):
        """Test the change email activation url to ensure it renders correctly.
        """
        new_email_address = '{0}@{1}.com'.format(random_alphanum(5),
                                                 random_alphanum(5))
        authorization = ChangeEmailAuthorization.objects.create(
            created_user=self.user,
            new_email_address=new_email_address
        )
        self.response_test_get(
            url=authorization.get_absolute_url(),
            expected_status_code=302
        )

        test_user = User.objects.get(id=self.user.id)
        self.assertEqual(test_user.email, new_email_address)

    def test_umanage_activate_account_expired_view(self):
        """Test the activate account expired email url to ensure it renders
        correctly.
        """
        self.response_test_get(
            url=reverse('umanage_activate_account_expired')
        )

    def test_umanage_token_expired_view(self):
        """Test the token expired url to ensure it renders correctly."""
        self.response_test_get(
            url=reverse('umanage_token_expired')
        )

    def test_umanage_change_email_sent_view(self):
        """Test the change email sent url to ensure it renders correctly."""
        self.response_test_get(
            url=reverse('umanage_change_email_sent')
        )

    def test_umanage_change_email_success_view(self):
        """Test the change email success url to ensure it renders correctly.
        """
        self.response_test_get(
            url=reverse('umanage_change_email_success')
        )

    def test_umanage_change_email_expired_view(self):
        """Test the change email expired url to ensure it renders correctly."""
        self.response_test_get(url=reverse('umanage_change_email_expired'))

    def test_umanage_change_password_view(self):
        """Test the change password url to ensure it renders correctly."""
        self.response_test_get(url=reverse('umanage_change_password'))

    def test_umanage_change_password_success_view(self):
        """Test the change password success url to ensure it renders correctly.
        """
        self.response_test_get(url=reverse('umanage_change_password_success'))

    def test_umanage_activate_account_view(self):
        """Test the activate account url to ensure it renders correctly."""
        test_user = create_user()
        test_user.is_active = False
        test_user.save()

        self.assertFalse(test_user.is_active)

        authorization = AccountActivationAuthorization.objects.create(
            created_user=test_user
        )

        self.response_test_get(
            url=authorization.get_absolute_url(),
            expected_status_code=302
        )

        test_user = User.objects.get(id=test_user.id)
        self.assertTrue(test_user.is_active)

    def test_umanage_activate_account_success_view(self):
        """Test the activate account success url to ensure it renders
        correctly.
        """
        self.response_test_get(url=reverse('umanage_activate_account_success'))

    def test_umanage_logout_view(self):
        """Test the logout view renders correctly."""
        self.response_test_get(url=reverse('umanage_logout'))

    def test_umanage_account_view_view(self):
        """Test the account view renders correctly."""
        self.response_test_get(url=reverse('umanage_account_view'))

    @override_settings(UMANAGE_USER_ACCOUNT_DISPLAY_FIELDS=('non', 'existent'))
    def test_umanage_account_view_display_account_fields_imporperly_set(self):
        """Test that the error is thrown when setting is improperly set for
        display account fields.
        """
        with self.assertRaises(UManageSettingImproperlyConfigured):
            self.response_test_get(url=reverse('umanage_account_view'))

    def test_umanage_account_edit_view(self):
        """Test the account edit renders correctly."""
        self.response_test_get(url=reverse('umanage_account_edit'))

    @override_settings(UMANAGE_USER_ACCOUNT_EDIT_FORM='path.non.Existent')
    def test_umanage_account_edit_form_imporperly_set(self):
        """Test that the error is thrown when setting is improperly set for
        account edit form.
        """
        with self.assertRaises(UManageSettingImproperlyConfigured):
            self.response_test_get(url=reverse('umanage_account_edit'))


class UmanageUnauthenticatedUrlTests(UrlTestCaseMixin,
                                     UnauthenticatedUserTestCase):
    """Test case for ensuring unauthenticated umanage urls return a correct
    response.
    """

    url_names = UNAUTHENTICATED_URL_NAMES

    def test_umanage_forgot_password_view(self):
        """Test the forgot password url renders."""
        self.response_test_get(url=reverse('umanage_forgot_password'))

    def test_umanage_forgot_password_expired_view(self):
        """Test the forgot password expired token url renders."""
        self.response_test_get(url=reverse('umanage_forgot_password_expired'))

    def test_umanage_forgot_password_sent_view(self):
        """Test the forgot password email was sent url renders."""
        self.response_test_get(url=reverse('umanage_forgot_password_sent'))

    def test_umanage_forgot_password_success_view(self):
        """Test the forgot password success url renders."""
        self.response_test_get(url=reverse('umanage_forgot_password_success'))

    def test_umanage_forgot_password_change_password_view(self):
        """Test the forgot password change password url renders."""
        authorization = ForgotPasswordAuthorization.objects.create(
            created_user=create_user()
        )
        self.response_test_get(url=authorization.get_absolute_url())

    def test_umanage_forgot_username_view(self):
        """Test the forgot username url renders."""
        self.response_test_get(url=reverse('umanage_forgot_username'))

    def test_umanage_forgot_username_sent_view(self):
        """Test the forgot username email sent url renders."""
        self.response_test_get(url=reverse('umanage_forgot_username_sent'))
