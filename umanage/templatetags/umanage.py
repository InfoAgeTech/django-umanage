from __future__ import unicode_literals

from django.template import Library
from django_core.utils.loading import get_function_from_settings
from django.conf import settings


register = Library()


@register.filter
def render_umanage_form(form):
    """Renders a form based on settings ``UMANAGE_FORM_RENDERER``
    setting.  This allows users to plug in different 3rd party form rendering
    apps while being able to maintain a consistent look and feel across their
    site.

    The function must accept 1 argument which is the form to be rendered. No
    other args will be passed.

    For example,  if I want to use the
    `django-bootstrap-form <https://github.com/tzangms/django-bootstrap-form>`_
    app to render forms, I would provide the following setting to the template
    tag form rendering function::

        UMANAGE_FORM_RENDERER = 'bootstrapform.templatetags.bootstrap.bootstrap'

    Then all forms will render using the django-bootstrap-form library.  You
    can optionally provide the following strings that will render that form
    using table, paragraph or list tags::

        UMANAGE_FORM_RENDERER = 'as_p'     # render form using <p> tags
        UMANAGE_FORM_RENDERER = 'as_table' # render form using <table>
        UMANAGE_FORM_RENDERER = 'as_ul'    # render form using <ul>

    This will default to rending the form to however the form's ``__str__``
    method is defined.
    """
    form_renderer_key = 'UMANAGE_FORM_RENDERER'
    form_renderer_str = getattr(settings, form_renderer_key, None)

    if form_renderer_str and '.' in form_renderer_str:
        renderer_func = get_function_from_settings(form_renderer_key)
        return renderer_func(form) if renderer_func else form

    if form_renderer_str == 'as_table':
        return form.as_table()

    if form_renderer_str == 'as_ul':
        return form.as_ul()

    if form_renderer_str == 'as_p':
        return form.as_p()

    return form
