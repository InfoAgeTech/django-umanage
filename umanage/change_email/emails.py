from __future__ import unicode_literals

from urllib.parse import urljoin

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from ..utils.emails import umanage_send_email


def send_change_email_notice_email(to_user):
    """Sends an email to a user alerting them that their email has been
    requested to change.
    """
    return umanage_send_email(
        to_user=to_user,
        subject=_('Email Change Requested'),
        text_template='umanage/change_email/change_email_requested.txt',
        html_template='umanage/change_email/change_email_requested.html')


def send_change_email_activation_email(to_user, change_email):
    """Sends an email to the address of the newly provided email for
    activation.
    """
    try:
        site_root_uri = getattr(settings, 'SITE_ROOT_URI')
    except AttributeError as e:
        raise ImproperlyConfigured(
            _('No setting found for "SITE_ROOT_URI".  This is a '
              'required setting for the django-umanage app in order to '
              'send certain emails.'))

    url = reverse('umanage_change_email_activation', change_email.token)
    context = {
        'umanage_change_email_activation_url': urljoin(site_root_uri, url)
    }

    return umanage_send_email(
        to_user=to_user,
        subject=_('Activate New Email Address'),
        text_template='umanage/change_email/change_email_requested.txt',
        html_template='umanage/change_email/change_email_requested.html',
        context=context)
