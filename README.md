django-umanage
==============

User management app for django.  This app solves the following workflows:

* account activation
* change password
* reset password
* change email address
* forgot username
* forgot password


Dependencies
============
* django-core
* markdown - used for email template conversion so the emails have to be written only once without having to maintain a .txt and .html version.  The markdown version is the email version.

Installation
============

    pip install django-umanage


DOC TODOS
=========
* add to installed apps
* context_processors
* UMANAGE_BASE_TEMPLATE setting
* adding to urls.py
* add "UMANAGE_FROM_EMAIL" in settings.py
* SITE_ROOT_URI setting in settings.py
* SITE_NAME setting in settings.py
* python markdown dependency for emails
* UMANAGE_BASE_HTML_TEMPLATE for overriding the base html template