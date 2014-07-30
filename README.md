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


DOC TODOS
=========
* add to installed apps
* context_processors ``umanage.context_processors.template_name``
* UMANAGE_BASE_TEMPLATE setting
* form rendering configuration
* adding to urls.py
* add "UMANAGE_FROM_EMAIL" in settings.py
* SITE_ROOT_URI setting in settings.py
* SITE_NAME setting in settings.py
* python markdown dependency for emails
* UMANAGE_BASE_HTML_TEMPLATE for overriding the base html template
* UMANAGE_BASE_UNAUTHENTICATED_TEMPLATE setting for using the unauthenticated template (defaults to UMANAGE_BASE_TEMPLATE if it doesn't exist)
* forgot username url configuration

Tests
=====
TODO: write tests and explain how to run them