{% comment %}
This is the email send to the current user's email address alerting them that
the email change was requested.

variables:

- to_user: the user the email is to
- new_email: the new email address

{% endcomment %}
{% load i18n %}

Dear {{ to_user.username }},

There was a request to change your email address at {{ site_root_uri }}.

An email has been send to {{ new_email }} which contains a verification link. Click on the link in this email to activate it.

Thanks for using our site!

Sincerely,

{{ site_name }}