from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django_core.views.mixins.auth import LoginRequiredViewMixin
from umanage.change_email.forms import ChangeEmailForm
from umanage.models import ChangeEmail


class ChangeEmailView(LoginRequiredViewMixin, FormView):
    """View for changing a user's email."""

    template_name = 'umanage/change_email/change_email.html'
    form_class = ChangeEmailForm

    def get_form_kwargs(self):
        form_kwargs = super(ChangeEmailView, self).get_form_kwargs()
        form_kwargs['user'] = self.request.user
        return form_kwargs

    def form_valid(self, form):
        form.send_email()
        return super(ChangeEmailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('umanage_change_email_sent')


class ChangeEmailSentView(LoginRequiredViewMixin, TemplateView):
    """View that confirms an email will be sent to the user to update the
    email address.
    """
    template_name = 'umanage/change_email/change_email_sent.html'


class ChangeEmailSuccessView(LoginRequiredViewMixin, TemplateView):
    """View that confirms an email has been updated successfully."""
    template_name = 'umanage/change_email/change_email_success.html'


class ChangeEmailActivationView(LoginRequiredViewMixin, TemplateView):

    template_name = 'umanage/change_email/change_email_invalid.html'

    def get(self, request, *args, **kwargs):
        change_email = ChangeEmail.objects.get_by_token_or_404(
            token=kwargs.get('change_email_token'),
            created_user=self.request.user
        )

        if not change_email.is_valid():
            return super(ChangeEmailActivationView, self).get(request, *args,
                                                              **kwargs)

        # It's a valid change email object, update the user's email
        self.request.user.email = change_email.new_email_address
        self.request.user.save()

        # Expire the change email token so it's no longer valid.
        change_email.expire()
        return redirect('umanage_change_email_success')
