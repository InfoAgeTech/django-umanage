{% comment %}
This is an email template for a user who forgot their username.

Variables:

- to_user: the user that forgot their username

{% endcomment %}

You requested your username for {{ site_name }}. Your username is:

{{ to_user.username }}

Thanks for using our site!

Sincerely,

{{ site_name }}