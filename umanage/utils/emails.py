from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from markdown import markdown


def umanage_send_email(to_user, subject, markdown_template=None,
                       text_template=None, html_template=None, from_email=None,
                       fail_silently=False, context=None):
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

    context = _get_email_context(context)
    context['to_user'] = to_user
    # context['MEDIA_URL'] = settings.MEDIA_URL
    # context['SITE_ROOT_URI'] = settings.SITE_ROOT_URI

    base_html_template = getattr(settings,
                                 'UMANAGE_BASE_HTML_TEMPLATE',
                                 'umanage/emails/base_email.html')

    context['umanage_base_html_email_template'] = base_html_template

    if markdown_template:
        text_content = render_to_string(markdown_template, context)
        context['email_content'] = markdown(text_content)
        html_content = render_to_string(base_html_template, context)
    else:
        text_content = render_to_string(text_template, context)
        html_content = render_to_string(html_template, context)

    msg = EmailMultiAlternatives(subject=subject,
                                 body=text_content,
                                 from_email=from_email,
                                 to=[to_user.email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def _get_email_context(context=None):
    if not context:
        context = {}

    try:
        context['site_root_uri'] = getattr(settings, 'SITE_ROOT_URI')
    except AttributeError as e:
        raise ImproperlyConfigured(
            _('No setting found for "SITE_ROOT_URI".  This is a '
              'required setting for the django-umanage app in order to '
              'send certain emails.'))

    try:
        context['site_name'] = getattr(settings, 'SITE_NAME')
    except AttributeError as e:
        raise ImproperlyConfigured(
            _('No setting found for "SITE_NAME".  This is a '
              'required setting for the django-umanage app in order to '
              'send emails.'))

    return context
