from django.conf import settings


def template_name(request):
    """Common settings to put in context."""
    # TODO: Probably want to throw a improperly configured error here if they
    #       don't have this in settings
    template_path = getattr(settings,
                            'UMANAGE_BASE_TEMPLATE',
                            'umanage/base_umanage.html')
    return {
        'UMANAGE_BASE_TEMPLATE': template_path
    }
