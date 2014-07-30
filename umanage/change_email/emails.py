from __future__ import unicode_literals

try:
    # python 2
    from urlparse import urljoin
except ImportError:
    # python 3
    from urllib.parse import urljoin

from django.utils.translation import ugettext as _

from ..utils.configuration import get_required_setting
from ..utils.emails import umanage_send_email


def send_change_email_notice_email(to_user,
                                   authorization,
                                   markdown_template='umanage/emails/change_email_requested.md',
                                   **kwargs):
    """Sends an email to a user alerting them that their email has been
    requested to change.
    """
    context = _get_change_email_context(to_user, authorization)
    return umanage_send_email(
        to_user=to_user,
        subject=_('Email Change Requested'),
        markdown_template=markdown_template,
        context=context,
        **kwargs)


def send_change_email_activation_email(to_user,
                                       authorization,
                                       markdown_template='umanage/emails/change_email_activation.md',
                                       **kwargs):
    """Sends an email to the address of the newly provided email for
    activation.
    """
    context = _get_change_email_context(to_user, authorization)
    url = urljoin(context.get('site_root_uri'),
                  authorization.get_absolute_url())
    context['umanage_change_email_activation_url'] = url

    return umanage_send_email(
        to_user=to_user,
        subject=_('Activate New Email Address'),
        markdown_template=markdown_template,
        context=context,
        **kwargs)


def _get_change_email_context(to_user, authorization):
    """Common context for the change email flow."""
    context = {
        'new_email': authorization.new_email_address,
        'site_root_uri': get_required_setting('UMANAGE_SITE_ROOT_URI')
    }

    return context
