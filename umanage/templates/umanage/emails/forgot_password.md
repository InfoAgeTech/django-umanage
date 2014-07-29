{% comment %}
This is an email template for a user who forgot their password.

Variables:

- to_user: the user that forgot their username

{% endcomment %}

You requested to reset your password. You can use the following link within the next day to do so:

{{ umanage_forgot_password_change_password_url }}

If you don't use this link within 24 hours, it will expire. To get a new password reset link, visit {{ forgot_password_url }}.

Thanks for using our site!

Sincerely,

{{ site_name }}