from __future__ import unicode_literals

from django.utils.translation import ugettext as _

from ..utils.emails import umanage_send_email


def send_change_forgot_username_email(to_user,
                                      markdown_template='umanage/emails/forgot_username.md',
                                      **kwargs):
    """Sends an email to a user letting them know their username."""
    return umanage_send_email(
        to_user=to_user,
        subject=_('The Username You Requested'),
        markdown_template=markdown_template,
        **kwargs)
