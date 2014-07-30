from __future__ import unicode_literals

from django.conf import settings

from umanage.utils.configuration import get_required_setting


def common(request):
    """Common settings to put in context."""
    template_path = get_required_setting('UMANAGE_BASE_TEMPLATE')

    if not request.user.is_authenticated():
        template_path = getattr(settings,
                                'UMANAGE_BASE_UNAUTHENTICATED_TEMPLATE',
                                template_path)

    return {
        'UMANAGE_BASE_TEMPLATE': template_path
    }
