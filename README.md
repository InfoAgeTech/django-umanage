[<img src="https://travis-ci.org/InfoAgeTech/django-umanage.png?branch=master">](http://travis-ci.org/InfoAgeTech/django-umanage)
[<img src="https://coveralls.io/repos/InfoAgeTech/django-umanage/badge.png">](https://coveralls.io/r/InfoAgeTech/django-umanage)
[<img src="https://badge.fury.io/py/django-core.png">](http://badge.fury.io/py/django-core)
[<img src="https://pypip.in/license/django-core/badge.png">](https://github.com/InfoAgeTech/django-core/blob/master/LICENSE)


django-umanage
==============

User management app for django.  This app solves the following user related workflows and the pages relating to their workflows:

* [account activation](./umanage/activate_account)
    * account activation
    * account activation token expired
    * account activation success
* [auth](./umanage/auth)
    * sign out 
* [change email address](./umanage/change_email)
    * change email address
    * change email address token expired
    * change email address email sent
    * change email address success
    * change email address activation
* [change password](./umanage/change_password)
    * change password
    * change password success
* [forgot password](./umanage/forgot_password)
    * forgot password
    * forgot password token expired
    * forgot password email sent
    * forgot password success
    * forgot password change password
* [forgot username](./umanage/forgot_username)
    * forgot username
    * forgot username email sent


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

3. ``urls.py``: Add desired urls to your ``urls.py`` file.   This app was designed so apps can inherit pieces of functionality or all functionality.  This was the reason that each use workflow has it's own folder. If all urls (workflows) are wanted, then add the following to your urls.py:

        urlpatterns = patterns('',
            url(r'', include('umanage.forgot_username.urls')),
            url(r'', include('umanage.forgot_password.urls')),
            url(r'^account', include('umanage.urls')),
        )
        
        # If that urls.py were expanded it could look something like
        urlpatterns = patterns('',
            url(r'', include('umanage.auth.urls')),
            url(r'', include('umanage.forgot_username.urls')),
            url(r'', include('umanage.forgot_password.urls')),
            url(r'^account', include('umanage.activate_account.urls')),
            url(r'^account', include('umanage.change_email.urls')),
            url(r'^account', include('umanage.change_password.urls')),
            url(r'^account/token-expired/?$', TokenExpiredView.as_view(), name='umanage_token_expired'),
        )

Settings
-------- 
1. ``UMANAGE_FROM_EMAIL``: *required* setting is used when sending emails to users.  An example would be something like:

        UMANAGE_FROM_EMAIL = 'noreply@mysitedomain.com'

2. ``UMANAGE_BASE_TEMPLATE``: *required* setting that is the gateway into your app to keep a consistent look and feel with your site.  This setting is the path to that template.  For example:

        # base_umanage.html in templates directory
        {% extends 'path/to/my/app_template.html' %}
        
        {% block content %}
            {% comment %}umanage_content This is a required block{% endcomment %}
            {% block umanage_content %}{% endblock %}
        {% endblock %}

        # settings.py
        UMANAGE_BASE_TEMPLATE = 'base_umanage.html'

3. ``UMANAGE_BASE_UNAUTHENTICATED_TEMPLATE``: *optional* setting is similar to ``UMANAGE_BASE_TEMPLATE`` except this would be the base template for unauthenticated views.  This defaults to using the same value as ``UMANAGE_BASE_TEMPLATE``.

        # base_umanage.html in templates directory
        {% extends 'path/to/my/unauthenticated_app_template.html' %}
        
        {% block content %}
            {% comment %}umanage_content This is a required block{% endcomment %}
            {% block umanage_content %}{% endblock %}
        {% endblock %}

        # settings.py
        UMANAGE_BASE_UNAUTHENTICATED_TEMPLATE = 'base_umanage.html'

4. ``UMANAGE_FORM_RENDERER``: *optional* setting that allows your app to defined a location to a function that renders forms.  It can be any function that requires a single argument, the form object to render.  This defaults to calling django ``as_table()`` form rendering function.  For example, let's say I want to render forms using the [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) app. Inside the app is a method to render forms called ``bootstrap(...)``.  So in the settings, I would define the for renderer as:

        UMANAGE_FORM_RENDERER = 'bootstrapform.templatetags.bootstrap.bootstrap'

5. ``UMANAGE_SITE_NAME``: required setting that is used as the signature as well as other places that refer to your site's name.

        UMANAGE_SITE_NAME = 'My Awesome Site'

6. ``UMANAGE_SITE_ROOT_URI``: required setting that is the root site uri for you site.  This is used to construct urls in emails that will link back to your site.

        UMANAGE_SITE_ROOT_URI = 'http://thisismydomain.com/'

7. ``UMANAGE_USER_ACCOUNT_DISPLAY_FIELDS``: *optional* setting that is a tuple of user field names to display on the account page.

        UMANAGE_USER_ACCOUNT_DISPLAY_FIELDS = ('first_name', 'last_name', 'email', 'is_staff', 'is_active')
        
8. ``UMANAGE_USER_ACCOUNT_EDIT_FORM``: *optional* setting which is the path to your custom account edit form.  The form must be a model form.  The easiest thing to do would be to just extend from the existing ``UserAccountForm``:

        # custom form in my_app/forms.py
        from umanage.accounts.forms import UserAccountForm
        
        class MyAppUserAccountForm(UserAccountForm):
            
            class Meta:
                model = MyUserModel
        
        # in settings.py
        UMANAGE_USER_ACCOUNT_EDIT_FORM = 'my_app.forms.MyAppUserAccountForm'



For a configuration example, look at the tests [settings.py](/tests/settings.py) file.