{% comment %}
This is an email template for the change email activation flow where the user needs to verify they have access to the emailed address they changed the email to.

Variables:

- to_user: the user that changed their email
- umanage_change_email_activation_url: the activation url

{% endcomment %}

Dear {{ to_user.username }},

You requested a change of your email address at {{ site_name }}.

Please confirm this email address by clicking on the link below:

- {{ umanage_change_email_activation_url }}


Thanks for using our site!

Sincerely,

{{ site_name }}