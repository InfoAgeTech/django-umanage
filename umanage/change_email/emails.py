from __future__ import unicode_literals

from urllib.parse import urljoin

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext as _

from ..utils.emails import umanage_send_email


def send_change_email_notice_email(to_user, change_email_obj,
                                   markdown_template='umanage/emails/change_email_requested.md',
                                   **kwargs):
    """Sends an email to a user alerting them that their email has been
    requested to change.
    """
    context = _get_change_email_context(to_user, change_email_obj)
    return umanage_send_email(
        to_user=to_user,
        subject=_('Email Change Requested'),
        markdown_template=markdown_template,
        context=context,
        **kwargs)


def send_change_email_activation_email(to_user, change_email_obj,
                                       markdown_template='umanage/emails/change_email_activation.md',
                                       **kwargs):
    """Sends an email to the address of the newly provided email for
    activation.
    """
    context = _get_change_email_context(to_user, change_email_obj)
    url = urljoin(context.get('site_root_uri'),
                  change_email_obj.get_absolute_url())
    context['umanage_change_email_activation_url'] = url

    return umanage_send_email(
        to_user=to_user,
        subject=_('Activate New Email Address'),
        markdown_template=markdown_template,
        context=context,
        **kwargs)


def _get_change_email_context(to_user, change_email_obj):
    """Common context for the change email flow."""
    context = {
        # 'to_user': to_user,
        'new_email': change_email_obj.new_email_address
    }

    try:
        context['site_root_uri'] = getattr(settings, 'SITE_ROOT_URI')
    except AttributeError as e:
        raise ImproperlyConfigured(
            _('No setting found for "SITE_ROOT_URI".  This is a '
              'required setting for the django-umanage app in order to '
              'send certain emails.'))

    return context
