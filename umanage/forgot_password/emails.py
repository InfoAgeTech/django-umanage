from __future__ import unicode_literals

try:
    # python 2
    from urlparse import urljoin
except ImportError:
    # python 3
    from urllib.parse import urljoin

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from ..utils.configuration import get_required_setting
from ..utils.emails import umanage_send_email


def send_forgot_password_email(to_user,
                               authorization,
                               markdown_template='umanage/emails/forgot_password.md',
                               **kwargs):
    """Sends an email to a user to reset their password.

    :param to_user: the user the email is for
    :param authorization: the ForgotPasswordAuthorization object to complete
        the flow.
    """
    context = _get_forgot_password_context(to_user)
    context['forgot_password_url'] = urljoin(
        context.get('site_root_uri'),
        reverse('umanage_forgot_password')
    )
    context['umanage_forgot_password_change_password_url'] = urljoin(
        context.get('site_root_uri'),
        authorization.get_absolute_url()
    )
    return umanage_send_email(
        to_user=to_user,
        subject=_('Password Reset'),
        markdown_template=markdown_template,
        context=context,
        **kwargs)


def _get_forgot_password_context(to_user):
    """Common context for the forgot password flow."""
    context = {
        'site_root_uri': get_required_setting('UMANAGE_SITE_ROOT_URI')
    }

    return context
