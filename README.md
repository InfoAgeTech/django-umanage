[<img src="https://travis-ci.org/InfoAgeTech/django-umanage.png?branch=master">](http://travis-ci.org/InfoAgeTech/django-umanage)
[<img src="https://coveralls.io/repos/InfoAgeTech/django-umanage/badge.png">](https://coveralls.io/r/InfoAgeTech/django-umanage)
[<img src="https://badge.fury.io/py/django-core.png">](http://badge.fury.io/py/django-core)
[<img src="https://pypip.in/license/django-core/badge.png">](https://github.com/InfoAgeTech/django-core/blob/master/LICENSE)


django-umanage
==============

User management app for django.  This app solves the following user related workflows:

* [account activation](./umanage/activate_account)
* [change password](./umanage/change_password)
* [change email address](./umanage/change_email)
* [forgot username](./umanage/forgot_username)
* [forgot password](./umanage/forgot_password)


Dependencies
============
* [django-core](https://github.com/InfoAgeTech/django-core) - provides a number of django related helpful utilities
* [markdown](https://github.com/waylan/Python-Markdown) - used for email template conversion so the emails have to be written only once without having to maintain a .txt and .html version.  The markdown version is the text email version.

Installation
============

    pip install django-umanage

Configuration
=============
1. Add to ``INSTALLED_APPS`` in your ``settings.py``:

        INSTALLED_APPS = (
            ...
            'umanage',
            ...
        )

2. Add context processor to the ``TEMPLATE_CONTEXT_PROCESSORS`` in ``settings.py``:

        TEMPLATE_CONTEXT_PROCESSORS = (
            ...
            'umanage.context_processors.common',
            ...
        )

3. ``UMANAGE_FROM_EMAIL``: *required* setting is used when sending emails to users.  An example would be something like:

        UMANAGE_FROM_EMAIL = 'noreply@mysitedomain.com'

4. ``UMANAGE_BASE_TEMPLATE``: *required* setting that is the gateway into your app to keep a consistent look and feel with your site.  This setting is the path to that template.  For example:

        # base_umanage.html in templates directory
        {% extends 'path/to/my/app_template.html' %}
        
        {% block content %}
            {% comment %}umanage_content This is a required block{% endcomment %}
            {% block umanage_content %}{% endblock %}
        {% endblock %}

        # settings.py
        UMANAGE_BASE_TEMPLATE = 'base_umanage.html'

5. ``UMANAGE_BASE_UNAUTHENTICATED_TEMPLATE``: *optional* setting is similar to ``UMANAGE_BASE_TEMPLATE`` except this would be the base template for unauthenticated views.  This defaults to using the same value as ``UMANAGE_BASE_TEMPLATE``.

        # base_umanage.html in templates directory
        {% extends 'path/to/my/unauthenticated_app_template.html' %}
        
        {% block content %}
            {% comment %}umanage_content This is a required block{% endcomment %}
            {% block umanage_content %}{% endblock %}
        {% endblock %}

        # settings.py
        UMANAGE_BASE_UNAUTHENTICATED_TEMPLATE = 'base_umanage.html'

6. ``UMANAGE_FORM_RENDERER``: *optional* setting that allows your app to defined a location to a function that renders forms.  It can be any function that requires a single argument, the form object to render.  This defaults to calling django ``as_table()`` form rendering function.  For example, let's say I want to render forms using the [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) app. Inside the app is a method to render forms called ``bootstrap(...)``.  So in the settings, I would define the for renderer as:

        UMANAGE_FORM_RENDERER = 'bootstrapform.templatetags.bootstrap.bootstrap'





DOC TODOS
=========
* UMANAGE_BASE_TEMPLATE setting
* form rendering configuration
* adding to urls.py
* add "UMANAGE_FROM_EMAIL" in settings.py
* SITE_ROOT_URI setting in settings.py
* SITE_NAME setting in settings.py
* UMANAGE_BASE_HTML_TEMPLATE for overriding the base html template
* UMANAGE_BASE_UNAUTHENTICATED_TEMPLATE setting for using the unauthenticated template (defaults to UMANAGE_BASE_TEMPLATE if it doesn't exist)
* forgot username url configuration

