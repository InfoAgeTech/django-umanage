from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string


def umanage_send_email(to_user, subject, text_template, html_template,
                       from_email=None, fail_silently=False, context=None):
    """Sends an email to a user."""
    if not to_user.email:
        return

    if not from_email:
        # TODO: Error handling here if not configured
        try:
            from_email = getattr(settings, 'UMANAGE_FROM_EMAIL')
        except AttributeError as e:
            raise ImproperlyConfigured(
                _('No setting found for "UMANAGE_FROM_EMAIL".  This is a '
                  'required setting for the django-umanage app in order to '
                  'send emails.'))

    if not context:
        context = {}

    context['to_user'] = to_user
    # context['MEDIA_URL'] = settings.MEDIA_URL
    # context['SITE_ROOT_URI'] = settings.SITE_ROOT_URI

    text_content = render_to_string(text_template, context)
    html_content = render_to_string(html_template, context)
    msg = EmailMultiAlternatives(subject=subject,
                                 body=text_content,
                                 from_email=from_email,
                                 to_email=to_user.email)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
