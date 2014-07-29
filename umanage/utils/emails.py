from __future__ import unicode_literals

from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from markdown import markdown

from umanage.utils.configuration import get_required_setting


def umanage_send_email(to_user, subject, markdown_template=None,
                       text_template=None, html_template=None, from_email=None,
                       fail_silently=False, context=None):
    """Sends an email to a user."""
    if not to_user.email:
        return

    if not from_email:
        from_email = get_required_setting('UMANAGE_FROM_EMAIL')

    context = _get_email_context(context)
    context['to_user'] = to_user

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

    text_content = mark_safe(text_content.strip())
    html_content = mark_safe(html_content.strip())

    msg = EmailMultiAlternatives(subject=subject,
                                 body=text_content,
                                 from_email=from_email,
                                 to=[to_user.email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def _get_email_context(context=None):
    if not context:
        context = {}

    context['site_root_uri'] = get_required_setting('SITE_ROOT_URI')
    context['site_name'] = get_required_setting('SITE_NAME')
    return context
